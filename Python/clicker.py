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
    "The grey hair has multiplied.",
    "Get on with your work.",
    "I'm retiring today",
    "BREAK",
    "ONE PERSON",
    "Heeennnryyyy",
    "Don't talk about other teachers, I get jealous.",
    "Fresh, hot detention slips!",
    "are you free this friday?",
    "ONE HOUR",
    "Start saving for my retirement funds",
    "Chong has retired.",
    "You look like you need detention.",
    "STOP HAVING FUN IN MY LESSON",
    "Welcome to the Chong comedy show",
    "All I know is that N0 is quick to mark.",
    "*menacing glare of the Chong*",
    "See? He only acts upon python commands.",
    "Here - One box of tissues, except only the box.",
    "*covers face in distress*",
    "WHAT?!?!?",
    "OI",
    "WORK",
    "HENRYYYYYY! NOOOO",
    "How many times do I have to help you with the image?",
    "This table is very Henry-Proof",
    "We should thank Henry for stabalising the table",
    "I deserve a medal",
    "I JUST TAUGHT HIM A NEW WORD",
    "Skills issue",
    "DO YOU GUYS HAVE FUN IN OTHER LESSONS AS WELL?!",
    "Why would I give you well done when you do what is expected from you?",
    "See you at Pak'n'save",
    "One term, one toilet pass",
    "Say I came from M block if Mr Gale catches you",
    "AHAhahHAhAHAHahAHAH",
    "EhehEhEHeHE",
    "I want to retire early",
    
]

if not os.path.exists('Python/click'): # Create saves directory if it doesn't exist
    os.makedirs('Python/click') # Create the directory

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

#some json work
def save_data():
    global minimum_level, slips_per_click, num_ds, slips_for_level_up
    if username != "Guest":
        data = { "level" : minimum_level, "slips_per_click" : slips_per_click, "slip_amount" : num_ds, "slips_for_level_up" : slips_for_level_up }
        filepath = f"Python/click/{username}_calculator_save.json"
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)

def load_data():
    global minimum_level, slips_per_click, num_ds, slips_for_level_up

    if username != "Guest":
        filepath = f"Python/click/{username}_calculator_save.json"
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r') as f:
                    data = json.load(f)
                #load from json, current variable as default.
                minimum_level = data.get("level", minimum_level)
                slips_per_click = data.get("slips_per_click", slips_per_click)
                num_ds = data.get("slip_amount", num_ds)
                slips_for_level_up = data.get("slips_for_level_up", slips_for_level_up)

                #update labels to get values right
                detention_label.config(text=f"Detention Slips: {num_ds}")
                target_label.config(text=f"{slips_for_level_up} detention slips needed to level up, level {minimum_level} / {maximum_level}, current slip gain per click: {slips_per_click}")
            except (json.JSONDecodeError, KeyError, IOError,) as e:
                return 0


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
slips_per_click = 1
slips_for_level_up = 100
increment_per_level_up = 1500
minimum_level = 1
maximum_level = 999

#GAME LABELS/MAIN FUNCTIONS

detention_label = Label(game_window, text=f"Detention Slips: {num_ds}", font=("MS Serif", 40), bg="#EB887F", fg="black", relief="raised", padx=20, pady=20)
clicker = Button(game_window, text = "CHONG", font = ("MS Serif", 40), bg="#EB887F", fg="black", relief="raised", padx=20, pady=20, command = lambda: [add_slip(), display_chong()])
message_label = Label(game_window, text = "CHONG", font = ("MS Serif", 20), bg ="#EB887F", fg="black", relief="raised", padx=20, pady=20,)
level_up_button = Button(game_window, text = "Level up", font = ("MS Serif", 30), bg ="#EB887F", fg="black",  padx=20, pady=20, command = lambda: level_up_check() ) 
target_label = Label(game_window, text = f"{slips_for_level_up} detention slips needed to level up, level {minimum_level} / {maximum_level}, current slip gain per click: {slips_per_click}",font = ("MS Serif", 30), bg ="#EB887F", fg="black",  padx=20, pady=20, )
feedback_label = Label(game_window, text = "", font = ("MS Serif", 30), bg ="#EB887F", fg="black", padx=20, pady=20,)

feedback_timer_id = None

def clear_feedback_label():
    global feedback_timer_id
    feedback_label.config(text = "")
    feedback_timer_id = None

def level_up_check():
    global num_ds, slips_per_click, slips_for_level_up, minimum_level, feedback_timer_id

    if feedback_timer_id:
        game_window.after_cancel(feedback_timer_id) #if timer exists, exterminate it.

    if num_ds >= slips_for_level_up: #success modelling
        num_ds -= slips_for_level_up
        minimum_level += 1
        slips_per_click += 1
        slips_for_level_up += increment_per_level_up # increase the cost

        detention_label.config(text=f"Detention Slips: {num_ds}")
        target_label.config(text=f"{slips_for_level_up} detention slips needed to level up, level {minimum_level} / {maximum_level}, current slip gain per click: {slips_per_click}")
        feedback_label.config(text="Level Up Successful!")
        feedback_timer_id = game_window.after(4000, clear_feedback_label)
    else:
        feedback_label.config(text="Not enough detention slips!")
        feedback_timer_id = game_window.after(4000, clear_feedback_label)


    

def display_chong():
    random_phrase = random.choice(Chong_phrases)
    message_label.config(text=random_phrase)
   
    
def add_slip():
    global num_ds
    num_ds += slips_per_click
    detention_label.config(text=f"Detention Slips: {num_ds}")

    
def enter_game_page():
    play_button.place_forget()
    title_label.place_forget()
    message_label.config(text="CHONG")
    detention_label.place(relx = 0.5, rely = 0.2, anchor = CENTER)
    clicker.place(relx = 0.5, rely = 0.4, anchor = CENTER)
    message_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    level_up_button.place(relx = 0.5, rely = 0.6, anchor = CENTER)
    target_label.place(relx = 0.5, rely = 0.7, anchor = CENTER)
    feedback_label.place(relx = 0.5, rely = 0.8, anchor = CENTER)

def return_to_menu():
    save_data()
    detention_label.place_forget()
    message_label.place_forget()
    clicker.place_forget()
    level_up_button.place_forget()
    feedback_label.place_forget()
    target_label.place_forget()

    change_exit_button_text("Exit Game")
    change_exit_function(lambda: exit_game())
    title_label.place(relx = 0.5, rely = 0.1, anchor = CENTER)
    play_button.place(relx = 0.5, rely = 0.7, anchor = CENTER)
                     
                     
load_data()
game_window.mainloop()