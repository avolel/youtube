#from pytube import YouTube
from pytubefix import YouTube
from pytubefix.cli import on_progress
import sys, getopt
import argparse
import os
import traceback

def Main(argv):
    try:
        argParser = argparse.ArgumentParser()
        argParser.add_argument("-u","--URL", type=str, help="Youtube Video URL")
        argParser.parse_args()
        opts, args = getopt.getopt(argv,"u:")

        for opt, arg in opts:
            if(opt == '-u'):
                print(f'Downloading {arg}.')        
                Download(arg)
                print("Download Completed Successfully.")               
    except Exception as e:  
        traceback.print_exc()
        sys.exit(2)

def Download(link):        
    youTubeobj = YouTube(link, use_oauth=True, allow_oauth_cache=True, on_progress_callback = on_progress)
    #test
    #youTubeobj = youTubeobj.streams.get_highest_resolution()
    #youTubeobj = YouTube(link)
    #youTubeobj.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(f'{os.getcwd()}\\videos\\')
    youTubeobj.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(f'{os.getcwd()}\\videos\\')
    #youTubeobj.download(f'{os.getcwd()}\\videos\\')

if(__name__ == "__main__"):
    Main(sys.argv[1:])