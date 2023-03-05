from pytube import YouTube
import sys, getopt

def Main(argv):
    try:
        opts, args = getopt.getopt(argv,"hu:")
    except getopt.GetoptError:
        print('youtube-download.py -u <url>')
        sys.exit(2)
    for opt, arg in opts:
        if(opt == '-h'):
            print('youtube-download.py -u <url>')
            sys.exit()
        elif(opt == '-u'):
            Download(arg)

def Download(link):
    youTubeobj = YouTube(link)
    youTubeobj = youTubeobj.streams.get_highest_resolution()
    try:
        youTubeobj.download()
    except:
        print("Opps! Something went wrong. Cannot download Youtube Video...")

if(__name__ == "__main__"):
    Main(sys.argv[1:])