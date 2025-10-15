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

big_label.place(relx=0.5, rely=0.1, anchor=CENTER)

# Functions to manage menu state
def terminate_menu():
    big_label.place_forget()
    play_button.place_forget()

def change_exit_button_text(new_text): # Change the text of the exit button
    exit_button.config(text=new_text)

def change_exit_button_command(new_command): # Change the command of the exit button
    exit_button.config(command=new_command)


def restore_menu(): # Restore the main menu elements
    big_label.place(relx=0.5, rely=0.1, anchor=CENTER)
    play_button.place(relx=relx(850), rely=rely(600))
    acc_label.place(relx=relx(1600), rely=rely(1000))

game_frame = None  # Global variable to hold the game frame

def return_to_menu():
    global game_frame # Declare game_frame as global to modify it
    if game_frame: # If the game frame exists, destroy it
        game_frame.destroy()
        game_frame = None # Clear the reference to the game frame
    restore_menu() # Restore the main menu elements
    change_exit_button_text("Exit")
    change_exit_button_command(lambda: exit_game()) # Restore exit button functionality

story_intro = (username + ", welcome to 'The Quest For The First Calculator'! In this adventure, you will crack codes based on logics and arithmetics across a diverse range of topics in mathematics. Get ready for an exciting journey through time and numbers!")
part_1_story = (username.title() + " finds himself in a dimly lit room, the air thick with the scent of old parchment and ink. In front of him lies an ancient scroll, its edges frayed and worn. As he unrolls it, he sees a series of symbols and numbers that seem to dance on the page. Suddenly, a voice echoes in the room, 'To unlock the secrets of the past, you must solve my riddles. Only then will you find the path to the first calculator.'")
stage_1_code = random.randint(1000, 9999)  # Random 4-digit code for stage 1, sorted for clue generation
stage_1_clue = f"for developers: the code is {stage_1_code}"
def show_intro():
    intro_label = Label(game_frame, 
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
    next_button = Button(game_frame,
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
    part_one_label = Label(game_frame, 
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
    next_button = Button(game_frame,
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
    global s1_code_entry, s1_submit_button
    stage_label = Label(game_frame, 
                      text="Stage 1: The Ancient Code",
                      font=("MS Serif", 60),
                      fg ="#000000",
                      bg="#EBDB7F",
                      padx=20,
                      pady=20,
                      )
    stage_label.place(relx=0.5, rely=0.1, anchor=CENTER)
    clue_label = Label(game_frame, 
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
    indicator_label = Label(game_frame, 
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
    s1_code_entry = Entry(game_frame, 
                       font=("MS Serif", 20),
                       fg="#000000",
                       bg="#FFFFFF",
                       bd=5,
                       width=10
                       )
    s1_code_entry.place(relx=relx(800), rely=rely(600))
    s1_submit_button = Button(game_frame,
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
                         command=lambda: check_stage_1_code(s1_code_entry.get()))
    s1_submit_button.place(relx=relx(800), rely=rely(700))
    s1_feedback_label = Label(game_frame, 
                          text="",
                          font=("MS Serif", 20),
                          fg ="#000000",
                          bg="#EBDB7F",
                          padx=20,
                          pady=20, 
                            wraplength=1200, 
            )   
    s1_feedback_label.place(relx=relx(600), rely=rely(800))
    def check_stage_1_code(entered_code):

        if entered_code == str(stage_1_code):           
            s1_code_entry.config(state='disabled')  # Disable entry after correct code
            s1_submit_button.config(state='disabled')  # Disable submit button after correct code
            s1_feedback_label.config(text="Correct! You've unlocked the next stage.") 
            next_button_2 = Button(game_frame,
                                   text="Next Stage",
                                      font=("MS Serif", 20),
                                        fg="#000000",
                                        bg="#FFFFFF",
                                        relief=RAISED,
                                        bd=5,
                                        padx=10,
                                        pady=5,
                                        activebackground="#3B10D4",
                                        activeforeground="#ED0F0F",
                                        command=lambda: [s1_feedback_label.place_forget(), next_button_2.place_forget(), stage_label.place_forget(), s1_code_entry.place_forget(),clue_label.place_forget(), indicator_label.place_forget(),  s1_submit_button.place_forget(), stage_2_story()]) # Placeholder for next stage function
            next_button_2.place(relx=relx(800), rely=rely(900))

            # Proceed to next stage or end game
        else:
            s1_feedback_label.config(text="Incorrect code. Try again.")


stage_2_story_text = (username.title() + " steps through a hidden door revealed by solving the ancient code. The door leads outside. The sun is shining brightly, and the sound of birds chirping fills the air. In the distance, " + username + " sees a group of people gathered around a strange device. As he approaches, he realizes it's an early version of a calculator. A wise scholar steps forward and says, 'To truly understand this device, you must first master the art of arithmetic. Solve my puzzles, and the calculator shall be one step closer to you.'")
stage_2_code = random.randint(10000, 99999)  # Random 5-digit code for stage 2, sorted for clue generation
stage_2_clue = f"for developers: the code is {stage_2_code}"

def stage_2_story():
    global stage_two_label
    stage_two_label = Label(game_frame, 
                      text="Stage 2: The Scholar's Challenge",
                      font=("MS Serif", 60),
                      fg ="#000000",
                      bg="#EBDB7F",
                      padx=20,
                      pady=20,
                      wraplength=1200,
                      justify="center",
                      )
    stage_two_label.place(relx=0.5, rely=0.1, anchor=CENTER)
    story_label = Label(game_frame, 
                      text=stage_2_story_text,
                      font=("MS Serif", 20),
                      fg ="#000000",
                      bg="#EBDB7F",
                      padx=20,
                      pady=20,
                      wraplength=1200,
                      justify="center",
                      )
    story_label.place(relx=relx(120), rely=rely(400))
    
    next_button = Button(game_frame,
                         text="Begin Stage 2",
                         font=("MS Serif", 20),
                         fg="#000000",
                         bg="#FFFFFF",
                         relief=RAISED,
                         bd=5,
                         padx=10,
                         pady=5,
                         activebackground="#3B10D4",
                         activeforeground="#ED0F0F",
                         command=lambda: [story_label.place_forget(), next_button.place_forget(), stage_2(),])
    next_button.place(relx=relx(800), rely=rely(700))

def stage_2():
    global s2_code_entry, s2_submit_button
    clue_label = Label(game_frame, 
                      text="Clue: " + stage_2_clue,
                      font=("MS Serif", 20),
                      fg ="#000000",
                      bg="#EBDB7F",
                      padx=20,
                      pady=20,
                      wraplength=1200,
                      justify="center",
                      )
    clue_label.place(relx=relx(500), rely=rely(300))
    indicator_label = Label(game_frame, 
                      text="Enter the 5-digit code to proceed:",
                      font=("MS Serif", 15),
                      fg ="#000000",
                      bg="#EBDB7F",
                      padx=20,
                      pady=20,
                      wraplength=1200,
                      justify="center",
                      )
    indicator_label.place(relx=relx(750), rely=rely(550))
    s2_code_entry = Entry(game_frame, 
                       font=("MS Serif", 20),
                       fg="#000000",
                       bg="#FFFFFF",
                       bd=5,
                       width=10
                       )
    s2_code_entry.place(relx=relx(800), rely=rely(600))
    s2_submit_button = Button(game_frame,
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
                         command=lambda: check_stage_2_code(s2_code_entry.get()))
    s2_submit_button.place(relx=relx(800), rely=rely(700))
    s2_feedback_label = Label(game_frame, 
                          text="",
                          font=("MS Serif", 20),
                          fg ="#000000",
                          bg="#EBDB7F",
                          padx=20,
                          pady=20, 
                            wraplength=1200, 
            )   
    s2_feedback_label.place(relx=relx(600), rely=rely(800))
    def check_stage_2_code(entered_code):
        feedback_label = Label(game_frame, 
                          text="",
                          font=("MS Serif", 20),
                          fg ="#000000",
                          bg="#EBDB7F",
                          padx=20,
                          pady=20, 
                            wraplength=1200, 
            )
        if entered_code == str(stage_2_code):  
            s2_code_entry.config(state='disabled')  # Disable entry after correct code
            s2_submit_button.config(state='disabled')  # Disable submit button after correct code         
            s2_feedback_label.config(text="Correct! You've unlocked the next stage.") 
            next_button_3 = Button(game_frame,
                                   text="Next Stage",
                                      font=("MS Serif", 20),
                                        fg="#000000",
                                        bg="#FFFFFF",
                                        relief=RAISED,
                                        bd=5,
                                        padx=10,
                                        pady=5,
                                        activebackground="#3B10D4",
                                        activeforeground="#ED0F0F",
                                        command=lambda: [s2_feedback_label.place_forget(), next_button_3.place_forget(), stage_two_label.place_forget(), s2_code_entry.place_forget(),clue_label.place_forget(), indicator_label.place_forget(),  s2_submit_button.place_forget(), next_button_3.place_forget(), show_part_3()]) # Placeholder for next stage function
            next_button_3.place(relx=relx(800), rely=rely(900))

        else:
            s2_feedback_label.config(text="Incorrect code. Try again.")

stage_3_story_text = (username.title() + " steps closer to the ancient calculator, feeling a mix of excitement and curiosity. The scholar smiles and waves his wand, suddenly, a portal opens. " + username + " steps through and finds himself in a ancient tomb. Before him lies a pedestal with an ancient calculator. However, to claim it, he must solve one final puzzle. The scholar's voice echoes, 'This calculator is the key to the future. Solve this final riddle, and it shall be yours.'")
stage_3_code = random.randint(100000, 999999)  # Random 6-digit code for stage 3, sorted for clue generation
stage_3_clue = f"for developers: the code is {stage_3_code}"

def show_part_3():
    global stage_three_label
    stage_three_label = Label(game_frame, 
                      text="Stage 3: The Final Riddle",
                      font=("MS Serif", 60),
                      fg ="#000000",
                      bg="#EBDB7F",
                      padx=20,
                      pady=20,
                      wraplength=1200,
                      )
    stage_three_label.place(relx=0.5, rely=0.1, anchor=CENTER)
    story_label = Label(game_frame, 
                      text=stage_3_story_text,
                      font=("MS Serif", 20),
                      fg ="#000000",
                      bg="#EBDB7F",
                      padx=20,
                      pady=20,
                      wraplength=1200,
                      justify="center",
                      )
    story_label.place(relx=relx(120), rely=rely(400))
    
    next_button_4 = Button(game_frame,
                         text="Begin Stage 3",
                         font=("MS Serif", 20),
                         fg="#000000",
                         bg="#FFFFFF",
                         relief=RAISED,
                         bd=5,
                         padx=10,
                         pady=5,
                         activebackground="#3B10D4",
                         activeforeground="#ED0F0F",
                         command=lambda: [story_label.place_forget(), next_button_4.place_forget(), stage_3(),])
    next_button_4.place(relx=relx(800), rely=rely(700))

def stage_3():
    global s3_code_entry, s3_submit_button
    clue_label = Label(game_frame, 
                      text="Clue: " + stage_3_clue,
                      font=("MS Serif", 20),
                      fg ="#000000",
                      bg="#EBDB7F",
                      padx=20,
                      pady=20,
                      wraplength=1200,
                      justify="center",
                      )
    clue_label.place(relx=relx(500), rely=rely(300))
    indicator_label = Label(game_frame, 
                      text="Enter the 6-digit code to proceed:",
                      font=("MS Serif", 15),
                      fg ="#000000",
                      bg="#EBDB7F",
                      padx=20,
                      pady=20,
                      wraplength=1200,
                      justify="center",
                      )
    indicator_label.place(relx=relx(750), rely=rely(550))
    s3_code_entry = Entry(game_frame, 
                       font=("MS Serif", 20),
                       fg="#000000",
                       bg="#FFFFFF",
                       bd=5,
                       width=10
                       )
    s3_code_entry.place(relx=relx(800), rely=rely(600))
    s3_submit_button = Button(game_frame,
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
                         command=lambda: check_stage_3_code(s3_code_entry.get()))
    s3_submit_button.place(relx=relx(800), rely=rely(700))
    s3_feedback_label = Label(game_frame, 
                          text="",
                          font=("MS Serif", 20),
                          fg ="#000000",
                          bg="#EBDB7F",
                          padx=20,
                          pady=20, 
                            wraplength=1200, 
            )   
    s3_feedback_label.place(relx=relx(430), rely=rely(800))
    def check_stage_3_code(entered_code):
        if entered_code == str(stage_3_code):    
            s3_submit_button.place_forget()
            s3_code_entry.place_forget()
            indicator_label.place_forget()
            clue_label.place_forget()
            stage_three_label.pack_forget()
            final_story = (username.title() + " solves the final riddle, and as he does, the ancient calculator glows with a mystical light. The scholar appears beside him, nodding in approval. 'You have proven yourself worthy,' he says. 'This calculator is not just a tool; it's a symbol of human ingenuity and the power of knowledge. Use it wisely.' With that, the scholar vanishes, leaving " + username + " alone with the ancient calculator, ready to unlock its secrets and shape the future.")
            s3_feedback_label.config(text="Congratulations! You've completed the quest and unlocked the ancient calculator!") 
            congrats_label = Label(game_frame,
                                   text="Congratulations!",
                                      font=("MS Serif", 60),
                                        fg="#000000",
                                        bg="#EBDB7F",
                                        padx=20,
                                        pady=20,
                                        wraplength=1200,
                                        )
            congrats_label.place(relx=0.5, rely=0.1, anchor=CENTER)
            final_label = Label(game_frame, 
                      text=final_story,
                      font=("MS Serif", 20),
                      fg ="#000000",
                      bg="#EBDB7F",
                      padx=20,
                      pady=20,
                      wraplength=1200,
                      )
            final_label.place(relx=relx(130), rely=rely(400))
            next_button_5 = Button(game_frame,
                                   text="Finish",
                                      font=("MS Serif", 20),
                                        fg="#000000",
                                        bg="#FFFFFF",
                                        relief=RAISED,
                                        bd=5,
                                        padx=10,
                                        pady=5,
                                        activebackground="#3B10D4",
                                        activeforeground="#ED0F0F",
                                        command=lambda: [ congrats_label.place_forget(),final_label.place_forget(),s3_feedback_label.place_forget(), next_button_5.place_forget(), stage_three_label.place_forget(), s3_code_entry.place_forget(),clue_label.place_forget(), indicator_label.place_forget(),  s3_submit_button.place_forget(), restore_menu()]) 
            next_button_5.place(relx=relx(900), rely=rely(900))
        else:
            s3_feedback_label.config(text="Incorrect code. Try again.")




acc_label = Label(game_window, 
                  text="Current User: " + username,
                  font=("MS Serif", 20),
                  fg ="#000000",
                  bg="#EBDB7F",
                  pady = 10,
                  )
acc_label.place(relx=relx(1600), rely=rely(1000))

play_button = Button(game_window,
                     text="Play",
                     font=("MS Serif", 30),
                     fg="#000000",
                     bg="#FFFFFF",
                     relief=RAISED,
                     bd=5,
                     padx=10,
                     pady=5,
                     activebackground="#3B10D4",
                     activeforeground="#ED0F0F",
                     command=lambda: [terminate_menu(), 
                                       change_exit_button_text("Save/exit"),
                                         change_exit_button_command(return_to_menu),
                                         start_game_sequence()] # Start the game sequence
)
def start_game_sequence():
    global game_frame
    game_frame = tk.Frame(game_window, bg="#EBDB7F") # Create a new frame for the game
    game_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
    acc_label.lift() # Ensure the account label is on top
    exit_button.lift() # Ensure the exit button is on top
    show_intro() # Start with the intro

play_button.place(relx=relx(850), rely=rely(600))
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

def handle_global_enter(event=None): # Handles Enter key presses globally, set event to None to allow calling without an event,
     if 's1_submit_button' in globals() and s1_submit_button.winfo_ismapped(): # Check if stage 1 submit button exists and is visible
         s1_submit_button.invoke() # Simulate button click
         return
     elif 's2_submit_button' in globals() and s2_submit_button.winfo_ismapped(): # Check if stage 2 submit button exists and is visible
         s2_submit_button.invoke() # Simulate button click
         return # Exit the function after handling
     elif 's3_submit_button' in globals() and s3_submit_button.winfo_ismapped(): # Check if stage 3 submit button exists and is visible
         s3_submit_button.invoke() # Simulate button click
         return
game_window.bind('<Return>', handle_global_enter) #binds the Enter key to the function that handles it
game_window.mainloop()