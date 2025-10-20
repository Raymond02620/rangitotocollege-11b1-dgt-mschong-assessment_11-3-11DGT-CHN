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
detention_slip_image = PhotoImage(file='Python/CHONG/detention.gif')
detention_slip_image = detention_slip_image.subsample(2,2)

Chong_phrases = [
    "The grey hair has multiplied."
    "Get on with your work."
    "BREAK"
    "ONE PERSON"
    "Heeennnryyyy"
    "Don't talk about other teachers, I get jealous."
    "Fresh, hot detention slips!"
    "are you free this friday?"
    "ONE HOUR"
    "Start saving for my retirement funds/"
    "Chong has retired."
    "You look like you need detention."
    "STOP HAVING FUN IN MY LESSON"
    "Welcome to the Chong comedy show"
    "All I know is that N0 is quick to mark."
    "*menacing glare of the Chong*"
    "See? He only acts upon python commands."
    "Here - One box of tissues, except only the box."
    "*covers face in distress*"
]

if not os.path.exists('Python/saves'): # Create saves directory if it doesn't exist
    os.makedirs('Python/saves') # Create the directory

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    username = "Guest"

def relx(x): return x / 1920 # Assuming a base width of 1920 pixels
def rely(y): return y / 1080 # Assuming a base height of 1080 pixels

title_label = Label(game_window, 
                    text="The Chong Clicker", 
                    font=("MS Serif", 70), 
                    bg="#EB887F",
                    fg="black",
                    padx=20,
                    pady=20,
                    relief="raised",
                    image = detention_slip_image,
                    compound="bottom")
title_label.place(relx = 0.5, rely = 0.1, anchor = CENTER)

username_label = Label(game_window, 
                       text=f"Player: {username}", 
                       font=("MS Serif", 40), 
                       bg="#EB887F")
username_label.place(relx = 0.9, rely = 0.96, anchor = CENTER)

def exit_game():
    game_window.destroy()
    subprocess.Popen(["python3", "Python/gameselection.py", username])




exit_button = Button(game_window, 
                     text="Exit Game", 
                     font=("MS Serif", 20), 
                     height = 3, 
                     width = 10, 
                     command= lambda: exit_game())
exit_button.place(relx = 0.1, rely = 0.9, anchor = CENTER)

def change_exit_button_text(new_text): # Change the text of the exit button
    if username != "Guest":
        exit_button.config(text=new_text)
    else:
        exit_button.config(text="Exit")

def change_exit_function(new_function):
    exit_button.config(command=new_function)
 
play_button = Button(game_window, text="Play", font=("MS Serif", 30), height = 2,width = 15, activebackground= "#EA544C", activeforeground="#7582E8", padx=10, pady=10, command = lambda: [enter_game_page(), change_exit_button_text("Return to Menu"), change_exit_function(lambda:[return_to_menu()])])
play_button.place(relx = 0.5, rely = 0.7, anchor = CENTER)

num_ds = 0

#GAME LABELS/MAIN FUNCTIONS

detention_label = Label(game_window, text=f"Detention Slips: {num_ds}", font=("MS Serif", 40), bg="#EB887F", fg="black", relief="raised", padx=20, pady=20)
clicker = Button(game_window, text = "CHONG", )

def enter_game_page():
    play_button.place_forget()
    title_label.place_forget()
    detention_label.place(relx = 0.5, rely = 0.2, anchor = CENTER)


def return_to_menu():
    detention_label.place_forget()
    change_exit_button_text("Exit Game")
    change_exit_function(lambda: exit_game())
    title_label.place(relx = 0.5, rely = 0.1, anchor = CENTER)
    play_button.place(relx = 0.5, rely = 0.7, anchor = CENTER)
                     
                     

game_window.mainloop()