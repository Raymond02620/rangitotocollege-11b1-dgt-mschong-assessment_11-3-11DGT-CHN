from tkinter import *
import os

menu_window = Tk() #Creates/instanstiates a window 
menu_window.geometry("634x400") #Sets the size of the window, ratio is length:height
menu_window.title("The Chong Games Compedium - Game selection") #Sets the title of the window
mm_icon = PhotoImage(file='Python/CHONG/Screenshot 2025-09-01 123022.png') #Imports an image to use as the icon of the window
mm_icon = mm_icon.subsample(2,2) #Resizes the image to be smaller by that factor
menu_window.iconphoto(True, mm_icon) #Sets the icon of the window
menu_window.config(background="#70B9E4") #Sets the background color of the window



menu_window.mainloop() #Runs the window, must be at the end of the code

