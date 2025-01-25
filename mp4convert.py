from moviepy.editor import *
import os

directory = os.fsencode(f'{os.getcwd()}\\vids')
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    mp3file = filename.replace(".mp4",".mp3")
    video = VideoFileClip(f'vids\\{filename}')
    video.audio.write_audiofile(f'{os.getcwd()}\\mp3\\{mp3file}')
    video.close()
    os.remove(f'{os.getcwd()}\\vids\\{filename}')