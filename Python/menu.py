from tkinter import *
import os
import json
import time

menu_window = Tk() #Creates/instanstiates a window 
screen_width = menu_window.winfo_screenwidth()
screen_height = menu_window.winfo_screenheight()
menu_window.geometry(f"{screen_width}x{screen_height}")
menu_window.title("The Chong Games Compedium - Main Menu") #Sets the title of the window
mm_icon = PhotoImage(file='Python/CHONG/Screenshot 2025-09-01 123022.gif') #Imports an image to use as the icon of the window
mm_icon = mm_icon.subsample(2,2) #Resizes the image to be smaller by that factor
menu_window.iconphoto(True, mm_icon) #Sets the icon of the window
menu_window.config(background="#70B9E4") #Sets the background color of the window

# Helper functions for dynamic placement
def relx(x): return x / 1920
def rely(y): return y / 1080

label = Label(menu_window,
              text = "🔥The Chong Games Compedium🔥",
              font = ('MS Serif', 74),
              fg="#D42D2D",
              bg = "#70B9E4",
              relief = RAISED,
              bd = 10,
              padx = 10,
              pady = 20,
              image = mm_icon,
              compound = 'bottom',)
label.place(relx=0.5, rely=0.08, anchor='n') #DYNAMICALLY CENTERED

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
exit_button.place(relx=relx(200), rely=rely(960)) #DYNAMIC

def sign_up():
    username_label = Label(menu_window,
                          text = "Enter your username below:",
                          font = ('MS Serif', 14),
                          fg="#000000",
                          bg = "#70B9E4",)
    username_label.place(relx=relx(150), rely=rely(690))
    username_entry = Entry(menu_window,
                          font = ('MS Serif', 14),
                          fg="#000000",
                          bg = "#FFFFFF",
                          width = 30,)
    username_entry.place(relx=relx(150), rely=rely(720))
    password_label = Label(menu_window,
                          text = "Enter your password below:",
                          font = ('MS Serif', 14),
                          fg="#000000",
                          bg = "#70B9E4",)
    password_label.place(relx=relx(150), rely=rely(750))
    password_entry = Entry(menu_window,
                          font = ('MS Serif', 14),
                          fg="#000000",
                          bg = "#FFFFFF",
                          width = 30,
                          show="*")
    password_entry.place(relx=relx(150), rely=rely(780))
    submit_button = Button(menu_window,
                           text = "Submit",
                           font = ('MS Serif', 14),
                           fg = "#FFFFFF",
                           bg = "#00AA00",
                           relief = RAISED,
                           bd = 5,
                           activebackground= "#23FF34",
                           padx = 10,
                           pady = 5,
                           command = lambda: [submit(username_entry, password_entry), terminate_entries()])
    submit_button.place(relx=relx(150), rely=rely(820))
    def terminate_entries():
        username_label.destroy()
        username_entry.destroy()
        password_label.destroy()
        password_entry.destroy()
        submit_button.destroy()

def submit(username_entry, password_entry):
        username = (username_entry.get()).strip()
        username = str(username)
        password = (password_entry.get()).strip()
        password = str(password)
        password = str(password)
        prevent_overwrite()
        if username in user_data:
            print("Username already exists!")
        elif username == "" and password == "":
            print("Please enter a username and password!")
        else:
            user_data[username] = password
            with open('user_data.json', 'w') as f:
                json.dump(user_data, f)
            print("User data saved!")
        username_entry.delete(0, END)
        password_entry.delete(0, END)

def load_user_data():
    try:
        with open('user_data.json', 'r') as f:
            existing_data = json.load(f)
            user_data.update(existing_data)
    except FileNotFoundError:
        print("No user data found!")

def prevent_overwrite():
    try:
        with open('user_data.json', 'r') as f:
            existing_data = json.load(f)
            user_data.update(existing_data)
    except FileNotFoundError:
        pass

user_data = {}

sign_up_button = Button(menu_window,
                        text = "Sign Up",
                        font = ('MS Serif', 20),
                        fg = "#FFFFFF",
                        bg = "#0000FF",
                        relief = RAISED,
                        bd = 5,
                        command = sign_up,
                        activebackground= "#236BFF",
                        padx = 10,
                        pady = 5,)
sign_up_button.place(relx=relx(200), rely=rely(620))

def verify(username_entry, password_entry):
    username = username_entry.get()
    password = password_entry.get()
    if username in user_data and user_data[username] == password:
        print("Login successful!")
        os.system("python gameselection.py")
        menu_window.destroy()
    else:
        print("Login failed!")
    username_entry.delete(0, END)
    password_entry.delete(0, END)

