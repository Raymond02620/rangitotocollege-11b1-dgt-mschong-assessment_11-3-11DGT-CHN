from tkinter import *
import tkinter as tk
import subprocess
import sys
import random
import json
import os


"work cited: https://www.youtube.com/watch?v=nKkBDtDjic4 - tutourial to learn more advanced json and intro to os"
if not os.path.exists('Python/calc'): # Create saves directory if it doesn't exist
    os.makedirs('Python/calc') # Create the directory

# Helper functions for dynamic placement
def relx(x): return x / 1920 # Assuming a base width of 1920 pixels
def rely(y): return y / 1080 # Assuming a base height of 1080 pixels

game_window = tk.Tk()

screen_width = game_window.winfo_screenwidth() # Get the screen width
screen_height = game_window.winfo_screenheight() # Get the screen height
game_window.geometry(f"{screen_width}x{screen_height}") # Set the window size to full screen
game_window.title("The Chong Games Compedium - The Quest For The First Calculator") #Sets the title of the window

game_window.config(background="#EBDB7F") #Sets the background color of the window


if len(sys.argv) > 1:  # Check if a username argument is provided
    username = sys.argv[1] # Get the username from command line arguments
else:
    username = "Guest" # Default to "Guest" if no username is provided

current_segment = 0 # Track the current segment of the game
for widget in game_window.winfo_children():
    widget.place_forget()
game_frame = None  # Global variable to hold the game frame


# --- Save/Load Functions ---
def save_game():
    if username != "Guest": # Only save if the user is not a guest
        save_file = f"Python/calc/{username}_calculator_save.json" # Define the save file path
        data = {
            "part": current_segment, # Save the current segment of the game
            "stage_1_code": stage_1_code,
            "stage_2_code": stage_2_code,
            "stage_3_code": stage_3_code,
        }
        
        with open(save_file, 'w') as f:
            json.dump(data, f) # Write the data to the JSON file
             

def load_game():
    global stage_1_code, stage_2_code, stage_3_code
    save_file = f"Python/calc/{username}_calculator_save.json" # Define the save file path
    if username != "Guest" and os.path.exists(save_file):
        try:
            with open(save_file, 'r') as f:
                data = json.load(f) # Load the data from the JSON file
                stage_1_code = data.get("stage_1_code", 0)
                stage_2_code = data.get("stage_2_code", 0)
                stage_3_code = data.get("stage_3_code", 0)
                return data.get("part", 0) # Return the saved part of the game
        except (json.JSONDecodeError, IOError):
            return 0 # Return 0 if there's an error loading the save file
    return 0 # Return 0 if no save file exists or user is Guest

def reset_progress():
    global current_segment
    current_segment = 0
    save_file = f"Python/calc/{username}_calculator_save.json"
    if os.path.exists(save_file):
        os.remove(save_file) # Delete the existing save file

# --- Main Menu and Navigation Functions ---
def exit_game():
    game_window.destroy()
    subprocess.Popen(["python3", "Python/gameselection.py", username]) # Return to game selection screen

def terminate_menu():
    big_label.place_forget()
    play_button.place_forget()
    continue_button.place_forget()
    new_game_button.place_forget()


def change_exit_button_text(new_text): # Change the text of the exit button
    if username != "Guest":
        exit_button.config(text=new_text)
    else:
        exit_button.config(text="Exit")

def change_exit_button_command(new_command): # Change the command of the exit button
    exit_button.config(command=new_command)

def randomise_code(): # Randomise the stage codes upon each new game
    global stage_1_code, stage_2_code, stage_3_code
    stage_1_code = random.randint(1000, 9999) # 4-digit code
    stage_2_code = random.randint(10000, 99999) # 5-digit code
    stage_3_code = random.randint(100000, 999999) # 6-digit code
    generate_clue() # Generate clues based on the new codes

