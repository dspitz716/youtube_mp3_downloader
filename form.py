import tkinter as tk
from youtube_downloader import YoutubeDownloader
from tkinter import filedialog
from tkinter import *


class Gui:
    def __init__(self):
        self.root = tk.Tk()

    

    def run(self):
        self.root.geometry("600x400")

        # declaring string variable
        url_var = tk.StringVar()
        play_var = tk.StringVar()


        # defining a function that will launch download method
        def submit():
            url = url_var.get()
            playlist = play_var.get()
            #password = passw_var.get()

            youtube = YoutubeDownloader(url, filepath, playlist)
            youtube.download()


        # creating a label for
        # name using widget Label
        name_label = tk.Label(self.root, text='Video/Playlist Url', font=('calibre', 10, 'bold'))

        # creating a entry for input
        # name using widget Entry
        name_entry = tk.Entry(self.root, textvariable=url_var, font=('calibre', 10, 'normal'))

        #playlist download name
        play_label = tk.Label(self.root, text='Download Whole Playlist? y/n (only req. for songs from playlist)', font=('calibre', 10, 'bold'))
        play_entry = tk.Entry(self.root, textvariable=play_var, font=('calibre', 10, 'normal'))

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
        play_label.grid(row=1, column=0)
        play_entry.grid(row=1, column=1)
        browse_label.grid(row=2, column=0)
        browsebutton.grid(row=2, column=1)
        pathlabel.grid(row=2, column=2)
        sub_btn.grid(row=3, column=1)

        # performing an infinite loop
        # for the window to display
        self.root.mainloop()
