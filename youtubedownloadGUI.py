import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube

def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return
    
    try:
        yt = YouTube(url)
    except Exception as e:
        messagebox.showerror("Error", f"Invalid URL: {e}")
        return

    file_path = filedialog.askdirectory()
    if not file_path:
        messagebox.showerror("Error", "Please select a directory to download the video")
        return
    
    try:
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=file_path)
        messagebox.showinfo("Success", f"Video downloaded successfully in {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Download failed: {e}")

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# URL Entry
url_label = tk.Label(root, text="YouTube URL:")
url_label.pack(pady=5)

url_entry = tk.Entry(root, width=70)
url_entry.pack(pady=5)

# File Path Selection
file_path_button = tk.Button(root, text="Choose Download Location", command=lambda: filedialog.askdirectory())
file_path_button.pack(pady=10)

# Download Button
download_button = tk.Button(root, text="Download Video", command=download_video)
download_button.pack(pady=20)

# Run the application
root.mainloop()