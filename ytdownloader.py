from pytubefix import YouTube
from tkinter import *
from tkinter import ttk
import ffmpeg

def download():
    link = entry.get()

    yt = YouTube(link)
    video = yt.streams.filter(adaptive=True, file_extension='mp4').order_by('resolution').desc().first().download(filename="video.mp4")
    audio = yt.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc().first().download(filename="audio.mp4")

    input_video = ffmpeg.input("video.mp4")
    input_audio = ffmpeg.input("audio.mp4")
    output = ffmpeg.concat(input_video, input_audio, v=1, a=1).output("output.mp4", acodec="aac")
    output.run()

root = Tk()
root.minsize(500,500)
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
entry = ttk.Entry(root, width=40)
entry.grid(column=1,row=1)
button = ttk.Button(frm, text="Download video", command=download).grid(column=1, row=0)

text = Text(root, width=40, height=10)

root.mainloop()