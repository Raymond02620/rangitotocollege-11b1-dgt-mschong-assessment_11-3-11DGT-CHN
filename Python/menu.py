from tkinter import *
import subprocess
import json
import time


"""
Works cited from: 


https://www.youtube.com/watch?v=lyoyTlltFVU&list=PLZPZq0r_RZOOeQBaP5SeMjl2nwDcJaV0T - Channel: Bro Code - Tkinter tutourial playlist

"""


user_data = {}

# Helper functions for dynamic placement
def relx(x): return x / 1920 # Assuming a base width of 1920 pixels
def rely(y): return y / 1080 # Assuming a base height of 1080 pixels



menu_window = Tk() #Creates/instanstiates a window
screen_width = menu_window.winfo_screenwidth()
screen_height = menu_window.winfo_screenheight()
menu_window.geometry(f"{screen_width}x{screen_height}")
menu_window.title("The Chong Games Compedium - Main Menu") #Sets the title of the window

menu_window.config(background="#70B9E4") #Sets the background color of the window


label = Label(menu_window,
            text = "🔥The Chong Games Compedium🔥",
            font = ('MS Serif', 74),
            fg="#D42D2D",
            bg = "#70B9E4",
            relief = RAISED,
            bd = 10,
            padx = 10,
            pady = 20,
            
            compound = 'bottom',)
label.pack()
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

dynamic_widgits = [] # List to keep track of dynamic widgets

def clear_dynamic_widgits():  # Function to clear dynamic widgets
    global dynamic_widgits # Access the global list
    for widget in dynamic_widgits: # Iterate through the list of dynamic widgets
        try: # Try to destroy each widget
            widget.destroy()
        except:# If it fails (e.g., widget already destroyed), just pass
            pass
    dynamic_widgits = []
    menu_window.unbind('<Return>')  # Unbind Enter key

def sign_up():
    clear_dynamic_widgits()
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
                           command = lambda: [submit(username_entry, password_entry), clear_dynamic_widgits()])
    submit_button.place(relx=relx(150), rely=rely(820))
    submit_button.focus_set() # Set focus to the submit button, which means it can be activated by pressing Enter
    menu_window.bind('<Return>', lambda event: submit_button.invoke())
    dynamic_widgits.extend([username_label, username_entry, password_label, password_entry, submit_button]) # Add widgets to the dynamic list (list operations)

signup_feedback_label = Label(menu_window,
                    text = "",
                    font = ('MS Serif', 14),
                    fg="#000000",
                    bg = "#70B9E4",)

signup_label_timer = None # Timer variable for clearing the label

def submit(username_entry, password_entry):
    global signup_label_timer
    username = (username_entry.get()).strip()
    username = str(username)
    password = (password_entry.get()).strip()
    password = str(password)
    password = str(password)
    prevent_overwrite()
    if signup_label_timer:
        menu_window.after_cancel(signup_label_timer) # Cancel previous timer if it exists
        signup_label_timer = None
    if username in user_data:
        signup_feedback_label.config(text="Username already exists!")
        signup_feedback_label.place(relx=relx(150), rely=rely(860))
        menu_window.update()
        signup_label_timer=menu_window.after(3000, lambda: signup_feedback_label.config(text="")) # Clear message after 3 seconds
    elif username == "" and password == "":
        signup_feedback_label.config(text="Please enter a username and password!")
        signup_feedback_label.place(relx=relx(150), rely=rely(860))
        menu_window.update()
        signup_label_timer=menu_window.after(3000, lambda: signup_feedback_label.config(text="")) # Clear message after 3 seconds
    elif username == "":
        signup_feedback_label.config(text="Please enter a username!")
        signup_feedback_label.place(relx=relx(150), rely=rely(860))
        menu_window.update()
        signup_label_timer=menu_window.after(3000, lambda: signup_feedback_label.config(text="")) # Clear message after 3 seconds
    elif password == "":
        signup_feedback_label.config(text="Please enter a password!")
        signup_feedback_label.place(relx=relx(150), rely=rely(860))
        menu_window.update()
        signup_label_timer=menu_window.after(3000, lambda: signup_feedback_label.config(text="")) # Clear message after 3 seconds
    else:
        user_data[username] = password
        with open('user_data.json', 'w') as f:
            json.dump(user_data, f)
        signup_feedback_label.config(text="Sign up successful!")
        signup_feedback_label.place(relx=relx(150), rely=rely(860))
        menu_window.update()
        signup_label_timer=menu_window.after(3000, lambda: signup_feedback_label.config(text="")) # Clear message after 3 seconds
        time.sleep(3) # Pause for a moment to let user see the success message
        subprocess.Popen(["python3", "Python/gameselection.py", username]) # Pass username as argument
        menu_window.quit()
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

