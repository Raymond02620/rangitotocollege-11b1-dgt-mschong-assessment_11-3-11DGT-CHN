from tkinter import *
import tkinter as tk
import sys
import subprocess

rule_window = tk.Tk()
screen_width = rule_window.winfo_screenwidth()
screen_height = rule_window.winfo_screenheight()
rule_window.geometry(f"{screen_width}x{screen_height}")
rule_window.title("Anarchy Rock, Paper Scissors - Rules")
gm_icon = PhotoImage(file='Python/CHONG/Screenshot 2025-09-01 123022.gif')
gm_icon = gm_icon.subsample(2,2)
rule_window.iconphoto(True, gm_icon)

def relx(x): return x / 1920
def rely(y): return y / 1080

if len(sys.argv) > 1:  # Check if a username argument is provided
    username = sys.argv[1] # Get the username from command line arguments
else:
    username = "Guest" # Default to "Guest" if no username is provided

canvas_setup = Canvas(rule_window, bg="white", highlightthickness=0)

resizable_canvas_items = []

def resize_canvas_elements(event):
    canvas_width = event.width
    canvas_height = event.height
    for item_id, item_type, design_coords in resizable_canvas_items:
        if item_type in ['line', 'rectangle', 'oval']:
            design_x0, design_y0, design_x1, design_y1 = design_coords
            new_coords = (
                relx(design_x0) * canvas_width, #calculate drawing positioning based on screen dimentions
                rely(design_y0) * canvas_height,
                relx(design_x1) * canvas_width,
                rely(design_y1) * canvas_height
            )
            canvas_setup.coords(item_id, *new_coords) #the new values in the tuple need to be individual arguments. the astetick tells the system to unpack whatever is in the tuple into these arguments.

def create_responsive_line(design_x0, design_y0, design_x1, design_y1, **kwargs):
    # the double asterick on the kwargs here means to take any 'key word arguments' such as fill, and put whatever it sees into a dictionary.
    item_id = canvas_setup.create_line(0, 0, 0, 0, **kwargs) #now the astericks tells the system to unpack the dictionary into arguments upon a function call, so it does the reverse. It is a highly flexiable tool to use.
    design_coords = (design_x0, design_y0, design_x1, design_y1)
    resizable_canvas_items.append((item_id, 'line', design_coords)) #must put the item ito list if it wants to be resized
    return item_id

def create_responsive_rectangle(design_x0, design_y0, design_x1, design_y1, **kwargs):
    item_id = canvas_setup.create_rectangle(0, 0, 0, 0, **kwargs)
    design_coords = (design_x0, design_y0, design_x1, design_y1)
    resizable_canvas_items.append((item_id, 'rectangle', design_coords)) #the list must know what I want, the type I want and the placement of my item.
    return item_id

def create_responsive_oval(design_x0, design_y0, design_x1, design_y1, **kwargs): 
    item_id = canvas_setup.create_oval(0, 0, 0, 0, **kwargs)
    design_coords = (design_x0, design_y0, design_x1, design_y1)
    resizable_canvas_items.append((item_id, 'oval', design_coords))
    return item_id


canvas_setup.bind("<Configure>", resize_canvas_elements)

create_responsive_line(0, 0, 0, 1080, fill="black", width=50)
create_responsive_line(0,0,1920,0, fill = "black", width = 50)
create_responsive_line(0,1080,1920,1080, fill = "black", width = 50)
create_responsive_line(1920,0,1920,1080, fill = "black", width = 50)
create_responsive_rectangle(30,0,1889,200, fill = "#E42E2E", outline = "black")
create_responsive_rectangle(30,200,1889,850, fill = "#38B342", outline = "black")
create_responsive_rectangle(30,850,1889,1080, fill ="#E42E2E", outline = "black")

canvas_setup.pack(fill="both", expand=True) 

big_label = Label(rule_window, text = "THE SUFFERING, THE ANARCHY, THE RULES", font = ("MS Serif", 50), padx = 20, pady = 20, relief = RAISED, bd = 10, fg = "#141FEC", bg = "#B63D57")
big_label.place(relx = 0.5, rely = 0.1, anchor = CENTER)

text1_label = Label(rule_window, text = "Welcome, to Anarchy Rock, Paper Scissors!. The main objective in this game is simple: Ensure that you absolutely OBLIBERATE your opponent's sanity or get your sanity set to [NULL].", fg = "#000000", bg = "#38B342", font = ("MS Serif", 20), wraplength = 1200)
text1_label.place(relx = 0.5, rely = 0.2, anchor = CENTER)
text2_label = Label(rule_window, text = "The rules are simple: At the start of each round, you will be assigned 3 of my beautiful, handcrafted anarchy cards. You will not know what your opponent has (duh.) All you have to do, is to use logic, and (maybe) a bit of your common sense to predict your best chances of winning, then select a card - and pray that you win. (Yes. PRAY.)", fg = "#000000", bg = "#38B342", font = ("MS Serif", 20), wraplength = 1200)
text2_label.place(relx = 0.5, rely = 0.3, anchor = CENTER)
text3_label = Label(rule_window, text = "If you win, you will recieve a point (yippee!), but, if you don't, TOO BAD. Plus you get one additional roast from the creator (me). The first to three points, will win! As a reward, your sworn enemy will recieve: a). A moment of glory, b). the sheer joy of looking at you being roasted (yes, AGAIN.) or vice versa.", fg = "#000000", bg = "#38B342", font = ("MS Serif", 20), wraplength = 1200)
text3_label.place(relx = 0.5, rely = 0.45, anchor = CENTER)
text4_label = Label(rule_window, text = "There is currently 10 cards of anarchy in this game. So before you even decide to play and expect to obliberate a soul, I'd suggest you to go to the cards galore, and check out what cards we have on stock, and use what you'd define as 'common sense' to make out a sense of what beats what. Oh by the way, once you play a game, you can't leave. Yes, you can't return the main menu. BUT you can close the game forcefully if you like to be a boomer. Welp, thats it from me, and happy-enjoying-anarchy-sadism!", fg = "#000000", bg = "#38B342", font = ("MS Serif", 20), wraplength = 1200)
text4_label.place(relx = 0.5, rely = 0.65, anchor = CENTER)
exit_button = Button(rule_window, text = "Back to main menu", font = ("MS Serif", 20),  padx = 10, pady = 10, bd = 5, fg = "#E33D2B", bg = "#3F28EE", activebackground="#334EC4", activeforeground="#D71F47", relief = RAISED, height = 2, width = 15, command = lambda: ( rule_window.destroy(), subprocess.Popen(["python3", "Python/rps.py", username ])))
exit_button.place(relx = 0.5, rely = 0.9, anchor = CENTER)
rule_window.mainloop()
