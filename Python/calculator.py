from tkinter import *
import tkinter as tk
import subprocess
import sys
import random

# Helper functions for dynamic placement
def relx(x): return x / 1920 # Assuming a base width of 1920 pixels
def rely(y): return y / 1080 # Assuming a base height of 1080 pixels

game_window = tk.Tk()

screen_width = game_window.winfo_screenwidth() # Get the screen width
screen_height = game_window.winfo_screenheight() # Get the screen height
game_window.geometry(f"{screen_width}x{screen_height}") # Set the window size to full screen
game_window.title("The Chong Games Compedium - The Quest For The First Calculator") #Sets the title of the window
gm_icon = PhotoImage(file='Python/CHONG/Screenshot 2025-09-01 123022.gif') #Imports an image to use as the icon of the window
gm_icon = gm_icon.subsample(2,2) #Resizes the image to be smaller by that factor
game_window.iconphoto(True, gm_icon) #Sets the icon of the window
game_window.config(background="#EBDB7F") #Sets the background color of the window

if len(sys.argv) > 1:  # Check if a username argument is provided
    username = sys.argv[1] # Get the username from command line arguments
else:
    username = "Guest" # Default to "Guest" if no username is provided


def exit_game():
    game_window.destroy()
    subprocess.Popen(["python3", "Python/gameselection.py", username]) # Return to game selection screen
big_label = Label(game_window, 
                  text="The Quest For The First Calculator",
                  font=("MS Serif", 80),
                  fg ="#000000",
                  relief=RAISED,
                  bg="#EBDB7F",
                  bd = 10,
                  padx = 10,
                  pady = 20,)

big_label.pack()

# Functions to manage menu state
def terminate_menu():
    big_label.pack_forget()
    play_button.place_forget()
    acc_label.place_forget()

def change_exit_button_text(new_text):
    exit_button.config(text=new_text)

def change_exit_button_command(new_command):
    exit_button.config(command=new_command)


def restore_menu():
    big_label.pack()
    play_button.place(relx=relx(760), rely=rely(600))
    acc_label.place(relx=relx(1600), rely=rely(1000))

story_intro = (username + ", welcome to 'The Quest For The First Calculator'! In this adventure, you will crack codes based on logics and arithmetics across a diverse range of topics in mathematics. Get ready for an exciting journey through time and numbers!")
part_1_story = (username.title() + " finds himself in a dimly lit room, the air thick with the scent of old parchment and ink. In front of him lies an ancient scroll, its edges frayed and worn. As he unrolls it, he sees a series of symbols and numbers that seem to dance on the page. Suddenly, a voice echoes in the room, 'To unlock the secrets of the past, you must solve my riddles. Only then will you find the path to the first calculator.'")
stage_1_code = random.randint(1000, 9999)  # Random 4-digit code for stage 1, sorted for clue generation
stage_1_clue = f"for developers: the code is {stage_1_code}"
def show_intro():
    intro_label = Label(game_window, 
                      text=story_intro,
                      font=("MS Serif", 20),
                      fg ="#000000",
                      bg="#EBDB7F",
                      padx=20,
                      pady=20,
                      wraplength=1200,
                      justify="center",
                      )
    intro_label.place(relx=relx(125), rely=rely(400))
    next_button = Button(game_window,
                         text="Next",
                         font=("MS Serif", 20),
                         fg="#000000",
                         bg="#FFFFFF",
                         relief=RAISED,
                         bd=5,
                         padx=10,
                         pady=5,
                         activebackground="#3B10D4",
                         activeforeground="#ED0F0F",
                         command=lambda: [intro_label.place_forget(), next_button.place_forget(), show_part_one()])
    next_button.place(relx=relx(900), rely=rely(900))

def show_part_one():
    part_one_label = Label(game_window, 
                      text=part_1_story,
                      font=("MS Serif", 20),
                      fg ="#000000",
                      bg="#EBDB7F",
                      padx=20,
                      pady=20,
                      wraplength=1200,
                      justify="center",
                      )
    part_one_label.place(relx=relx(120), rely=rely(400))
    next_button = Button(game_window,
                         text="Begin Your Quest",
                         font=("MS Serif", 20),
                         fg="#000000",
                         bg="#FFFFFF",
                         relief=RAISED,
                         bd=5,
                         padx=10,
                         pady=5,
                         activebackground="#3B10D4",
                         activeforeground="#ED0F0F",
                         command=lambda: [part_one_label.place_forget(), next_button.place_forget(), stage_1()])
    next_button.place(relx=relx(800), rely=rely(700))

def stage_1():
    stage_label = Label(game_window, 
                      text="Stage 1: The Ancient Code",
                      font=("MS Serif", 60),
                      fg ="#000000",
                      bg="#EBDB7F",
                      padx=20,
                      pady=20,
                      )
    stage_label.pack()
    clue_label = Label(game_window, 
                      text="Clue: " + stage_1_clue,
                      font=("MS Serif", 20),
                      fg ="#000000",
                      bg="#EBDB7F",
                      padx=20,
                      pady=20,
                      wraplength=1200,
                      justify="center",
                      )
    clue_label.place(relx=relx(500), rely=rely(300))
    indicator_label = Label(game_window, 
                      text="Enter the 4-digit code to proceed:",
                      font=("MS Serif", 15),
                      fg ="#000000",
                      bg="#EBDB7F",
                      padx=20,
                      pady=20,
                      wraplength=1200,
                      justify="center",
                      )
    indicator_label.place(relx=relx(750), rely=rely(550))
    code_entry = Entry(game_window, 
                       font=("MS Serif", 20),
                       fg="#000000",
                       bg="#FFFFFF",
                       bd=5,
                       width=10
                       )
    code_entry.place(relx=relx(800), rely=rely(600))
    submit_button = Button(game_window,
                         text="Submit Code",
                         font=("MS Serif", 20),
                         fg="#000000",
                         bg="#FFFFFF",
                         relief=RAISED,
                         bd=5,
                         padx=10,
                         pady=5,
                         activebackground="#3B10D4",
                         activeforeground="#ED0F0F",
                         command=lambda: check_stage_1_code(code_entry.get()).strip())
    submit_button.place(relx=relx(800), rely=rely(700))

play_button = Button(game_window,
                     text="Start Game",
                     font=("MS Serif", 40),
                     fg="#000000",
                     bg="#FFFFFF",
                     relief=RAISED,
                     bd=5,
                     padx=20,
                     pady=10,
                     activebackground="#3B10D4",
                     activeforeground="#ED0F0F",
                     command=lambda: [terminate_menu(), change_exit_button_text("Save / back"), change_exit_button_command(lambda: [restore_menu(), change_exit_button_text("Exit"), change_exit_button_command(exit_game)]), show_intro()  ],
                     )# Placeholder command
play_button.place(relx=relx(760), rely=rely(600))

acc_label = Label(game_window, 
                  text="Current User: " + username,
                  font=("MS Serif", 20),
                  fg ="#000000",
                  bg="#EBDB7F",
                  pady = 10,
                  )
acc_label.place(relx=relx(1600), rely=rely(1000))

exit_button = Button(game_window,
                     text="Exit",
                     font=("MS Serif", 20),
                     fg="#000000",
                     bg="#FFFFFF",
                     relief=RAISED,
                     bd=5,
                     padx=10,
                     pady=5,
                     activebackground="#3B10D4",
                     activeforeground="#ED0F0F",
                     command=lambda: exit_game(),
                    width=10,
                    height=2,
)
exit_button.place(relx=relx(0), rely=rely(1000))

game_window.mainloop()