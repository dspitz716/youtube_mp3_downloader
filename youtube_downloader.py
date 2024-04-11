from pytube import YouTube
from pytube import Playlist
import os
from pytube.innertube import _default_clients

_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]


class YoutubeDownloader:
    def __init__(self, url: str, dest: str):
        self.url = url
        self.dest = dest

    def object_generator(self, url):
        url = url
        if 'com/play' in url:
            playlist = Playlist(url)
            pl = []
            for video in playlist.video_urls:
                pl.append(video)
            return pl
                                 
        else:
            yt = [url]
            return yt

                    
                


    def download(self):
        videos = self.object_generator(self.url)
        try:
            for video in videos:
                try:
                    yt = YouTube(video)
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
        except TypeError:
            print("Something went wrong please try again later")