def generate_clue(): # Randomise the stage codes upon each new game
    global  stage_1_clue, stage_2_clue, stage_3_clue
    s1_digits = [int(d) for d in str(stage_1_code)] # Extract digits
    sum_digits = sum(s1_digits)
    prod_digits = s1_digits[0] * s1_digits[-1] # Product of first and last digit
    stage_1_clue = f"My four digits sum to {sum_digits}. The product of my first and last digit is {prod_digits}. My third digit is {s1_digits[2]}."

    s2_str = str(stage_2_code)
    first_two = int(s2_str[0:2]) # First two digits
    last_two = int(s2_str[3:5]) # Last two digits
    middle_digit_type = "even" if int(s2_str[2]) % 2 == 0 else "odd" # Determine if the middle digit is even or odd
    stage_2_clue = stage_2_clue = f"I am a 5-digit number. My middle digit is {middle_digit_type}. My first two digits and last two digits (as numbers) sum to {first_two + last_two}. My fourth digit is {s2_str[3]}."

    s3_str = str(stage_3_code)
    part_a = int(s3_str[0:2]) # First two digits
    part_b = int(s3_str[2:4]) # Middle two digits
    part_c = int(s3_str[4:6]) # Last two digits
    sum_parts = part_a + part_b + part_c # Sum of the three parts
    c_divisor = next((i for i in range(9, 1, -1) if part_c > i and part_c % i == 0), None) # Find largest single-digit divisor
    divisor_clue = f"The last of these numbers is a multiple of {c_divisor}." if c_divisor else f"The last of these numbers ({part_c}) is prime."
    comparison = "greater than" if s3_str[0] > s3_str[5] else ("less than" if s3_str[0] < s3_str[5] else "equal to")
    stage_3_clue = f"Split me into three 2-digit numbers. Their sum is {sum_parts}. {divisor_clue} My first digit is {comparison} my last digit."

def restore_menu(): # Restore the main menu elements
    big_label.place(relx=0.5, rely=0.1, anchor=CENTER)
    show_main_menu_buttons()
    acc_label.place(relx=relx(1600), rely=rely(1000))

def start_fresh_game():
    randomise_code() # Randomise the codes for a new game
    save_file = f"Python/calc/{username}_calculator_save.json" # Define the save file path
    if os.path.exists(save_file):
        os.remove(save_file) # Delete the existing save file
    
    terminate_menu()
    change_exit_button_text("Save/exit")
    change_exit_button_command(return_to_menu)
    start_game_sequence()

def return_to_menu():
    global  game_frame, s1_code_entry, s1_submit_button, s2_code_entry, s2_submit_button, s3_code_entry, s3_submit_button, stage_two_label,stage_three_label # Declare game_frame as global to modify it
    save_game()  # Save the game state before returning to menu
    if game_frame:
        game_frame.destroy()  # Remove the game frame
        game_frame = None

    s1_code_entry = s1_submit_button = None
    s2_code_entry = s2_submit_button = None
    s3_code_entry = s3_submit_button = None
    stage_two_label = stage_three_label = None
    restore_menu()
    change_exit_button_text("Exit")
    change_exit_button_command(exit_game)

def finish_and_reset():
    global game_frame
    reset_progress()
    if game_frame:
        game_frame.destroy()
        game_frame = None
    restore_menu()
    change_exit_button_text("Exit")
    change_exit_button_command(exit_game)
# --- New Game / Continue Game Logic Functions ---


def show_main_menu_buttons(): # Shows the main menu buttons
    save_file = f"Python/calc/{username}_calculator_save.json" # Define the save file path
    save_exist = username != "Guest" and os.path.exists(save_file) # Check if the save file exists and user is not Guest

    if save_exist:
        play_button.place_forget()
        continue_button.place(relx=relx(850), rely=rely(600))
        new_game_button.place(relx=relx(850), rely=rely(700))
    else:
        continue_button.place_forget()
        new_game_button.place_forget()
        play_button.place(relx=relx(850), rely=rely(600))

