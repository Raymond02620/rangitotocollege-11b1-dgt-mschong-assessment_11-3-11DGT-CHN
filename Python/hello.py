"""This program is for the main-main menu for my TK GUI. Works cited from: 
https://www.youtube.com/watch?v=lyoyTlltFVU&list=PLZPZq0r_RZOOeQBaP5SeMjl2nwDcJaV0T - Channel: Bro Code - Tkinter tutourial playlist"""

from tkinter import * #Imports the tkinter library
import json #Imports the json library

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
                           command = lambda: print(f"Username: {username_entry.get()}, Password: {password_entry.get()}")) #Prints the username and password to the console when clicked
    submit_button.place(x=270, y=650) #Places the button at the x and y coordinates
    #saves the username and password to a dictionary
    user_data = {} #Creates an empty dictionary to store the usernames and passwords
    user_data[username_entry.get()] = password_entry.get() #Adds the username and password to the dictionary
    print(user_data) #Prints the dictionary to the console for testing purposes
    save_user_data() #Calls the function to save the user data to a json file

#creates a dictionary that stores usernames and passwords
#puts the info from the entry into the dictionary when the submit button is clicked
#each new username should be a new key, and each password should be the value   
    
#saves the dictionary to a json file
def save_user_data():
    with open('user_data.json', 'w') as f: #Opens the file in write mode
        json.dump(user_data, f, ident = 4) #Dumps the dictionary into the file with an indent of 4 spaces for readability

#loads the dictionary from the json file when login button is clicked
def load_user_data():
   try:
       with open('user_data.json', 'r') as f: #Opens the file in read mode
           user_data = json.load(f) #Loads the dictionary from the file
           print(user_data) #Prints the dictionary to the console for testing purposes
   except FileNotFoundError:
        print("No user data found.") #Prints to the console if the file is not found


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
login_button = Button(menu_window,
                        text = "Login",
                        font = ('MS Serif', 20),
                        fg = "#FFFFFF",
                        bg = "#0000FF",
                        relief = RAISED,
                        bd = 5,
                        command = load_user_data, #Calls the load_user_data function when clicked
                        activebackground= "#236BFF", #Changes color when clicked
                        padx = 10,
                        pady = 5,) #No command yet
login_button.place(x=650, y=450) #Places the button at the x and y coordinates


menu_window.mainloop() #Runs the window infinitely until closed by user, listen for events.