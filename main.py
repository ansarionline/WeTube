try:
    import tkinter as tk
    from tkinter import ttk
    from tkinter import filedialog
    from tkinter.scrolledtext import ScrolledText
    import threading
    import sys
    import yt_dlp

    class RedirectText:
        def __init__(self, text_widget):
            self.output = text_widget

        def write(self, string):
            self.output.insert(tk.END, string)
            self.output.see(tk.END)

        def flush(self):
            pass

    def browse_output_path():
        path = filedialog.askdirectory()
        if path:
            output_entry.delete(0, tk.END)
            output_entry.insert(0, path)

    def get_video_name(url):
        ydl_opts = {
            'quiet': True,  # Suppress output
            'skip_download': True,  # Do not download the video
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            video_title = info_dict.get('title', None)
        
        return video_title

    def download_video(url, resolution, player, output_path, text_widget):
        try:
            nam = get_video_name(url)
            ext = player
            name = f"{nam}.{ext}"
            path = f"{output_path}/{name}"
            ydl_opts = {
                    'outtmpl': path if path else name,
                    'format': f'best[height<={resolution}]'
                }
            sys.stdout = RedirectText(text_widget)
            sys.stderr = RedirectText(text_widget)
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
            except Exception as e:
                text_widget.insert("end",f"Error: {e}")
            finally:
                sys.stdout = sys.__stdout__
                sys.stderr = sys.__stderr__
        except Exception as e:
            text_widget.insert("end",f"Error; {e}")

    def start_download():
        url = url_entry.get()
        resolution = resolution_combobox.get()
        player = player_combobox.get()
        output_path = output_entry.get()
        threading.Thread(target=download_video, args=(url, resolution, player, output_path, text_widget)).start()

    root = tk.Tk()
    root.title("YouTube Downloader")
    root.minsize(600,600)
    try:
        root.iconbitmap('icon.ico')
    except Exception:
        pass
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TButton', font=('Helvetica', 15), foreground='white', background='red', borderwidth=0)
    style.map('TButton', background=[('active', 'dark red')])
    font=('Helvetica', 20)
    fg='black'

    frame = ttk.Frame(root)
    frame.pack(fill="both",expand=True,padx=10,pady=10)

    url_label = ttk.Label(frame, text="YouTube URL:",font=font,foreground=fg)
    url_label.pack(anchor='w', padx=20,pady=5)
    url_entry = ttk.Entry(frame, width=40, font=font,foreground=fg)
    url_entry.pack(fill='x', padx=20,pady=5)

    resolution_label = ttk.Label(frame, text="Resolution:",font=font,foreground=fg)
    resolution_label.pack(anchor='w', padx=20,pady=5)
    resolution_combobox = ttk.Combobox(frame, values=["720p", "1080p", "1440p", "2160p"],font=font,foreground=fg)
    resolution_combobox.pack(fill='x', padx=20,pady=5)
    resolution_combobox.current(0)  

    player_frame = ttk.Frame(frame,style="TFrame")
    player_label = ttk.Label(frame, text="Player:",font=font,foreground=fg)
    player_label.pack(anchor='w', padx=20,pady=5)
    player_combobox = ttk.Combobox(frame, values=["mp4"],font=font,foreground=fg)
    player_combobox.pack(fill='x', padx=20,pady=5)
    player_combobox.current(0)  

    output_frame = ttk.Frame(frame,style="TFrame")
    output_label = ttk.Label(frame, text="Output Path:",font=font,foreground=fg)
    output_label.pack(anchor='w', padx=20,pady=5)
    output_entry = ttk.Entry(output_frame, width=30,font=font,foreground=fg)
    output_entry.pack(fill='x',expand=True, padx=0,pady=5,side='left')

    browse_button = ttk.Button(output_frame, text="Browse", command=browse_output_path, style='TButton')
    browse_button.pack(padx=5,pady=5,side='right')
    output_frame.pack(padx=20,pady=5,fill='x')

    download_button = ttk.Button(frame, text="Download", style='TButton', command=start_download)
    download_button.pack(padx=20,pady=20,fill='x')

    text_widget = ScrolledText(frame, wrap=tk.WORD, width=80, height=20, 
                            font=("calibri",11,"italic"),fg="blue",bd=2,
                            relief="solid",bg="lightyellow")
    text_widget.insert("end","**CONSOLE**\n")
    text_widget.pack(pady=10,padx=20,fill='both')

    root.mainloop()
except Exception as e:
    print(e)