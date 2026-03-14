from pytubefix import YouTube
from pytubefix import Playlist
import os

######COMBINED ALL MODULES INTO 1 FILE TO USE WITH PYINSTALLER EASILY

DEFAULT_DOWNLOAD_DIR = os.path.join(os.path.expanduser("~"), "Downloads")


class YoutubeDownloader:
    def __init__(self, url: str, dest: str):
        self.url = url
        self.dest = dest

    def object_generator(self, url):
        if 'com/play' in url:
            playlist = Playlist(url)
            return list(playlist.video_urls)
        else:
            return [url]

    def download(self):
        videos = self.object_generator(self.url)
        try:
            for video in videos:
                try:
                    yt = YouTube(video, use_oauth=False)
                    stream = yt.streams.filter(only_audio=True).first()
                    out = stream.download(output_path=self.dest)
                    base, ext = os.path.splitext(out)
                    new_file = base + '.mp3'
                    os.rename(out, new_file)
                    print(f"✓ '{yt.title}' downloaded successfully.")
                except KeyError:
                    print("Unable to fetch video information. Please check the video URL or your network connection.")
                except FileExistsError:
                    print("File already exists in that location.")
        except TypeError:
            print("Something went wrong, please try again later.")


def run():
    print("=== YouTube Downloader ===\n")

    url = input("Enter video or playlist URL: ").strip()

    dest_input = input(f"Download location (press Enter for default: {DEFAULT_DOWNLOAD_DIR}): ").strip()
    dest = dest_input if dest_input else DEFAULT_DOWNLOAD_DIR

    if not os.path.isdir(dest):
        print(f"Directory '{dest}' does not exist. Creating it...")
        os.makedirs(dest)

    print(f"\nDownloading to: {dest}\n")
    downloader = YoutubeDownloader(url, dest)
    downloader.download()


if __name__ == '__main__':
    run()