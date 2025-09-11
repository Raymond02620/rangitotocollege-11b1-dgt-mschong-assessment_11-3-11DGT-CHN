"""This program is for the main-main menu for my TK GUI. Works cited from: 
https://www.youtube.com/watch?v=lyoyTlltFVU&list=PLZPZq0r_RZOOeQBaP5SeMjl2nwDcJaV0T - Channel: Bro Code - Tkinter tutourial playlist"""

from tkinter import * #Imports the tkinter library
import json #Imports the json library
import os

menu_window = Tk() #Creates/instanstiates a window 
menu_window.geometry("634x400") #Sets the size of the window, ratio is length:height
menu_window.title("The Chong Games Compedium - Main Menu") #Sets the title of the window
mm_icon = PhotoImage(file='Python/CHONG/Screenshot 2025-09-01 123022.png') #Imports an image to use as the icon of the window
mm_icon = mm_icon.subsample(2,2) #Resizes the image to be smaller by that factor
menu_window.iconphoto(True, mm_icon) #Sets the icon of the window
menu_window.config(background="#70B9E4") #Sets the background color of the window

 #creates a label for the title of the window
label = Label(menu_window,
              text = "🔥The Chong Games Compedium🔥",
              font = ('MS Serif', 74, 'bold'),
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

exit_button = Button(menu_window,
                     text = "Exit",
                     font = ('MS Serif', 20),
                     fg = "#FFFFFF",
                     bg = "#FF0000",
                     relief = RAISED,
                     bd = 5,
                     activebackground= "#FF6923", #Changes color when clicked
                     padx = 10,
                     pady = 5,
                     command = menu_window.quit) #Quits the window when clicked
exit_button.place(x=350, y=750) #Places the button at the x and y coordinates


#creates a function for the fun button which will display a jumpscare when clicked

jumpscarephoto = PhotoImage(file='Python/CHONG/Screenshot 2025-09-03 150600.png') #Imports an image to use as the jumpscare
def fun():
    jumpscare_window = Toplevel() #Creates a new window on top of the main menu window
    jumpscare_window.geometry("800x600") #Sets the size of the window, ratio is length:height
    jumpscare_window.title("FUN BUTTON ACTIVATED") #Sets the title of the window
    jumpscare_window.iconphoto(True, mm_icon) #Sets the icon of the window
    jumpscare_window.config(background="#000000") #Sets the background color of the window
    jumpscare_label = Label(jumpscare_window,
                            text = "BOO!",
                            font = ('MS Serif', 74, 'bold'),
                            fg="#FF0000",
                            bg = "#000000",
                            image = jumpscarephoto,
                            compound = 'bottom',)
    jumpscare_label.pack() #Packs the label into the window
    jumpscare_button = Button(jumpscare_window,
                              text = "Close",
                              font = ('MS Serif', 20),
                              fg = "#FFFFFF",
                              bg = "#FF0000",
                              relief = RAISED,
                              bd = 5,
                              activebackground= "#FF6923", #Changes color when clicked
                              padx = 10,
                              pady = 5,
                              command = jumpscare_window.destroy) #Closes the jumpscare window when clicked
    jumpscare_button.place(x=350, y=500) #Places the button at the x and y coordinates
        
fun_button = Button(menu_window,
                    text = "PRESS ME FOR FUN",
                    font = ('MS Serif', 20),
                    fg = "#d84141",
                    bg = "#201A53",
                    activebackground= "#23FFF4", 
                    activeforeground= "#D434C4",
                    relief = RAISED,
                    bd = 5, #Border thickness
                    padx = 10,
                    pady = 5,
                    command = fun) #Prints to console when clicked
fun_button.place(x=10, y=750) #Places the button at the x and y coordinates

# a function thaat creates a input box below the button when the sign up button is clicked
def sign_up():
    username_label = Label(menu_window,
                          text = "Enter your username below:",
                          font = ('MS Serif', 14),
                          fg="#000000",
                          bg = "#70B9E4",)
    username_label.place(x=150, y=520) #Places the label at the x and y coordinates
    username_entry = Entry(menu_window,
                          font = ('MS Serif', 14),
                          fg="#000000",
                          bg = "#FFFFFF",
                          width = 30,)
    username_entry.place(x=150, y=550) #Places the entry box at the x and y coordinates
    #and now for the password input box
    password_label = Label(menu_window,
                          text = "Enter your password below:",
                          font = ('MS Serif', 14),
                          fg="#000000",
                          bg = "#70B9E4",)
    password_label.place(x=150, y=580) #Places the label at the x and y coordinates
    password_entry = Entry(menu_window,
                          font = ('MS Serif', 14),
                          fg="#000000",
                          bg = "#FFFFFF",
                          width = 30,
                          show="*") #Hides the password input
    password_entry.place(x=150, y=610) #Places the entry box at the x and y coordinates
    submit_button = Button(menu_window,
                           text = "Submit",
                           font = ('MS Serif', 14),
                           fg = "#FFFFFF",
                           bg = "#00AA00",
                           relief = RAISED,
                           bd = 5,
                           activebackground= "#23FF34", #Changes color when clicked
                           padx = 10,
                           pady = 5,
                           command = lambda: submit(username_entry, password_entry))
    #calls the submit function when the submit button is clicked
    submit_button.place(x=150, y=650) #Places the button at the x and y coordinates
    #end of sign_up function
    #function to save the username and password to a json file
    
def submit(username_entry, password_entry):
        username = username_entry.get()
        username = str(username) #Converts the username to a string to prevent json data type errors
        password = password_entry.get()
        password = str(password) #Converts the password to a string to prevent json data type errors
        password = str(password) #Converts the password to a string to prevent json data type errors
        prevent_overwrite() #Calls the prevent_overwrite function to prevent previous data from being overwritten
        if username in user_data:
            print("Username already exists!") #Prints to the console if the username already exists
        else:
            user_data[username] = password #saves the username and password to the dictionary
            with open('user_data.json', 'w') as f:
                json.dump(user_data, f)  #Saves the dictionary to a json file
            print("User data saved!") #Prints to the console
        username_entry.delete(0, END) #Clears the username entry box
        password_entry.delete(0, END) #Clears the password entry box

# loads the user data from the json file when the login button is clicked
def load_user_data():
    try:
        with open('user_data.json', 'r') as f:
            existing_data = json.load(f) #Loads the existing data from the json file
            user_data.update(existing_data) #Updates the dictionary with the existing data
            print("User data loaded!") #Prints to the console
            print(user_data) #Prints the dictionary to the console
    except FileNotFoundError:
        print("No user data found!") #Prints to the console if no file is found
    #end of load_user_data function

#function to prevent previous user data entered from the previous time the window is opened from being overwritten
def prevent_overwrite():
    try:
        with open('user_data.json', 'r') as f:
            existing_data = json.load(f) #Loads the existing data from the json file
            user_data.update(existing_data) #Updates the dictionary with the existing data
    except FileNotFoundError:
        pass #If the file does not exist, do nothing
    #end of submit function
    #saves the username and password to a dictionary


#creates a dictionary that stores usernames and passwords
#puts the info from the entry into the dictionary when the submit button is clicked
#each new username should be a new key, and each password should be the value   
user_data = {} #Creates an empty dictionary to store user data

sign_up_button = Button(menu_window,
                        text = "Sign Up",
                        font = ('MS Serif', 20),
                        fg = "#FFFFFF",
                        bg = "#0000FF",
                        relief = RAISED,
                        bd = 5,
                        command = sign_up, #Calls the sign_up function when clicked
                        activebackground= "#236BFF", #Changes color when clicked
                        padx = 10,
                        pady = 5,) #No command yet
sign_up_button.place(x=170, y=450) #Places the button at the x and y coordinates

#creates a login button that when clicked will create two input boxes for username and password
#a function that creates a input box below the button when the login button is clicked

#a function to verify the username and password when the submit button is clicked
def verify(username_entry, password_entry):
    username = username_entry.get()
    password = password_entry.get()
    if username in user_data and user_data[username] == password:
        print("Login successful!") #Prints to the console if the username and password match
        os.system("python gameselection.py")  #Opens the game selection window if the login is successful
        menu_window.destroy() #Closes the main menu window after opening the game selection window
    else:
        print("Login failed!") #Prints to the console if the username and password do not match
    username_entry.delete(0, END) #Clears the username entry box
    password_entry.delete(0, END) #Clears the password entry box
    #end of verify function

def login():
    username_label = Label(menu_window,
                          text = "Enter your username below:",
                          font = ('MS Serif', 14),
                          fg="#000000",
                          bg = "#70B9E4",)
    username_label.place(x=500, y=520) #Places the label at the x and y coordinates
    username_entry = Entry(menu_window,
                          font = ('MS Serif', 14),
                          fg="#000000",
                          bg = "#FFFFFF",
                          width = 30,)
    username_entry.place(x=500, y=550) #Places the entry box at the x and y coordinates
    #and now for the password input box
    password_label = Label(menu_window,
                          text = "Enter your password below:",
                          font = ('MS Serif', 14),
                          fg="#000000",
                          bg = "#70B9E4",)
    password_label.place(x=500, y=580) #Places the label at the x and y coordinates
    password_entry = Entry(menu_window,
                          font = ('MS Serif', 14),
                          fg="#000000",
                          bg = "#FFFFFF",
                          width = 30,
                          show="*") #Hides the password input
    password_entry.place(x=500, y=610) #Places the entry box at the x and y coordinates
    submit_button = Button(menu_window,
                           text = "Submit",
                           font = ('MS Serif', 14),
                           fg = "#FFFFFF",
                           bg = "#00AA00",
                           relief = RAISED,
                           bd = 5,
                           activebackground= "#23FF34", #Changes color when clicked
                           padx = 10,
                           pady = 5,
                           command = lambda: [ load_user_data, verify(username_entry, password_entry),])
    #check if the username and password match the data in the json file when the submit button is clicked

    #calls the verify function when the submit button is clicked
    submit_button.place(x=500, y=650) #Places the button at the x and y coordinates
    #end of login function

login_button = Button(menu_window,
                      text = "Login",
                      font = ('MS Serif', 20),
                      fg = "#FFFFFF",
                      bg = "#0000FF",
                      relief = RAISED,
                      bd = 5,
                      command = login, )#Calls the login function when clicked
login_button.place(x=550, y=450) #Places the button at the x and y coordinates

def guest_play():
#Opens the game selection window, ensures closing one window won't close both
    os.system("python gameselection.py")  #Opens the game selection window if the login is successful
    menu_window.destroy() #Closes the main menu window after opening the game selection window

guest_button = Button(menu_window,
                      text = "Play as Guest",
                      font = ('MS Serif', 20),
                      fg = "#FFFFFF",
                      bg = "#0000FF",
                      relief = RAISED,
                      bd = 5,
                      command = guest_play, )#Calls the guest_play function when clicked
guest_button.place(x=900, y=450) #Places the button at the x and y coordinates

menu_window.mainloop() #Runs the window infinitely until closed by user, listen for events.