# --- Game Sequence and Story Functions ---
story_intro = (username + ", welcome to 'The Quest For The First Calculator'! In this adventure, you will crack codes based on logics and arithmetics across a diverse range of topics in mathematics. Get ready for an exciting journey through time and numbers!")
part_1_story = (username.title() + " finds himself in a dimly lit room, the air thick with the scent of old parchment and ink. In front of him lies an ancient scroll, its edges frayed and worn. As he unrolls it, he sees a series of symbols and numbers that seem to dance on the page. A mysterious voice emerges from the room, it echos, 'Greetings, my name  is Archimedes. To unlock the secrets of the ancient calculator, you must first decipher the code before you. Solve the puzzle, and the path to the calculator will be revealed.'")
stage_1_code, stage_2_code, stage_3_code = 0, 0, 0 # Initialize stage codes
stage_1_clue, stage_2_clue, stage_3_clue = "", "", "" # Initialize stage clues
randomise_code()
stage_2_story_text = (username.title() + " steps through a hidden door revealed by solving the ancient code. The door leads outside. The sun is shining brightly, and the sound of birds chirping fills the air. In the distance, " + username.title() + " sees a group of people gathered around a strange device. As he approaches, he realizes it's an early version of a calculator. A wise scholar strolls towards" + username.title() + " and says, 'To unlock the full potential of this device, you must first prove yourknowledge of numbers and logic. Solve my challenge, and the gateway to the calculator will open.'")
stage_3_story_text = (username.title() + " steps closer to the ancient calculator, feeling a mix of excitement and curiosity. The scholar smiles and waves his wand, suddenly, a portal opens. " + username + " steps through and finds himself in a ancient tomb. Before him lies a pedestal with an ancient calculator. However, to claim it, he must solve one final puzzle. The scholar's voice echoes, 'This calculator is the key to the future. Solve this final riddle, and it shall be yours.'")
def show_intro():
    intro_label = Label(game_frame, text=story_intro, font=("MS Serif", 20), fg ="#000000", bg="#EBDB7F", padx=20, pady=20, wraplength=1200, justify="center")
    intro_label.place(relx=relx(125), rely=rely(400))
    next_button = Button(game_frame, text="Next", font=("MS Serif", 20), fg="#000000", bg="#FFFFFF", relief=RAISED, bd=5, padx=10, pady=5, activebackground="#3B10D4", activeforeground="#ED0F0F", command=lambda: [intro_label.place_forget(), next_button.place_forget(), show_part_one()])
    next_button.place(relx=relx(900), rely=rely(900))

def show_part_one():
    global current_segment
    current_segment = 0
    part_one_label = Label(game_frame, text=part_1_story, font=("MS Serif", 20), fg ="#000000", bg="#EBDB7F", padx=20, pady=20, wraplength=1200, justify="center")
    part_one_label.place(relx=0.5, rely=rely(400), anchor = CENTER)
    next_button = Button(game_frame, text="Begin Your Quest", font=("MS Serif", 20), fg="#000000", bg="#FFFFFF", relief=RAISED, bd=5, padx=10, pady=5, activebackground="#3B10D4", activeforeground="#ED0F0F", command=lambda: [part_one_label.place_forget(), next_button.place_forget(), stage_1()])
    next_button.place(relx=0.5, rely=rely(700), anchor = CENTER)

def stage_1():
    global s1_code_entry, s1_submit_button, current_segment
    current_segment = 1
    stage_label = Label(game_frame, text="Stage 1: The Ancient Code", font=("MS Serif", 60), fg ="#000000", bg="#EBDB7F", padx=20, pady=20)
    stage_label.place(relx=0.5, rely=0.1, anchor=CENTER)
    clue_entry = Entry(game_frame, font=("MS Serif", 20), fg="#000000", justify="center", bd=0, readonlybackground="#EBDB7F")
    clue_entry.insert(0, "Clue: " + stage_1_clue)
    clue_entry.config(state='readonly', width = len(clue_entry.get()) + 4)
    clue_entry.place(relx=0.5, rely=rely(350), anchor="center")
    indicator_label = Label(game_frame, text="Enter the 4-digit code to proceed:", font=("MS Serif", 15), fg ="#000000", bg="#EBDB7F", padx=20, pady=20, wraplength=1200, justify="center")
    indicator_label.place(relx=relx(750), rely=rely(550))
    s1_code_entry = Entry(game_frame, font=("MS Serif", 20), fg="#000000", bg="#FFFFFF", bd=5, width=10)
    s1_code_entry.place(relx=relx(800), rely=rely(600))
    s1_submit_button = Button(game_frame, text="Submit Code", font=("MS Serif", 20), fg="#000000", bg="#FFFFFF", relief=RAISED, bd=5, padx=10, pady=5, activebackground="#3B10D4", activeforeground="#ED0F0F", command=lambda: check_stage_1_code(s1_code_entry.get()))
    s1_submit_button.place(relx=relx(800), rely=rely(700))
    s1_feedback_label = Label(game_frame, text="", font=("MS Serif", 20), fg ="#000000", bg="#EBDB7F", padx=20, pady=20, wraplength=1200)
    s1_feedback_label.place(relx=0.5, rely=rely(800), anchor=CENTER)
    def check_stage_1_code(entered_code):
        if entered_code == str(stage_1_code):           
            s1_code_entry.config(state='disabled')
            s1_submit_button.config(state='disabled')
            s1_feedback_label.config(text="Correct! You've unlocked the next stage.") 
            next_button_2 = Button(game_frame, text="Next Stage", font=("MS Serif", 20), fg="#000000", bg="#FFFFFF", relief=RAISED, bd=5, padx=10, pady=5, activebackground="#3B10D4", activeforeground="#ED0F0F", command=lambda: [s1_feedback_label.place_forget(), next_button_2.place_forget(), stage_label.place_forget(), s1_code_entry.place_forget(),clue_entry.place_forget(), indicator_label.place_forget(),  s1_submit_button.place_forget(), stage_2_story()])
            next_button_2.place(relx=relx(800), rely=rely(900))
        else:
            s1_feedback_label.config(text="Incorrect code. Try again.")

