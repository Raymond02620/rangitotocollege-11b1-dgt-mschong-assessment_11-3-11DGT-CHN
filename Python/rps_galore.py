from tkinter import *
import tkinter as tk
import sys
import subprocess

galore_window = tk.Tk()
screen_width = galore_window.winfo_screenwidth()
screen_height = galore_window.winfo_screenheight()
galore_window.geometry(f"{screen_width}x{screen_height}")
galore_window.title("Anarchy Rock, Paper Scissors - Card Galore")


def relx(x): return x / 1920
def rely(y): return y / 1080

if len(sys.argv) > 1:  
    username = sys.argv[1] 
else:
    username = "Guest" 

canvas_setup = Canvas(galore_window, bg="white", highlightthickness=0)

resizable_canvas_items = []

def resize_canvas_elements(event):
    canvas_width = event.width
    canvas_height = event.height
    for item_id, item_type, design_coords in resizable_canvas_items:
        if item_type in ['line', 'rectangle', 'oval']:
            design_x0, design_y0, design_x1, design_y1 = design_coords
            new_coords = (
                relx(design_x0) * canvas_width, 
                rely(design_y0) * canvas_height,
                relx(design_x1) * canvas_width,
                rely(design_y1) * canvas_height
            )
            canvas_setup.coords(item_id, *new_coords)

def create_responsive_line(design_x0, design_y0, design_x1, design_y1, **kwargs):

    item_id = canvas_setup.create_line(0, 0, 0, 0, **kwargs) 
    design_coords = (design_x0, design_y0, design_x1, design_y1)
    resizable_canvas_items.append((item_id, 'line', design_coords)) 
    return item_id

def create_responsive_rectangle(design_x0, design_y0, design_x1, design_y1, **kwargs):
    item_id = canvas_setup.create_rectangle(0, 0, 0, 0, **kwargs)
    design_coords = (design_x0, design_y0, design_x1, design_y1)
    resizable_canvas_items.append((item_id, 'rectangle', design_coords)) 
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

big_label = Label(galore_window, text = "THE CHAOS, THE PAIN, THE 10 CARDS OF ETERNAL DOOM", font = ("MS Serif", 50), relief = RAISED, padx = 20, pady = 20, bd = 10, fg = "#141FEC", bg = "#B63D57")
big_label.place(relx = 0.5, rely = 0.1, anchor = CENTER)
label1  = Label(galore_window, text = "The Rock 🪨 - geological violence simulator", font = ("MS Serif", 20), padx = 20, pady = 20,  bd = 10, fg = "#000000", bg = "#38B342")
label1.place(relx = 0.5, rely = 0.2, anchor = CENTER)
label2  = Label(galore_window, text = "The Paper 🧾 - flat but emotionally unstable ", font = ("MS Serif", 20), padx = 20, pady = 20, bd = 10, fg = "#000000", bg = "#38B342")
label2.place(relx = 0.2, rely = 0.3, anchor = CENTER)
label3  = Label(galore_window, text = "The Scissors ✂️ - kindergarten hazard edition.", font = ("MS Serif", 20), padx = 20, pady = 20, bd = 10, fg = "#000000", bg = "#38B342")
label3.place(relx = 0.2, rely = 0.5, anchor = CENTER)
label4 = Label(galore_window, text = "The Fire 🔥 - hotter than your cpu on launch day", font = ("MS Serif", 20), padx = 20, pady = 20,  bd = 10, fg = "#000000", bg = "#38B342")
label4.place(relx = 0.2, rely = 0.7, anchor = CENTER)
label5  = Label(galore_window, text = "The Water 💧 - now in 144p resolution", font = ("MS Serif", 20), padx = 20, pady = 20,  bd = 10, fg = "#000000", bg = "#38B342")
label5.place(relx = 0.5, rely = 0.3, anchor = CENTER)
label6  = Label(galore_window, text = "The Earth 🌍 - dirt but make it emotional", font = ("MS Serif", 20), padx = 20, pady = 20,  bd = 10, fg = "#000000", bg = "#38B342")
label6.place(relx = 0.5, rely = 0.5, anchor = CENTER)
label7 = Label(galore_window, text = "The Air 💨 - its literally nothing", font = ("MS Serif", 20), padx = 20, pady = 20,  bd = 10, fg = "#000000", bg = "#38B342")
label7.place(relx = 0.5, rely = 0.7, anchor = CENTER)
label8 = Label(galore_window, text = "The Void ⚫ - game.uninstall()", font = ("MS Serif", 20), padx = 20, pady = 20,  bd = 10, fg = "#000000", bg = "#38B342")
label8.place(relx = 0.8, rely = 0.3, anchor = CENTER)
label9  = Label(galore_window, text = "The Darkness 🔮 - universe.exe corrupted ", font = ("MS Serif", 20), padx = 20, pady = 20,  bd = 10, fg = "#000000", bg = "#38B342")
label9.place(relx = 0.8, rely = 0.5, anchor = CENTER)
label10 = Label(galore_window, text = "The Lightning ⚡ - wifi but fatal", font = ("MS Serif", 20), padx = 20, pady = 20,  bd = 10, fg = "#000000", bg = "#38B342")
label10.place(relx = 0.8, rely = 0.7, anchor = CENTER)
exit_button = Button(galore_window, text = "Back to main menu", font = ("MS Serif", 20), padx = 10, pady = 10, bd = 5, fg = "#E33D2B", bg = "#3F28EE", activebackground="#334EC4", activeforeground="#D71F47", relief = RAISED, height = 2, width = 15, command = lambda: ( galore_window.destroy(), subprocess.Popen(["python3", "Python/rps.py", username ])))
exit_button.place(relx = 0.5, rely = 0.9, anchor = CENTER)
galore_window.mainloop()

