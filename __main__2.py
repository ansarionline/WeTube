import customtkinter as tk
from __widgets__ import addEntry, addScrolledFrame, addFrame,addCombobox,addCheckbtn
from __funcs__ import get_video_info as gvi,get_thumbnail as gtb,download_video as std
from yt_dlp import DownloadError as derr

pad = 10
bg = "gray25"
fg = bg
bd = 2
bd_clr = "red"
hover_red = "#8B0A1A"
light_red = "#FFC5C5"
entry_clr = "gray50"

class App:
    def __init__(self, root):
        self.root = root
        self.main_f = addFrame(self.root,padx=50,pady=50,border_w=0,width=1280-500)
        self.addWidgets()
        self.bottom_frame()
        tk.CTkButton(self.main_f,text="Download",text_color="white",
                     bg_color=bg,fg_color=bd_clr,font=("Helvetica",20,"bold"),hover_color=light_red,
                     height=10,command=self.dnd,
                     border_width=bd,border_color=bd_clr).pack(side="top",fill="x",
                                                               padx=50,pady=1)
        self.pbar = tk.CTkProgressBar(self.main_f,corner_radius=5,bg_color="black",
                                      fg_color="black",border_color="black",border_width=2,
                                      height=15,mode="determinate",orientation="horizontal",
                                      progress_color="red")
    def pack_bar(self):
        self.pbar.pack(side="bottom",fill="x",padx=50,pady=5)
        return

    def dnd(self):
        self.pack_bar()
        self.pbar.set(0)
        self.pbar.start()
        self.root.after(500, self.do_std)  # 500ms = 0.5s

    def do_std(self):
        std(self.e_url.get().strip(),
                    self.res.get(),
                    self.cdc.get(),
                    self.pth.get())
        self.pbar.stop()
        self.pbar.pack_forget()

    def addWidgets(self):
        self.e = addFrame(self.main_f,padx=30,pady=1,bg="red",fill="x",border_w=bd)
        self.e_l = tk.CTkLabel(self.e,text="URL",text_color="white",bg_color="gray50",
                             fg_color="red",corner_radius=5,font=("helvetica",18)
                             )
        self.e_l.pack(fill="x",side="left")
        self.e_url = addEntry(self.e,padx=1,pady=1,side="left")
        self.e_url.insert(0, "Paste the URL here and Press Enter ...")
        self.e_url.bind("<Return>",lambda e: self.vidInfo())
        self.response_f = self.r_f = addScrolledFrame(self.main_f,padx=0,pady=0,height=9,fill="x")
        self.btm_f = addFrame(self.main_f,fill="x",padx=50,pady=1,bg="gray50")
    
    def vidInfo(self):
        self.info_Text = tk.CTkTextbox(self.response_f,font=("Helvetica",20),width=(1280//2)+16,
                                       height=10,wrap=tk.WORD,
                                       text_color="black",state="normal")
        self.l = tk.CTkLabel(self.response_f,text="",corner_radius=2)
        self.l.pack(side="left",fill="both",padx=1,pady=1)
        self.info_Text.pack(side="right",fill="both",padx=1,pady=1)
        if self.e_url.get() != "" or self.e_url.get() != "Paste the URL here and Press Enter ...":
          try:
            keys,values = gvi(self.e_url.get().strip())
            image = gtb(self.e_url.get().strip())
            self.l.configure(image=image)
            self.info_Text.delete(1.0,tk.END)
            for i in range(0,len(keys)):
                self.info_Text.insert(tk.END,f"{keys[i].capitalize()}: {values[i]}\n")
          except derr:
              self.info_Text.delete(1.0,tk.END)
              self.info_Text.insert(tk.END,"Invalid URL.")
        self.info_Text.configure(state="disabled")
    
    def bottom_frame(self):
        vid = [
        "mp4",  # Video Format
        "webm", # Video Format
        "flv",  # Video Format
        "avi",  # Video Format
        "m4v",  # Video Format
        "3gp",  # Video Format
        "mkv",  # Video Format
        "mov",  # Video Format
        "wmv",  # Video Format
        ]
        aud = [
        "mp3",  # Audio Format
        "m4a",  # Audio Format
        "wav",  # Audio Format
        "ogg",  # Audio Format
        "aac",  # Audio Format
        "flac", # Audio Format
        "opus"  # Audio Format
        ]
        def on_toggle(e=None):
            print(var.get())
            if var.get():
                self.var.configure(text = "Audio")
                self.res.configure(state="disabled")
                self.cdc.configure(values=aud)
            else:
                self.var.configure(text =  "Video")
                self.res.configure(state="normal")
                self.cdc.configure(values=vid)
                
        r = self.btm_f
        self.res = addCombobox(r,padx=5,pady=5,values = ["144","240","360",
                                                        "480","576","720",
                                                         "1080","1440","1536",
                                                         "2160","4320","8640"])
        self.res.set("480")
        self.cdc = addCombobox(r,padx=5,pady=5,values=vid)
        var = tk.BooleanVar()
        self.var = addCheckbtn(r,text="Audio",padx=5,pady=5,var=var,cmd=on_toggle)
        self.pth = addEntry(r,side="left",padx=5,pady=5)
        self.pth.insert(tk.END,"Output Path")
        self.pth.bind("<Button-1>",lambda e: self.browse_path())
    
    def browse_path(self):
        from customtkinter import filedialog as fdg 
        a = fdg.askdirectory()
        if a:
            self.pth.delete(0,tk.END)
            self.pth.insert(tk.END,f"{a}")
            self.path = a

root = tk.CTk(fg_color="black")
try:
    root.iconbitmap("icon.ico")
except FileNotFoundError:
    pass
root.geometry("780x480")
root.title("WeTube ©2024")
App(root)
root.resizable(False,False)
root.mainloop()