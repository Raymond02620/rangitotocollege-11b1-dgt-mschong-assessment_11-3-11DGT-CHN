"""This program is for the main-main menu for my TK GUI. Works cited from: 
https://www.youtube.com/watch?v=lyoyTlltFVU&list=PLZPZq0r_RZOOeQBaP5SeMjl2nwDcJaV0T - Channel: Bro Code - Tkinter tutourial playlist"""

from tkinter import * #Imports EVERYTHING from tkinter

menu_window = Tk() #Creates/instanstiates a window 
menu_window.geometry("634x400") #Sets the size of the window, ratio is length:height
menu_window.title("The Chong Games Compedium - Main Menu") #Sets the title of the window
mm_icon = PhotoImage(file='Python/CHONG/Screenshot 2025-09-01 123022.png') #Imports an image to use as the icon of the window
mm_icon = mm_icon.subsample(2,2) #Resizes the image to be smaller by that factor
menu_window.iconphoto(True, mm_icon) #Sets the icon of the window
menu_window.config(background="#70B9E4") #Sets the background color of the window

 #creates a labbel for the title of the window
label = Label(menu_window,
              text = "🔥The Chong Games Compedium🔥",
              font = ('MS Serif', 90, 'bold'),
              fg="#D42D2D",
              bg = "#70B9E4",
              relief = RAISED,
              bd = 10,
              padx = 10,
              pady = 20,
              image = mm_icon,
              compound = 'bottom',)
#customize label, fg = text color, bg = background cover on the text

label.pack() #Packs the label into the window

exit_button = 


menu_window.mainloop() #Runs the window infinitely until closed by user, listen for events.