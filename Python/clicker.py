import tkinter as tk
from tkinter import *
import subprocess
import sys
import random
import json
import os

game_window = tk.Tk()
screen_width = game_window.winfo_screenwidth()
screen_height = game_window.winfo_screenheight()
game_window.geometry(f"{screen_width}x{screen_height}")
game_window.title("The Chong Games Compedium - The Chong Clicker")
gm_icon = PhotoImage(file='Python/CHONG/Screenshot 2025-09-01 123022.gif')
gm_icon = gm_icon.subsample(2,2)
game_window.iconphoto(True, gm_icon)
game_window.config(background="#EB887F")

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    username = "Guest"



game_window.mainloop()