def stage_2_story():
    global stage_two_label, current_segment
    current_segment = 2
    stage_two_label = Label(game_frame, text="Stage 2: The Scholar's Challenge", font=("MS Serif", 60), fg ="#000000", bg="#EBDB7F", padx=20, pady=20, wraplength=1200, justify="center")
    stage_two_label.place(relx=0.5, rely=0.1, anchor=CENTER)
    story_label = Label(game_frame, text=stage_2_story_text, font=("MS Serif", 20), fg ="#000000", bg="#EBDB7F", padx=20, pady=20, wraplength=1200, justify="center")
    story_label.place(relx=0.5, rely=rely(400), anchor=CENTER)
    next_button = Button(game_frame, text="Begin Stage 2", font=("MS Serif", 20), fg="#000000", bg="#FFFFFF", relief=RAISED, bd=5, padx=10, pady=5, activebackground="#3B10D4", activeforeground="#ED0F0F", command=lambda: [story_label.place_forget(), next_button.place_forget(), stage_2()])
    next_button.place(relx=0.5, rely=rely(700), anchor=CENTER)

def stage_2():
    global s2_code_entry, s2_submit_button
    clue2_entry = Entry(game_frame, font=("MS Serif", 20), fg="#000000", justify="center", bd=0, readonlybackground="#EBDB7F")
    clue2_entry.insert(0, "Clue: " + stage_2_clue)
    clue2_entry.config(state='readonly', width = len(clue2_entry.get()) + 4)
    clue2_entry.place(relx=0.5, rely=rely(350), anchor="center")
    indicator_label = Label(game_frame, text="Enter the 5-digit code to proceed:", font=("MS Serif", 15), fg ="#000000", bg="#EBDB7F", padx=20, pady=20, wraplength=1200, justify="center")
    indicator_label.place(relx=relx(750), rely=rely(550))
    s2_code_entry = Entry(game_frame, font=("MS Serif", 20), fg="#000000", bg="#FFFFFF", bd=5, width=10)
    s2_code_entry.place(relx=relx(800), rely=rely(600))
    s2_submit_button = Button(game_frame, text="Submit Code", font=("MS Serif", 20), fg="#000000", bg="#FFFFFF", relief=RAISED, bd=5, padx=10, pady=5, activebackground="#3B10D4", activeforeground="#ED0F0F", command=lambda: check_stage_2_code(s2_code_entry.get()))
    s2_submit_button.place(relx=relx(800), rely=rely(700))
    s2_feedback_label = Label(game_frame, text="", font=("MS Serif", 20), fg ="#000000", bg="#EBDB7F", padx=20, pady=20, wraplength=1200)
    s2_feedback_label.place(relx=0.5, rely=rely(800), anchor=CENTER)
    def check_stage_2_code(entered_code):
        if entered_code == str(stage_2_code):  
            s2_code_entry.config(state='disabled')
            s2_submit_button.config(state='disabled')
            s2_feedback_label.config(text="Correct! You've unlocked the next stage.") 
            next_button_3 = Button(game_frame, text="Next Stage", font=("MS Serif", 20), fg="#000000", bg="#FFFFFF", relief=RAISED, bd=5, padx=10, pady=5, activebackground="#3B10D4", activeforeground="#ED0F0F", command=lambda: [s2_feedback_label.place_forget(), next_button_3.place_forget(), stage_two_label.place_forget(), s2_code_entry.place_forget(), clue2_entry.place_forget(), indicator_label.place_forget(),  s2_submit_button.place_forget(), next_button_3.place_forget(), show_part_3()])
            next_button_3.place(relx=relx(800), rely=rely(900))
        else:
            s2_feedback_label.config(text="Incorrect code. Try again.")

