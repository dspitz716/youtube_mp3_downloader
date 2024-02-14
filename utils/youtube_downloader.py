from pytube import YouTube
from pytube import Playlist
import os



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
            return playlist
        
        elif '&list' in url:
            n = 1
            while n < 4:
                yn = str(input('''This song appears to be part of a playlist...
Would you like to download the entire playlist? y/n
>>'''))
                if yn.lower() == 'y':
                    playlist = Playlist(url)
                    pl = []
                    for video in playlist.video_urls:
                        pl.append(video)
                    return playlist
                elif yn.lower() == 'n':
                    yt = [url]
                    return yt
                else:
                    print(f'''Please respond y/n...
Attempt {n}/3''')
                    if n == 3:
                        print('Max attempts reached!')
                        break
                    else:
                        n += 1

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
