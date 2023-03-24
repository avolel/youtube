from pytube import YouTube
from moviepy.editor import *
import sys, getopt
import argparse
import os

viddir_list = []

def Main(argv):
    global viddir_list
    try:
        argParser = argparse.ArgumentParser()
        argParser.add_argument("-u","--URL", type=str, help="Youtube Video URL")
        argParser.add_argument("-l","--LOCATION", type=str, help="Video Location")
        argParser.parse_args()
        opts, args = getopt.getopt(argv,"u:l:")
        for opt, arg in opts:
            if(opt == '-u'):            
                Download(arg)
            elif(opt == '-l'):
                viddir_list = os.listdir(f'{arg}\\')
                loopContinue = True
                while loopContinue:
                    VideoMenu()
                    choice = input(f"Which video would you like to convert to an MP3 [0 - {len(viddir_list) - 1}]: ")
                    if choice.isnumeric():
                        if int(choice) >= 0 and int(choice) <= len(viddir_list) - 1:
                            ConvertMP4toMP3(viddir_list[int(choice)], f'{arg}\\')
                            loopContinue = False
                        else:
                            print("Invalid Option. Try Again.")
                    else:
                        print("Invalid Option. Try Again.")
    except getopt.GetoptError:
        print('youtubedownload.py [-h]')
        sys.exit(2)

def Download(link):
    youTubeobj = YouTube(link)
    youTubeobj = youTubeobj.streams.get_highest_resolution()
    try:
        youTubeobj.download(f'{os.getcwd()}\\videos\\')
        print(f"{link} Download Completed Successfully.")
    except:
        print("Opps! Something went wrong. Cannot download Youtube Video...")

def ConvertMP4toMP3(file, dir):
    mp3file = file.replace(".mp4",".mp3")
    if(os.path.exists(f'{os.getcwd()}\\mp3\\{mp3file}') == False):
        video = VideoFileClip(f'{dir}\\{file}')
        video.audio.write_audiofile(f'{os.getcwd()}\\mp3\\{mp3file}')

def VideoMenu():
    global viddir_list
    index = 0    
    print(30 * "-", "Choose a Video", 30 * "-")
    for file in viddir_list:
        print(f"{index}. {file}\n")
        index+=1
    print(67 * "-")


if(__name__ == "__main__"):
    Main(sys.argv[1:])