def show_part_3():
    global stage_three_label, current_segment
    current_segment = 3
    stage_three_label = Label(game_frame, text="Stage 3: The Final Riddle", font=("MS Serif", 60), fg ="#000000", bg="#EBDB7F", padx=20, pady=20, wraplength=1200)
    stage_three_label.place(relx=0.5, rely=0.1, anchor=CENTER)
    story_label = Label(game_frame, text=stage_3_story_text, font=("MS Serif", 20), fg ="#000000", bg="#EBDB7F", padx=20, pady=20, wraplength=1200, justify="center")
    story_label.place(relx=0.5, rely=rely(400), anchor=CENTER)
    next_button_4 = Button(game_frame, text="Begin Stage 3", font=("MS Serif", 20), fg="#000000", bg="#FFFFFF", relief=RAISED, bd=5, padx=10, pady=5, activebackground="#3B10D4", activeforeground="#ED0F0F", command=lambda: [story_label.place_forget(), next_button_4.place_forget(), stage_3()])
    next_button_4.place(relx=0.5, rely=rely(700), anchor=CENTER)

def stage_3():
    global s3_code_entry, s3_submit_button
    clue3_entry = Entry(game_frame, font=("MS Serif", 20), fg="#000000", justify="center", bd=0, readonlybackground="#EBDB7F")
    clue3_entry.insert(0, "Clue: " + stage_3_clue)
    clue3_entry.config(state='readonly', width = len(clue3_entry.get()) + 4)
    clue3_entry.place(relx=0.5, rely=rely(350), anchor="center")
    indicator_label = Label(game_frame, text="Enter the 6-digit code to proceed:", font=("MS Serif", 15), fg ="#000000", bg="#EBDB7F", padx=20, pady=20, wraplength=1200, justify="center")
    indicator_label.place(relx=relx(750), rely=rely(550))
    s3_code_entry = Entry(game_frame, font=("MS Serif", 20), fg="#000000", bg="#FFFFFF", bd=5, width=10)
    s3_code_entry.place(relx=relx(800), rely=rely(600))
    s3_submit_button = Button(game_frame, text="Submit Code", font=("MS Serif", 20), fg="#000000", bg="#FFFFFF", relief=RAISED, bd=5, padx=10, pady=5, activebackground="#3B10D4", activeforeground="#ED0F0F", command=lambda: check_stage_3_code(s3_code_entry.get()))
    s3_submit_button.place(relx=relx(800), rely=rely(700))
    s3_feedback_label = Label(game_frame, text="", font=("MS Serif", 20), fg ="#000000", bg="#EBDB7F", padx=20, pady=20, wraplength=1200)
    s3_feedback_label.place(relx=0.5, rely=rely(850), anchor=CENTER)
    def check_stage_3_code(entered_code):
        global current_segment
        if entered_code == str(stage_3_code):    
            current_segment = 4
            s3_submit_button.place_forget()
            s3_code_entry.place_forget()
            indicator_label.place_forget()
            clue3_entry.place_forget()
            stage_three_label.place_forget()
            final_story = (username.title() + " solves the final riddle, and as he does, the ancient calculator glows with a mystical light. The scholar appears beside him, nodding in approval. 'You have proven yourself worthy,' he says. 'This calculator is not just a tool; it's a symbol of human ingenuity and the power of knowledge. Use it wisely.' With that, the scholar vanishes, leaving " + username + " alone with the ancient calculator, ready to unlock its secrets and shape the future.")
            s3_feedback_label.config(text="Congratulations! You've completed the quest and unlocked the ancient calculator!") 
            congrats_label = Label(game_frame, text="Congratulations!", font=("MS Serif", 60), fg="#000000", bg="#EBDB7F", padx=20, pady=20, wraplength=1200)
            congrats_label.place(relx=0.5, rely=0.1, anchor=CENTER)
            final_label = Label(game_frame, text=final_story, font=("MS Serif", 20), fg ="#000000", bg="#EBDB7F", padx=20, pady=20, wraplength=1200)
            final_label.place(relx=relx(130), rely=rely(400))
            next_button_5 = Button(game_frame, text="Finish", font=("MS Serif", 20), fg="#000000", bg="#FFFFFF", relief=RAISED, bd=5, padx=10, pady=5, activebackground="#3B10D4", activeforeground="#ED0F0F", command=finish_and_reset)
            next_button_5.place(relx=relx(900), rely=rely(900))
        else:
            s3_feedback_label.config(text="Incorrect code. Try again.")

