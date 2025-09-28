from pytube import YouTube
from pytube.extract import video_id

link = input("Enter YT link:'    '")

def download(link):
    try:
        linked = YouTube(link)
        video = linked.streams.filter(file_extension="mp4").get_highest_resolution()
        video.
        print("Video downloaded")

    except:
        print("Video not downloaded")

