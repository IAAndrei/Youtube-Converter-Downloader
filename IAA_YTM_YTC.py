from __future__ import unicode_literals
import youtube_dl

print("IAAndrei's YoutubeDL Downloader")
print("To run this you must have YoutubeDL.py installed\n(i did mine via pip install and")
print(" FFMPEG installed either on PATH or python directory")

inkl = input("Paste your youtube URL(right click): ")

test = input("Input 1 for MP4/WEBM | Input 2 for MP3(FFMPEG CONVERT)")
if test == "1":
    ydl_opts = {}
if test == "2":
    ydl_opts = {
        'format': 'bestaudio',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }


with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([inkl])
        
test = input("Input anything to exit")
