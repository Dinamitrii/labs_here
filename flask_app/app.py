import requests
import signal
import socket
import subprocess
import threading
from dotenv import load_dotenv
from flask import Flask, render_template, request, Response, stream_with_context, jsonify

app = Flask(__name__, template_folder="templates", static_folder="static")

load_dotenv(".flaskenv")

process_lock = threading.Lock()
current_process = None


def detect_ip_version(ip):
    try:
        socket.inet_pton(socket.AF_INET, ip)
        return 4
    except OSError:
        try:
            socket.inet_pton(socket.AF_INET6, ip)
            return 6
        except OSError:
            return None


def resolve_target(target):
    try:
        socket.inet_pton(socket.AF_INET, target)
        return target
    except OSError:
        try:
            socket.inet_pton(socket.AF_INET6, target)
            return target
        except OSError:
            try:
                return socket.getaddrinfo(target, None)[0][4][0]
            except Exception:
                return None


def stop_current_process():
    global current_process
    with process_lock:
        if current_process and current_process.poll() is None:
            try:
                current_process.send_signal(signal.SIGINT)
            except Exception:
                current_process.terminate()
        current_process = None


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/stop", methods=["POST"])
def stop_process():
    stop_current_process()
    return "stopped"


@app.route("/geo")
def geo_lookup():
    ip = request.args.get("ip", "").strip()
    if not ip:
        return jsonify({"error": "Missing IP"}), 400
    try:
        # ipapi.co дава полета latitude / longitude
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
        d = r.json()
        lat = d.get("latitude") or d.get("lat") or None
        lon = d.get("longitude") or d.get("lon") or None
        return jsonify({
            "ip": ip,
            "country": d.get("country_name", ""),
            "city": d.get("city", ""),
            "org": d.get("org", ""),
            "latitude": lat,
            "longitude": lon
        })
    except Exception:
        return jsonify({"error": "Lookup failed"}), 500


@app.route("/stream")
def stream_command():
    cmd_type = request.args.get("cmd")
    target = request.args.get("target", "").strip()
    if not target:
        return Response("❌ Няма зададен адрес.", mimetype="text/plain")

    ip = resolve_target(target)
    if not ip:
        return Response(f"❌ Неуспешно резолвиране на {target}", mimetype="text/plain")

    stop_current_process()
    ipver = detect_ip_version(ip)
    if cmd_type == "ping":
        cmd = ["ping6" if ipver == 6 else "ping", "-c", "20", ip]
    elif cmd_type == "trace":
        # използваме -n за GNU traceroute; ако средата го няма, команда ще покаже съобщение
        cmd = ["traceroute", ip]
    elif cmd_type == "whois":
        cmd = ["whois", ip]
    else:
        return Response("❌ Невалидна команда.", mimetype="text/plain")

    def generate():
        global current_process
        with process_lock:
            current_process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in iter(current_process.stdout.readline, ""):
            yield f"data: {line.rstrip()}\n\n"
        yield "data: [END]\n\n"

    return Response(stream_with_context(generate()), mimetype="text/event-stream")


if __name__ == "__main__":
    app.run()
