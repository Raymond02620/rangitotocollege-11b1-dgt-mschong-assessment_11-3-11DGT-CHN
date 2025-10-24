from tkinter import *
import tkinter as tk
import subprocess
import sys

# Helper functions for dynamic placement
def relx(x): return x / 1920 # Assuming a base width of 1920 pixels
def rely(y): return y / 1080 # Assuming a base height of 1080 pixels

game_window = tk.Tk()

screen_width = game_window.winfo_screenwidth()
screen_height = game_window.winfo_screenheight()
game_window.geometry(f"{screen_width}x{screen_height}")
game_window.title("The Chong Games Compedium - Game Selection") #Sets the title of the window

game_window.config(background="#70B9E4") #Sets the background color of the window

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    username = "Guest"

big_label = Label(game_window, 
                  text="Welcome to The Chong Games Compedium, " + username + "!", 
                  font=("MS Serif", 40), 
                  fg ="#FFFFFF",
                  relief=RAISED,
                  bg="#70B9E4",
                  bd = 10,
                  padx = 10,
                  pady = 20,)
big_label.pack()

small_label = Label(game_window, 
                    text="Please select a game to play:", 
                    font=("MS Serif", 25), 
                    fg ="#FFFFFF",
                    bg="#70B9E4",
                    pady = 10,)
small_label.pack()

def enter_game1():
    game_window.destroy()
    subprocess.Popen(["python3", "Python/calculator.py", username])
def enter_game2():
    game_window.destroy()
    subprocess.Popen(["python3", "Python/clicker.py", username])
def enter_game3():
    game_window.destroy()
    subprocess.Popen(["python3", "Python/rps.py", username])


game1_button = Button(game_window,
                      text="Game 1: The Quest For the First Calculator",
                        font=("MS Serif", 30),
                        fg="#000000",
                        bg="#FFFFFF",
                        padx=20,
                        pady=10,
                        activebackground="#3B10D4",
                        activeforeground="#ED0F0F",
                        command=lambda: enter_game1())
game1_button.place(relx=relx(550), rely=rely(300))

game2_button = Button(game_window,
                      text="Game 2: The Chong Clicker",
                        font=("MS Serif", 30),
                        fg="#000000",
                        bg="#FFFFFF",
                        padx=20,
                        pady=10,
                        activebackground="#3B10D4",
                        activeforeground="#ED0F0F",
                        command=lambda: enter_game2())
game2_button.place(relx=relx(670), rely=rely(600))

game3_button = Button(game_window,
                      text="Game 3: Anarchy Rock Paper Scissors",
                        font=("MS Serif", 30),
                        fg="#000000",
                        bg="#FFFFFF",
                        padx=20,
                        pady=10,
                        activebackground="#3B10D4",
                        activeforeground="#ED0F0F",
                        command=lambda: enter_game3())
game3_button.place(relx=relx(590), rely=rely(900))

log_out_button = Button(game_window,
                        text="Log Out",
                        font=("MS Serif", 20),
                        fg="#000000",
                        bg="#FFFFFF",
                        padx=10,
                        pady=5,
                        activebackground="#3B10D4",
                        activeforeground="#ED0F0F",
                        command=lambda: [game_window.destroy(), subprocess.Popen(["python3", "Python/menu.py"])])
log_out_button.place(relx=relx(0), rely=rely(1000))
   

game_window.mainloop()