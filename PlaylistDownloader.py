import yt_dlp
import os
import sys

def download_playlist(playlist_url):
    try:
        current_directory = os.path.dirname(os.path.realpath(__file__))
        parent_directory = os.path.dirname(current_directory)
        download_folder = os.path.join(parent_directory, 'downloaded_mp3s')

        if not os.path.exists(download_folder):
            os.makedirs(download_folder)

        ydl_opts = {
            'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'noplaylist': False,
            'ignoreerrors': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])

        print("Download completed successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    if getattr(sys, 'frozen', False):
        # For PyInstaller executable
        if len(sys.argv) > 1:
            download_playlist(sys.argv[1])
        else:
            print("Please provide playlist URL as an argument")
            input("Press Enter to exit...")
    else:
        # For normal Python execution
        playlist_url = input("Enter YouTube playlist URL: ")
        download_playlist(playlist_url)