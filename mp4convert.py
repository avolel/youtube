from moviepy.editor import *
import os

directory = os.fsencode(f'{os.getcwd()}\\videos')
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    mp3file = filename.replace(".mp4",".mp3")
    video = VideoFileClip(f'videos\\{filename}')
    video.audio.write_audiofile(f'{os.getcwd()}\\mp3\\{mp3file}')