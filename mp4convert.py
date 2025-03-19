from moviepy.editor import *
import os

directory = os.path.join(os.getcwd(), 'vids')
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if not filename.endswith('.mp4'):
        print(f"Skipping non-MP4 file: {filename}")
        continue
    
    mp3file = filename.replace(".mp4", ".mp3")
    video_path = os.path.join(directory, filename)
    audio_path = os.path.join(os.getcwd(), 'mp3', mp3file)
    
    try:
        with VideoFileClip(video_path) as video:
            video.audio.write_audiofile(audio_path)
    except Exception as e:
        print(f"Error processing file: {filename} - {str(e)}")
    
    # Remove original file (but be careful not to delete the wrong file!)
    os.remove(video_path)