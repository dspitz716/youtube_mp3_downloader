from pytube import YouTube
import os



class YoutubeDownloader:
    def __init__(self, url: str, dest: str):
        self.url = url
        self.dest = dest

    def download_single(self):
        try:
            yt = YouTube(self.url)
            video = yt.streams.filter(only_audio=True).first()
            destination = self.dest
            out = video.download(output_path=destination)
            base, ext = os.path.splitext(out)
            new_file = base + '.mp3'
            os.rename(out, new_file)
            print(yt.title + " has been successfully downloaded.")
        except KeyError:
            print("Unable to fetch video information. Please check the video URL or your network connection.")
        except FileExistsError:
            print("File already exists in location")