login_label_timer = None # Timer variable for clearing the label
login_feedback_label = Label(menu_window,
                    text = "",
                    font = ('MS Serif', 14),
                    fg="#000000",
                    bg = "#70B9E4",)

def verify(username_entry, password_entry):
    global login_label_timer
    load_user_data()
    username = (username_entry.get()).strip()
    password = (password_entry.get()).strip()
    if login_label_timer:
        menu_window.after_cancel(login_label_timer) # Cancel previous timer if it exists
        login_label_timer = None
    if username in user_data and user_data[username] == password:
        login_feedback_label.config(text="Login successful! Logging in....")
        login_feedback_label.place(relx=relx(800), rely=rely(860))
        menu_window.update()
        login_label_timer=menu_window.after(3000, lambda: login_feedback_label.config(text="")) # Clear message after 3 seconds
        time.sleep(3) # Pause for a moment to let user see the success message
        subprocess.Popen(["python3", "Python/gameselection.py", username]) # Pass username as argument
        menu_window.quit()
    else:
        login_feedback_label.config(text="Invalid username or password!")
        login_feedback_label.place(relx=relx(800), rely=rely(860))
        menu_window.update()
        login_label_timer=menu_window.after(3000, lambda: login_feedback_label.config(text="")) # Clear message after 3 seconds
    username_entry.delete(0, END)
    password_entry.delete(0, END)

def login():
    clear_dynamic_widgits()
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
                           command = lambda: [ load_user_data(), verify(username_entry, password_entry), clear_dynamic_widgits(),])

    submit_button.place(relx=relx(800), rely=rely(810))
    submit_button.focus_set() # Set focus to the submit button, which means it can be activated by pressing Enter
    menu_window.bind('<Return>', lambda event: submit_button.invoke())
    dynamic_widgits.extend([username_label, username_entry, password_label, password_entry, submit_button]) # Add widgets to the dynamic list (list operations)
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
    menu_window.destroy()
    subprocess.Popen(["python3", "Python/gameselection.py"])

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

forgot_label_timer = None # Timer variable for clearing the label

def forgot_verify(username_entry):
    load_user_data()
    username = (username_entry.get()).strip()
    username = str(username)
    global forgot_label_timer
    try:
        if forgot_label_timer:
            menu_window.after_cancel(forgot_label_timer) # Cancel previous timer if it exists
            forgot_label_timer = None
        if username in user_data:
            password_label.config(text=f"Your password is: {user_data[username]}")
            password_label.place(relx=relx(1500), rely=rely(920))
            menu_window.update()
            forgot_label_timer=menu_window.after(3000, lambda: password_label.config(text="")) # Clear message after 3 seconds
        elif username == "":
            password_label.config(text="Please enter a username!")
            menu_window.update()
            forgot_label_timer=menu_window.after(3000, lambda: password_label.config(text="")) # Clear message after 3 seconds
        else:
            password_label.config(text="Username not found!")
            password_label.place(relx=relx(1500), rely=rely(920))
            menu_window.update()
            forgot_label_timer=menu_window.after(3000, lambda: password_label.config(text="")) # Clear message after 3 seconds
    except UnboundLocalError:
        print("No user data found!")
    username_entry.delete(0, END)

def forgot_password_username():
    global username_label, username_entry, submit_button
    clear_dynamic_widgits()
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
                           command = lambda: [forgot_verify(username_entry), clear_dynamic_widgits()])
    submit_button.place(relx=relx(1500), rely=rely(860))
    submit_button.focus_set() # Set focus to the submit button, which means it can be activated by pressing Enter
    menu_window.bind('<Return>', lambda event: submit_button.invoke())
    dynamic_widgits.extend([username_label, username_entry, submit_button]) # Add
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
                                command = lambda: forgot_password_username())
forgot_password_button.place(relx=relx(1500), rely=rely(960))

if __name__ == "__main__":
    menu_window.mainloop()