def login():
    username_label = Label(menu_window,
                          text = "Enter your username below:",
                          font = ('MS Serif', 14),
                          fg="#000000",
                          bg = "#70B9E4",)
    username_label.place(relx=relx(800), rely=rely(690))
    username_entry = Entry(menu_window,
                          font = ('MS Serif', 14),
                          fg="#000000",
                          bg = "#FFFFFF",
                          width = 30,)
    username_entry.place(relx=relx(800), rely=rely(720))
    password_label = Label(menu_window,
                          text = "Enter your password below:",
                          font = ('MS Serif', 14),
                          fg="#000000",
                          bg = "#70B9E4",)
    password_label.place(relx=relx(800), rely=rely(750))
    password_entry = Entry(menu_window,
                          font = ('MS Serif', 14),
                          fg="#000000",
                          bg = "#FFFFFF",
                          width = 30,
                          show="*")
    password_entry.place(relx=relx(800), rely=rely(780))
    submit_button = Button(menu_window,
                           text = "Submit",
                           font = ('MS Serif', 14),
                           fg = "#FFFFFF",
                           bg = "#00AA00",
                           relief = RAISED,
                           bd = 5,
                           activebackground= "#23FF34",
                           padx = 10,
                           pady = 5,
                           command = lambda: [ load_user_data(), verify(username_entry, password_entry),])
    menu_window.bind("<Return>", lambda event: [load_user_data(), verify(username_entry, password_entry)])
    submit_button.place(relx=relx(800), rely=rely(810))

login_button = Button(menu_window,
                      text = "Login",
                      font = ('MS Serif', 20),
                      fg = "#FFFFFF",
                      bg = "#0000FF",
                      relief = RAISED,
                      bd = 5,
                      command = login, )
login_button.place(relx=relx(900), rely=rely(620))

def guest_play():
    os.system("python gameselection.py")
    menu_window.destroy()

guest_button = Button(menu_window,
                      text = "Play as Guest",
                      font = ('MS Serif', 20),
                      fg = "#FFFFFF",
                      bg = "#0000FF",
                      relief = RAISED,
                      bd = 5,
                      command = guest_play, )
guest_button.place(relx=relx(1500), rely=rely(620))

password_label = Label(menu_window,
                       text = "",
                       font = ('MS Serif', 14),
                       fg="#000000",
                       bg = "#70B9E4",)
def forgot_verify(username_entry):
    load_user_data()
    username = (username_entry.get()).strip()
    try:
        if username in user_data:
            password_label.config(text=f"Your username's password is: {user_data[username]}")
            password_label.place(relx=relx(1500), rely=rely(920))
            menu_window.update()
            time.sleep(5)
            password_label.config(text="")
        elif username == "":
            password_label.config(text="please enter a username!")
            password_label.place(relx=relx(1500), rely=rely(920))
            menu_window.update()
            time.sleep(3)
            password_label.config(text="")
        else:
            password_label.config(text=f"Username not found!")
            password_label.place(relx=relx(1500), rely=rely(920))
            menu_window.update()
            time.sleep(3)
            password_label.config(text="")
    except UnboundLocalError:
        print("No user data found!")
    username_entry.delete(0, END)

def forgot_password_username():
    global username_label, username_entry, submit_button
    username_label = Label(menu_window,
                          text = "Enter your username:",
                          font = ('MS Serif', 14),
                          fg="#000000",
                          bg = "#70B9E4",)
    username_label.place(relx=relx(1500), rely=rely(800))
    username_entry = Entry(menu_window,
                          font = ('MS Serif', 14),
                          fg="#000000",
                          bg = "#FFFFFF",
                          width = 30,)
    username_entry.place(relx=relx(1500), rely=rely(830))
    submit_button = Button(menu_window,
                           text = "Submit",
                           font = ('MS Serif', 14),
                           fg = "#FFFFFF",
                           bg = "#00AA00",
                           relief = RAISED,
                           bd = 5,
                           activebackground= "#23FF34",
                           padx = 10,
                           pady = 5,
                           command = lambda: [forgot_verify(username_entry), terminate_username_entries()])
    submit_button.place(relx=relx(1500), rely=rely(860))
def terminate_username_entries():
        username_label.destroy()
        username_entry.destroy()
        submit_button.destroy()
forgot_password_button = Button(menu_window,
                                text = "Forgot Password?",
                                font = ('MS Serif', 14),
                                fg = "#FFFFFF",
                                bg = "#FF0000",
                                relief = RAISED,
                                bd = 5,
                                activebackground= "#FF6923",
                                padx = 10,
                                pady = 5,
                                command = lambda: forgot_password_username() )
forgot_password_button.place(relx=relx(1500), rely=rely(960))

menu_window.mainloop() #Runs the window infinitely until closed by user, listen for events.
