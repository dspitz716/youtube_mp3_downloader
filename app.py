
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from pytube import YouTube
from pytube import Playlist
import os

######COMBINED ALL MODULES INTO 1 FILE TO USE WITH PYINSTALLER EASILY

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

class Gui:
    def __init__(self):
        self.root = tk.Tk()

    

    def run(self):
        self.root.geometry("600x400")

        # declaring string variable
        url_var = tk.StringVar()


        # defining a function that will launch download method
        def submit():
            url = url_var.get()
            #password = passw_var.get()

            youtube = YoutubeDownloader(url, filepath)
            youtube.download()


        # creating a label for
        # name using widget Label
        name_label = tk.Label(self.root, text='Video/Playlist Url', font=('calibre', 10, 'bold'))

        # creating a entry for input
        # name using widget Entry
        name_entry = tk.Entry(self.root, textvariable=url_var, font=('calibre', 10, 'normal'))

        # opens file explorer
        def browsefunc():
            global filepath
            filepath = filedialog.askdirectory()
            pathlabel.config(text=filepath)
        
        browse_label = tk.Label(self.root, text='Download location', font=('calibre', 10, 'bold'))

        browsebutton = Button(self.root, text="Browse", command=browsefunc)


        pathlabel = Label(self.root)
        


        # creating a button using the widget
        # Button that will call the submit function
        sub_btn = tk.Button(self.root, text='Submit', command=submit)

        # placing the label and entry in
        # the required position using grid
        # method
        name_label.grid(row=0, column=0)
        name_entry.grid(row=0, column=1)
        browse_label.grid(row=1, column=0)
        browsebutton.grid(row=1, column=1)
        pathlabel.grid(row=1, column=2)
        sub_btn.grid(row=2, column=1)

        # performing an infinite loop
        # for the window to display
        self.root.mainloop()

    
if __name__ == '__main__':
    gui = Gui()
    gui.run()