def start_game_sequence():
    global game_frame, current_segment
    game_frame = tk.Frame(game_window, bg="#EBDB7F")
    game_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
    acc_label.lift()
    exit_button.lift()
    current_segment = load_game()
    if current_segment == 1:
        stage_1()
    elif current_segment == 2:
        stage_2_story()
    elif current_segment == 3:
        show_part_3()
    else:
        show_intro()

def handle_global_enter(event=None):
     if 's1_submit_button' in globals() and s1_submit_button is not None and s1_submit_button.winfo_ismapped():
         s1_submit_button.invoke()
         return
     elif 's2_submit_button' in globals() and s2_submit_button is not None and s2_submit_button.winfo_ismapped():
         s2_submit_button.invoke()
         return
     elif 's3_submit_button' in globals() and s3_submit_button is not None and s3_submit_button.winfo_ismapped():
         s3_submit_button.invoke()
         return

# --- Labels ---
big_label = Label(game_window, text="The Quest For The First Calculator", font=("MS Serif", 80), fg ="#000000", relief=RAISED, bg="#EBDB7F", bd = 10, padx = 10, pady = 20)
acc_label = Label(game_window, text="Current User: " + username, font=("MS Serif", 20), fg ="#000000", bg="#EBDB7F", pady = 10)

# --- Buttons ---
play_button = Button(game_window, text="Play", font=("MS Serif", 30), fg="#000000", bg="#FFFFFF", relief=RAISED, bd=5, padx=10, pady=5, activebackground="#3B10D4", activeforeground="#ED0F0F", command=lambda: [randomise_code(),terminate_menu(), change_exit_button_text("Save/exit"), change_exit_button_command(return_to_menu), start_game_sequence()])
continue_button = Button(game_window, text = "Continue game", font=("MS Serif", 30), fg="#000000", bg="#FFFFFF", relief=RAISED, bd=5, padx=10, pady=5, activebackground="#3B10D4", activeforeground="#ED0F0F", command=lambda: [terminate_menu(), change_exit_button_text("Save/exit"), change_exit_button_command(return_to_menu), start_game_sequence()])
new_game_button = Button(game_window, text = "New Game", font=("MS Serif", 30), fg="#000000", bg="#FFFFFF", relief=RAISED, bd=5, padx=10, pady=5, activebackground="#3B10D4", activeforeground="#ED0F0F", command=start_fresh_game)
exit_button = Button(game_window, text="Exit", font=("MS Serif", 20), fg="#000000", bg="#FFFFFF", relief=RAISED, bd=5, padx=10, pady=5, activebackground="#3B10D4", activeforeground="#ED0F0F", command=exit_game, width=10, height=2)

# --- Initial Layout ---
big_label.place(relx=0.5, rely=0.1, anchor=CENTER)
acc_label.place(relx=relx(1600), rely=rely(1000))
exit_button.place(relx=relx(0), rely=rely(1000))
show_main_menu_buttons()

# --- Bindings & Main Loop ---
game_window.bind('<Return>', handle_global_enter)
game_window.mainloop()
