import speedtest as sp
from alive_progress import alive_bar
import time

def main():

    starting_time = time.time()

    test = sp.Speedtest()

    download_speed = test.download()
    download_speed = f"{(download_speed / 10 ** 6):.2f}"

    stop_time = time.time()

    elapsed_time = stop_time - starting_time

    def compute():
        for sec in str(elapsed_time).split("."):
            print(sec)
            yield  # simply insert this :)

    with alive_bar(1000) as bar:
        for i in compute():
            bar()
    
    
    
    print("Download Speed in Mbps: ", download_speed)

    upload_speed = test.upload()
    upload_speed = f"{(upload_speed / 10 ** 6):.2f}"

    print("Upload Speed in Mbps: ", upload_speed)

    ping = test.results.ping


    print("Ping ", ping)



main()
