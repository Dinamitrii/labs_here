from pytube import YouTube

def download(link):
    try:
        video = YouTube(link)
        video = video.streams.get_highest_resolution()
        video.download()
        print("Video downloaded")

    except:
        print("Video not found")