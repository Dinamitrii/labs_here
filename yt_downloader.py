from pytube import YouTube

link = input("Enter YT link:'    '")

def download(link):
    try:
        video = YouTube(link)
        video = video.streams.filter(file_extension="mp4").get_highest_resolution()
        video.download(link)
        print("Video downloaded")

    except:
        print("Video not downloaded")

