let eventSource;
let map, markers = [], polyline = null, mapShown = false;

function startLoading() {
    document.getElementById("planet").style.display = "block";
}

function stopLoading() {
    document.getElementById("planet").style.display = "none";
}

function clearOutput() {
    document.getElementById("output").innerHTML = "";
}

function closeEventSource() {
    if (eventSource) {
        eventSource.close();
        eventSource = null;
    }
}

function stopCommand() {
    closeEventSource();
    fetch('/stop', {method: 'POST'});
    stopLoading();
    document.getElementById("output").innerHTML += "<div class='line-info'>🛑 Процесът беше прекъснат.</div>";
    // clear map if desired: keep markers for manual review (optional)
}

async function geoLookup(ip) {
    if (!ip) return;
    try {
        const res = await fetch(`/geo?ip=${encodeURIComponent(ip)}`);
        const data = await res.json();
        if (data.error) return null;
        return data; // {ip, country, city, org, latitude, longitude}
    } catch {
        return null;
    }
}

function ensureMap() {
    if (mapShown) return;
    const mapDiv = document.getElementById('map');
    mapDiv.style.display = 'block';
    map = L.map('map').setView([0, 0], 2);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 18,
        attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);
    polyline = L.polyline([], {color: '#58a6ff'}).addTo(map);
    mapShown = true;
}

function addHopToMap(lat, lon, popupText) {
    if (lat == null || lon == null) return;
    ensureMap();
    try {
        const marker = L.marker([lat, lon]).addTo(map);
        marker.bindPopup(popupText);
        markers.push(marker);
        polyline.addLatLng([lat, lon]);
        // zoom/fit to show all markers
        const group = new L.featureGroup(markers);
        map.fitBounds(group.getBounds().pad(0.3));
    } catch (e) {
        console.log("Map add error:", e);
    }
}

function runCommand(cmd) {
    closeEventSource();
    startLoading();
    clearOutput();
    // reset map
    if (mapShown) {
        markers.forEach(m => map.removeLayer(m));
        markers = [];
        if (polyline) {
            polyline.setLatLngs([]);
        }
    }

    const target = document.getElementById("target").value.trim();
    if (!target) {
        alert("Въведи адрес или IP");
        stopLoading();
        return;
    }

    fetch('/stop', {method: 'POST'}).then(() => {
        eventSource = new EventSource(`/stream?cmd=${cmd}&target=${encodeURIComponent(target)}`);
        const out = document.getElementById("output");

        eventSource.onmessage = async (event) => {
            if (event.data === "[END]") {
                eventSource.close();
                stopLoading();
                return;
            }

            let text = event.data;
            console.log("LINE:", text);

            let cls = "line-default";
            if (text.includes("ttl=") || text.includes("bytes from")) cls = "line-success";
            else if (text.toLowerCase().includes("timeout") || text.toLowerCase().includes("unreachable") || text.includes("*")) cls = "line-fail";
            else if (text.match(/^\s*\d+/)) cls = "line-info";

            out.innerHTML += `<div class='${cls}'>${escapeHtml(text)}</div>`;
            out.scrollTop = out.scrollHeight;

            // По-точен regex: IP в скоби (1.2.3.4), standalone IPv4 или IPv6
            const ipMatch = text.match(/\((\d{1,3}(?:\.\d{1,3}){3})\)|(\d{1,3}(?:\.\d{1,3}){3})|([0-9a-fA-F:]{3,})/);
            if (cmd === "trace" && ipMatch) {
                const ip = ipMatch[1] || ipMatch[2] || ipMatch[3];
                if (ip) {
                    // покажи че търсим гео
                    out.innerHTML += `<div class='line-geo'>🔍 ${ip} — търся гео... </div>`;
                    out.scrollTop = out.scrollHeight;
                    const geo = await geoLookup(ip);
                    if (geo && (geo.latitude || geo.lat || geo.longitude || geo.lon)) {
                        const lat = geo.latitude || geo.lat || geo.latitude === 0 ? parseFloat(geo.latitude) : null;
                        const lon = geo.longitude || geo.lon || geo.longitude === 0 ? parseFloat(geo.longitude) : null;
                        const popup = `${geo.ip} — ${geo.city ? geo.city + ', ' : ''}${geo.country || ''}${geo.org ? ' — ' + geo.org : ''}`;
                        addHopToMap(lat, lon, popup);
                        out.innerHTML += `<div class='line-geo'>🧭 ${ip} → ${geo.city ? geo.city + ', ' : ''}${geo.country || 'Няма данни'} (${geo.org || '—'})</div>`;
                        out.scrollTop = out.scrollHeight;
                    } else {
                        out.innerHTML += `<div class='line-fail'>⚠️ ${ip} → Няма гео данни</div>`;
                        out.scrollTop = out.scrollHeight;
                    }
                }
            }
        };

        eventSource.onerror = () => {
            out.innerHTML += "<div class='line-fail'>⚠️ Грешка при връзката.</div>";
            stopLoading();
            eventSource.close();
        };
    });
}

// помощна функция за безопасен HTML output
function escapeHtml(unsafe) {
    return unsafe.replace(/[&<"'>]/g, function (m) {
        return {'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;'}[m];
    });
}
