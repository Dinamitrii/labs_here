import speedtest as sp


def main():
    test = sp.Speedtest()

    download_speed = test.download()
    download_speed = f"{(download_speed / 10 ** 6):.2f}"
    print("Download Speed in Mbps: ", download_speed)

    upload_speed = test.upload()
    upload_speed = f"{(upload_speed / 10 ** 6):.2f}"
    print("Upload Speed in Mbps: ", upload_speed)

    ping = test.results.ping
    print("Ping ", ping)

main()