from PIL import Image
from io import BytesIO
import requests
import yt_dlp
from customtkinter import CTkImage as cti
import sys

def get_video_info(url):
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        
        video_info = {
            "title": info.get("title", ""),
            "channel": info.get("channel", ""),
            "uploader": info.get("uploader", ""),
            "duration": info.get("duration", 0),
            "fps": info.get("fps", 0),
            "resolution": info.get("resolution", ""),
            "views": info.get("view_count", 0),
        }
        keys = list(video_info.keys())
        values = list(video_info.values())
        return keys,values

def get_thumbnail(url):
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        thumbnail_url = info.get('thumbnail')
        if thumbnail_url:
            response = requests.get(thumbnail_url)
            if response.status_code == 200:
                image = Image.open(BytesIO(response.content))
                print(image.width,image.height)
                image = cti(image,size=(image.width//4,image.height//4))
                return image
            else:
                return "Failed to download thumbnail"
        else:
            return None
        
def get_video_name(url):
    ydl_opts = {
            'quiet': True,  # Suppress output
            'skip_download': True,  # Do not download the video
        }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        video_title = info_dict.get('title', None)
        
    return video_title
def download_video(url, resolution, player, output_path):
    try:
            nam = get_video_name(url)
            ext = player
            name = f"{nam}.{ext}"
            path = f"{output_path}/{name}"
            ydl_opts = {
                'outtmpl':path if path else name,
                'format': f'best[height<={resolution}]'
            }
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                from tkinter import messagebox as msg 
                msg.showinfo("Done","Video Downloaded Successfully!")
            except Exception:
                from tkinter import messagebox as msg
                msg.showerror("Error","Error in Downloading.")            
            finally:
                sys.stdout = sys.__stdout__
                sys.stderr = sys.__stderr__
    except Exception as e:
            print(e)