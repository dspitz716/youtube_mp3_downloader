from utils.youtube_downloader import YoutubeDownloader
import os
import tkinter as tk
from tkinter import filedialog

def main():

    root = tk.Tk()
    root.withdraw()
    print("Select location for mp3 download \n>>")
    dest = filedialog.askdirectory()
    url = str(input("Enter the URL of the video you want to download: \n>> "))
    youtube = YoutubeDownloader(url, dest)
    youtube.download()



if __name__ == '__main__':
    main()
