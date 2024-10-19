"""
<h1>Widgets</h1>
Provide themed Widgets for Downloader GUI.
"""
import customtkinter as ctk
        
pad = 10
bgdark = "gray25"
bglight = "white"
bgfdark = "black"
bd = 2
entry_d = "gray50"
entry_l = "white"
RED = "red"
DARK_RED = "#8B0A1A"
LIGHT_RED = "#FFC5C5"

def addEntry(master,theme="dark",side="top",fill="x",expand=True,padx=pad,pady=pad):
    theme = theme.lower().strip()
    entry = ctk.CTkEntry(master,font=("Helvetica",20),justify="center")
    if theme == "dark":
        entry.configure(
            bg_color=bgdark,
            fg_color=entry_d,
            text_color="white",
            )
        entry.bind("<Leave>",lambda e: entry.configure(True,fg_color=entry_d,text_color="white"))
    if theme == "light":
        entry.configure(
            bg_color=bglight,
            fg_color=entry_l,
            text_color="black",
            )
        entry.bind("<Leave>",lambda e: entry.configure(True,fg_color=entry_l,text_color="white"))
    entry.bind("<Enter>",lambda e: entry.configure(True,fg_color=LIGHT_RED,text_color=DARK_RED))
    entry.pack(side=side,fill=fill,expand=expand,padx=padx,pady=pady)
    return entry

def addScrolledFrame(master,theme="dark",side=None,fill="both",height=200,
                     expand=True,padx=100,pady=100,border_w = bd):
        f_l = ctk.CTkScrollableFrame(master,width=300,scrollbar_button_color=RED,border_color=RED,
                                         scrollbar_button_hover_color=DARK_RED,border_width=border_w,
                                         height=height)
        if theme == "dark":
            f_l.configure(bg_color=bgdark,fg_color=bgdark,scrollbar_fg_color=bgdark)
        if theme == "light":
            f_l.configure(bg_color=bglight,fg_color=bglight,scrollbar_fg_color=bglight)
        f_l.pack(side=side,fill=fill,expand=expand,padx=padx,pady=pady)
        return f_l

def addFrame(master,theme="dark",side=None,fill="both",width=300,height=50,
                     expand=True,padx=100,pady=100,border_w = bd,bg=bgfdark):
        f_l = ctk.CTkFrame(master,width=width,border_color=RED,border_width=border_w,height=height)
        if theme == "dark":
            f_l.configure(bg_color=bgdark,fg_color=bgfdark)
        if theme == "light":
            f_l.configure(bg_color=bglight,fg_color=bglight)
        f_l.pack(side=side,fill=fill,expand=expand,padx=padx,pady=pady)
        return f_l

def addCombobox(master,theme="dark",side="left",fill="both",expand=True,padx=1,pady=1,width=80,values=[0,1,2,3]):
        cb = ctk.CTkComboBox(master,dropdown_hover_color=LIGHT_RED,width=width,
                    dropdown_text_color="black",dropdown_fg_color=LIGHT_RED,values=values)
        if theme == "dark":
            cb.configure(bg_color=bgdark,fg_color=bgdark,text_color="white")
        if theme == "light":
            cb.configure(bg_color=bglight,fg_color=bglight,text_color=DARK_RED)
        cb.pack(side=side,fill=fill,expand=expand,padx=padx,pady=pady)
        return cb
    
def addCheckbtn(master,theme="dark",side="left",fill="both",expand=True,padx=1,pady=1,text="",width=48,
                var=None,cmd=None):
        cb = ctk.CTkCheckBox(master,text_color="white",border_width=bd,
                             checkmark_color=DARK_RED,text=text,
                             width=width,border_color=DARK_RED,
                             font=("Helvetica",15,"bold"),command=cmd,
                             variable=var)
        if theme == "dark":
            cb.configure(bg_color=bgfdark,fg_color=bgfdark)
        if theme == "light":
            cb.configure(bg_color=bglight,fg_color=bglight)
        cb.pack(side=side,fill=fill,expand=expand,padx=padx,pady=pady)
        return cb