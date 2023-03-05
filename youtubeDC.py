from pytube import YouTube
from moviepy.editor import *
import sys, getopt
import argparse
import os

def Main(argv):
    try:
        argParser = argparse.ArgumentParser()
        argParser.add_argument("-u","--URL", type=str, help="Youtube Video URL")
        argParser.add_argument("-l","--MP3LOCATION", type=str, help="Location to save MP3")
        argParser.parse_args()
        opts, args = getopt.getopt(argv,"u:l:")
    except getopt.GetoptError:
        print('youtubeDC.py [-h]')
        sys.exit(2)       
    for opt, arg in opts:
        if(opt == '-u'):            
            Download(arg)
            if(len(opts) == 1):
                ConvertMP4toMP3(f'{os.getcwd()}\\mp3')
        elif(opt == '-l'):
            ConvertMP4toMP3(arg)

def Download(link):
    youTubeobj = YouTube(link)
    youTubeobj = youTubeobj.streams.get_highest_resolution()
    try:
        youTubeobj.download(f'{os.getcwd()}\\videos\\')
    except:
        print("Opps! Something went wrong. Cannot download Youtube Video...")

def ConvertMP4toMP3(mp3location):
     viddir_list = os.listdir(f'{os.getcwd()}\\videos\\')     
     for file in viddir_list:
         mp3file = file.replace(".mp4",".mp3")
         if(os.path.exists(f'{mp3location}\\{mp3file}') == False):
             video = VideoFileClip(f'{os.getcwd()}\\videos\\{file}')
             video.audio.write_audiofile(f'{mp3location}\\{mp3file}')
if(__name__ == "__main__"):
    Main(sys.argv[1:])