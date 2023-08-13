from pytube import YouTube
from moviepy.editor import *
import sys, getopt
import argparse
import os

viddir_list = []

def Main(argv):
    try:
        argParser = argparse.ArgumentParser()
        argParser.add_argument("-u","--URL", type=str, help="Youtube Video URL")
        argParser.parse_args()
        opts, args = getopt.getopt(argv,"u:")

        for opt, arg in opts:
            if(opt == '-u'):
                print(f'Downloading {arg}.')        
                fileName = Download(arg)
                print("Download Completed Successfully.")
                print("Converting Video to MP3.")                                  
                ConvertMP4toMP3(fileName)
                print("Video Converted to MP3 successfully.")
    except Exception as e:
        print('An Exception occurred:', e)
        sys.exit(2)

def Download(link):        
        youTubeobj = YouTube(link, use_oauth=True, allow_oauth_cache=True)
        file_name = youTubeobj.streams[0].default_filename
        youTubeobj = youTubeobj.streams.get_highest_resolution()
        youTubeobj.download(f'{os.getcwd()}\\videos\\')        
        return file_name.replace(".3gpp",".mp4")

def ConvertMP4toMP3(file):    
    mp3file = file.replace(".mp4",".mp3")
    if(os.path.exists(f'{os.getcwd()}\\mp3\\{mp3file}') == False):
        video = VideoFileClip(f'videos\\{file}')
        video.audio.write_audiofile(f'{os.getcwd()}\\mp3\\{mp3file}')

if(__name__ == "__main__"):
    Main(sys.argv[1:])