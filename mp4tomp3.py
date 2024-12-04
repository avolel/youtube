from moviepy.editor import *
import sys, getopt
import argparse
import os

def Main(argv):
    try:
        argParser = argparse.ArgumentParser()
        argParser.add_argument("-f","--FILE", type=str, help="MP4 filepath")
        argParser.parse_args()
        opts, args = getopt.getopt(argv,"f:")
        for opt, arg in opts:
            if(opt == '-f'):
                print("Converting Video to MP3.")       
                ConvertMP4toMP3(arg)
                print("Video Converted to MP3 successfully.")
    except Exception as e:
        type, value, traceback = sys.exc_info()
        print('An Exception occurred:', value.strerror)
        sys.exit(2)
    
def ConvertMP4toMP3(file):    
    mp3file = file.replace(".mp4",".mp3")
    video = VideoFileClip(f'videos\\{file}')
    video.audio.write_audiofile(f'{os.getcwd()}\\mp3\\{mp3file}')

if(__name__ == "__main__"):
    Main(sys.argv[1:])