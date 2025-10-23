from tkinter import *
import tkinter as tk
import random
import json
import sys
import subprocess
import os

"""Tkinter tutourial used / cited: Brocode - canvas tutourial https://www.youtube.com/watch?v=171uIsavFf8 """

if not os.path.exists('Python/rps'): # Create saves directory if it doesn't exist
    os.makedirs('Python/rps') # Create the directory

game_window = tk.Tk()
screen_width = game_window.winfo_screenwidth()
screen_height = game_window.winfo_screenheight()
game_window.geometry(f"{screen_width}x{screen_height}")
game_window.title("The Chong Games Compedium - Anarchy Rock, Paper Scissors")
gm_icon = PhotoImage(file='Python/CHONG/Screenshot 2025-09-01 123022.gif')
gm_icon = gm_icon.subsample(2,2)
game_window.iconphoto(True, gm_icon)

def relx(x): return x / 1920
def rely(y): return y / 1080

if len(sys.argv) > 1:  # Check if a username argument is provided
    username = sys.argv[1] # Get the username from command line arguments
else:
    username = "Guest" # Default to "Guest" if no username is provided


canvas_setup = Canvas(game_window, bg="white", highlightthickness=0)

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

def create_responsive_oval(design_x0, design_y0, design_x1, design_y1, **kwargs): #Ill leave it here since thats the only 3 shapes I need.
    item_id = canvas_setup.create_oval(0, 0, 0, 0, **kwargs)
    design_coords = (design_x0, design_y0, design_x1, design_y1)
    resizable_canvas_items.append((item_id, 'oval', design_coords))
    return item_id

#and now I bind the whole dynamic sizing function to launch it.
canvas_setup.bind("<Configure>", resize_canvas_elements)

#Now I start drawing my screen
create_responsive_line(0, 0, 0, 1080, fill="black", width=50)
create_responsive_line(0,0,1920,0, fill = "black", width = 50)
create_responsive_line(0,1080,1920,1080, fill = "black", width = 50)
create_responsive_line(1920,0,1920,1080, fill = "black", width = 50)
create_responsive_rectangle(30,0,1889,200, fill = "#E42E2E", outline = "black")
create_responsive_rectangle(30,200,1889,850, fill = "#38B342", outline = "black")
create_responsive_rectangle(30,850,1889,1080, fill ="#E42E2E", outline = "black")
create_responsive_line(30,540,1889,540, fill = "white", width = 10)
create_responsive_oval(910, 490, 1010, 590, fill = "white", outline="black", width=5)
canvas_setup.pack(fill="both", expand=True) 
#end of page setup

element_beats = {
    "rock":       ["scissors", "paper", "fire", "air", "void"],
    "paper":      ["rock", "water", "earth", "darkness", "lightning"],
    "scissors":   ["paper", "air", "lightning", "void", "fire"],
    "fire":       ["paper", "scissors", "air", "darkness", "void"],
    "water":      ["fire", "earth", "rock", "void", "lightning"],
    "earth":      ["lightning", "fire", "void", "air", "paper"],
    "air":        ["water", "fire", "paper", "rock", "void"],
    "void":       ["air", "rock", "darkness", "lightning", "earth"],
    "darkness":   ["lightning", "fire", "air", "rock", "water"],
    "lightning":  ["water", "air", "rock", "scissors", "void"]
}
#I admit, I made this part a bit diabolical because the point of this game is to be chaotic; paper can beat rock and rock can beat paper. 

player_score = 0
computer_score = 0
player_hand = [] # used to track whatever 3 cards the player has
current_enemy_choice = None

player_total_wins = 0
player_total_losses = 0
save_file = f"Python/rps/{username}_gamestats.json"


praises = [
    "A truly brilliant move.",
    "DAMN YOU GOT SOME MOVES",
    "BE THE NEXT ELON MUSK!",
    "Wait, you can read minds?!?!",
    "Bro has entered god mode",
    "Enemy: obliberated",
    "Time itself paused to admire your skill",
    "+99999999999 Aura",
    "The enemy sure is comic-sans-level bad",
    "The CPU just filed a resignation letter",
    "Time itself paused to admire your skill",
    "You hacked reality and won",
    "Giga-chad level unlocked",
    "Congratulations, you are now untouchable",
    "The universe bows to your choice",
    "You just wrote the tutorial on winning",
    "Ludicrous skill detected. Warning: do not approach",
    "Your move is being taught in wizard schools",
    "Enemy morale: evaporated",
    "Omega-level strategy achieved",
    "You didn't just win, you redesigned winning",
    "The laws of probability surrender to you",
    "Even your keyboard is sweating",
    "God-tier reflexes. Respect.",
    "CPU sanity: NULL NULL NULL 404ERROR",
    "All opposing pixels spontaneously combusted.",
    "The AI just filed a complaint to the multiverse.",
    "Enemy strategy.exe has stopped working.",
    "Your brain just hacked reality.",
    "Congratulations, you are now the CPU overlord.",
    "Even the firewall applauds your skill.",
    "Next level unlocked: Infinite Domination.",
    "You just broke physics. Again.",
    "The scoreboard weeps in admiration.",
    "Opponent has entered existential meltdown mode.",
    "+∞ IQ detected in player's hands.",
    "All game logic has resigned.",
    "Your mouse is now sentient with pride.",
    "Reality.exe has crashed from awe.",
    "You didn't just win, you altered time itself.",
    "Enemy morale: vaporized into the void.",
    "Giga-chad mode active. Humans obsolete.",
    "All NPCs are worshipping your fingers.",
    "You just taught the universe how to play.",
]

roasts = [
    "You just got existentially canceled.",
    "Even the NPCs are laughing at you.",
    "Congratulations, you just made failure an art form.",
    "Your IQ just filed for early retirement.",
    "Enemy: laughing.exe activated.",
    "You just hit new lows in multiverse standards.",
    "Gravity itself is mocking your attempt.",
    "Even your reflection refuses to acknowledge you.",
    "The universe just sighed in disappointment.",
    "Time just fast-forwarded past your move.",
    "Your strategy has been permanently deleted.",
    "CPU sanity: 0%, despair: 100%.",
    "Congratulations, you are officially a cautionary tale.",
    "Enemy morale? They're dancing on your ruins.",
    "The laws of physics are shaking their heads.",
    "You just got roasted into another dimension.",
    "Even the firewall refused to process that move.",
    "Your keyboard just unplugged itself in shame.",
    "You played the game. And lost existence.",
    "Omega-level failure achieved.",
    "You didn't just lose, you rewrote the definition of losing.",
    "All pixels on screen are crying.",
    "Reality.exe recommends therapy.",
    "Your move is being taught in villain schools… as a warning.",
    "The AI is applauding you… sarcastically.",
    "Enemy strategy.exe is now unemployed thanks to you.",
    "All multiverses just sighed collectively.",
    "Your reflexes just filed a complaint against your body.",
    "Even your mouse is ashamed of your performance.",
    "Congratulations, you just unlocked 'Humiliation: Legendary Edition'.",
    "Your attempt is now a meme in all timelines.",
    "The cosmos just unfollowed you.",
    "You just got ghosted by probability itself.",
    "Every NPC just updated their will to survive.",
    "Your loss has been patented as a weapon of mass embarrassment.",
    "Defeat: maximum DEFCON triggered.",
    "Your fingers have been temporarily banned from existence.",
    "Even the shadows are whispering about your failure.",
    "You didn't just lose, you triggered a universal bug.",
    "Enemy morale: laughing hysterically at your expense.",
    "Congratulations… you just became lore for how not to play.",
    "The game just filed harassment charges against you.",
    "All elements involved demand a refund.",
    "You've just broken the leaderboard… downwards.",
    "Your loss has caused a minor singularity.",
    "Even the AI is crying silently in shame."
    "EVEN MY DEAD GRANDMA WILL DO BETTER!"
    "Your IQ: comic-sans"
    "You just got CHONGd"
]

brutal_roasts = [
     "You just got erased from the multiverse.",
    "Congratulations, your existence is now optional.",
    "Even reality itself logged off in shame.",
    "The universe just filed a restraining order against you.",
    "All timelines now consider you a bug.",
    "Your soul has been demoted to spectator mode.",
    "Every particle near you just unfriended you.",
    "You didn't lose… you were uninstalled from existence.",
    "Omega-level obliteration achieved. Humanity disappointed.",
    "Time itself just reset to forget your move.",
    "Your defeat just caused entropy to smile.",
    "Even the AI mourns the tragedy of your life choices.",
    "Your loss is now a cautionary tale in seven galaxies.",
    "The scoreboard just self-destructed out of pity.",
    "You became the reason NPCs panic on sight.",
    "All energy in this dimension just left your body.",
    "Enemy strategy.exe cried itself into a new universe.",
    "Your name has been blacklisted by reality.",
    "Even the dead are whispering 'why'.",
    "Congratulations… you broke the concept of winning forever.",
    "Every law of probability just sighed and quit.",
    "The cosmos has issued a formal apology for your attempt.",
    "Your loss unlocked the 'existential dread' achievement.",
    "Even the shadows are weeping for your failure.",
    "You didn't just lose, you caused a minor singularity of shame.",
    "All elements involved have resigned in despair.",
    "Your failure has become a permanent glitch in the multiverse.",
    "Omega-level disgrace recorded. Do not attempt again.",
    "The fabric of reality just filed harassment charges.",
    "You are now a universal cautionary tale: 'How Not to Play'.",
    "All nearby NPCs are now traumatized beyond repair.",
    "Your defeat will echo until the heat death of the universe."
    "YOUR SKILL IS BANNED IN 12 PARALLEL UNIVERSES, ONE OF THEM IS THE 'Chongverse'"
]

def save_data():
    if username == "Guest":
        return
    data = {"total_wins": player_total_wins, "total_losses": player_total_losses}
    with open(save_file, 'w') as f:
        json.dump(data, f)

def load_stats():
    global player_total_wins, player_total_losses

    if username == "Guest":
        player_total_wins = 0
        player_total_losses = 0
        return
    try:
        with open(save_file, "r") as f:
            data = json.load(f)
            player_total_wins = data.get("total_wins", 0)
            player_total_losses = data.get("total_losses", 0)
    except (FileNotFoundError, json.JSONDecodeError, IOError):
        player_total_wins = 0
        player_total_losses = 0

#start of game initialisation of widgets"
big_label = Label(game_window, text = "Anarchy Rock, Paper, Scissors", font = ("MS Serif", 50), padx = 20, pady = 20, relief = RAISED, bd = 10, fg = "#141FEC", bg = "#B63D57")
big_label.place(relx = 0.5, rely = 0.1, anchor = CENTER)
small_label = Label(game_window, text = "A game where hopes, peace and friendship disintergrates", font = ("MS Serif", 20), padx = 20, pady = 20, relief = RAISED, bd = 10, fg = "#141FEC", bg = "#B63D57")
small_label.place(relx = 0.5, rely = 0.25, anchor = CENTER)
exit_button = Button(game_window, text = "Exit", font = ("MS Serif", 20), padx = 10, pady = 10, bd = 5, fg = "#E33D2B", bg = "#3F28EE", activebackground="#334EC4", activeforeground="#D71F47", relief = RAISED, height = 2, width = 10, command = lambda: ( game_window.destroy(), subprocess.Popen(["python3", "Python/gameselection.py", username ])))
exit_button.place(relx = 0.2, rely = 0.9, anchor = CENTER)
play_button = Button(game_window, text = "Play", font = ("MS Serif", 20), padx = 10, pady = 10, bd = 5, fg = "#E33D2B", bg = "#3F28EE", activebackground="#334EC4", activeforeground="#D71F47", relief = RAISED, height = 2, width = 10, command = lambda: print('play game'))
play_button.place(relx = 0.4, rely = 0.9, anchor = CENTER)
rules_button = Button(game_window, text = "How to play", font = ("MS Serif", 20), padx = 10, pady = 10, bd = 5, fg = "#E33D2B", bg = "#3F28EE",activebackground="#334EC4", activeforeground="#D71F47", relief = RAISED, height = 2, width = 10, command = lambda: (game_window.destroy(), subprocess.Popen(["python3", "rps_rules.py", username])))
rules_button.place(relx = 0.6, rely = 0.9, anchor = CENTER)
galore_button = Button(game_window, text = "Card Galore", font = ("MS Serif", 30), padx = 10, pady = 10, bd = 5, fg = "#E33D2B", bg = "#3F28EE", activebackground="#334EC4", activeforeground="#D71F47", relief = RAISED, height = 2, width = 10, command = lambda: (game_window.destroy(), subprocess.Popen(["python3", "rps_galore.py", username])))
galore_button.place(relx = 0.8, rely = 0.9, anchor = CENTER)
account_label = Label(game_window, text = f"Current account: {username}", font = ("MS Serif", 30),padx = 10, pady = 10, bd = 5, )
account_label.place(relx = 0.5, rely =0.35, anchor = CENTER)

player_score_label = Label(game_window, text="Player: 0", font=("MS Serif", 20), bg="#E42E2E", fg="white")
computer_score_label = Label(game_window, text="Computer: 0", font=("MS Serif", 20), bg="#E42E2E", fg="white")
result_label = Label(game_window, text="", font=("MS Serif", 30), bg="#38B342", fg="white")
enemy_card_label = Label(game_window, text="???", font=("MS Serif", 30), height=2, width=15, relief=RAISED, bd=5, fg = "black", bg = "#53C8DF")

element_button_data = {
    "rock": "THE ROCK 🪨", "paper": "The Paper 🧾", "scissors": "The Scissors ✂️",
    "fire": "The Fire 🔥", "water": "The Water 💧", "earth": "The Earth 🌍",
    "air": "The Air 💨", "void": "The Void ⚫", "darkness": "The Darkness 🔮",
    "lightning": "The Lightning ⚡"
}

all_element_buttons = {}
for name, text, in element_button_data.items(): #take each key and value in the dictionary
    button = Button(game_window, text=text, font=("MS Serif", 30), height=2, fg="#000000", bg="#3F28EE") #makes a button out of each key/value pair
    all_element_buttons[name] = button #add the buttons to the dictionary with elements as the key

play_again_button = Button(game_window, text="Play Again", font=("MS Serif", 20), fg = "black", bg = "#EC6A6A", padx = 20, pady = 20, bd = 5, activebackground="#334EC4", activeforeground="#D71F47")
main_menu_button = Button(game_window, text="Main Menu", font=("MS Serif", 20), fg = "black", bg = "#EC6A6A", padx = 20, pady = 20, bd = 5, activebackground="#334EC4", activeforeground="#D71F47")

def start_round():
    global player_hand, player_score, computer_score, current_enemy_choice
    #the system keeps drawing until there is a valid combination of hands.
    while True:
        all_elements = list(element_beats.keys()) #take the keys from the dictionary, chuck it in a list
        current_enemy_choice = random.choice(all_elements)
        chosen_elements = random.sample(all_elements, 3) #use sample to prevent duplicates
        winning_cards_in_hand = []
        #loops through the player's hand
        for player_card in chosen_elements:
            #checks if the player's card beats the computer's card
            player_wins = current_enemy_choice in element_beats[player_card]
            #now do it the other way
            enemy_wins = player_card in element_beats[current_enemy_choice]
            #checks for a combination where only the player wins
            if player_wins and not enemy_wins:
                winning_cards_in_hand.append(player_card)
        if len(winning_cards_in_hand) == 1: #checks that there is only one way to win
            break
    #check if the user came from the main menu
    if play_button.winfo_ismapped():
        player_score = 0
        computer_score = 0
        
    player_score_label.config(text=f"Player: {player_score}"); computer_score_label.config(text=f"Computer: {computer_score}")
    player_score_label.place(relx = 0.2, rely = 0.2, anchor = CENTER)
    computer_score_label.place(relx = 0.8, rely = 0.2, anchor = CENTER)

    big_label.place_forget(); small_label.place_forget(); play_button.place_forget(); exit_button.place_forget()
    rules_button.place_forget(); galore_button.place_forget(); result_label.place_forget()
    play_again_button.place_forget(); main_menu_button.place_forget(); account_label.place_forget()

    enemy_card_label.config(text="???")
    enemy_card_label.place(relx=0.5, rely=0.4, anchor=CENTER)

    #gets the buttons of the player's stuff and global them from the draw
    player_hand = [all_element_buttons[name] for name in chosen_elements]
    #set up their positions
    button_positions = [{'relx': 0.3, 'rely': 0.9, 'anchor': CENTER}, {'relx': 0.5, 'rely': 0.9, 'anchor': CENTER}, {'relx': 0.7, 'rely': 0.9, 'anchor': CENTER}]
    for i, element_name in enumerate(chosen_elements): #iterate it so they everything has a index and a value on a enumerate item
        #gets the button that corrosponds to widget name
        button = all_element_buttons[element_name]
        button.config(command=lambda choice=element_name: play_turn(choice))
        button.place(**button_positions[i])

def play_turn(player_choice):
    global player_hand
    for button in player_hand:
        button_text_parts = (button.cget("text")).split(" ") #takes value of widget using cget and takes the element's name from text
        element_name = (button_text_parts[1]).lower() #since split gives a list, just take the second part and use that as the name.
        if element_name == player_choice: #check if button is the one that the player clicked
            button.place(relx=0.5, rely=rely(800), anchor=CENTER) #move it to the lower green area
        else:
            button.place_forget()
    game_window.after(1000, lambda: reveal_enemy_card(player_choice))

def reveal_enemy_card(player_choice):
    global current_enemy_choice
    enemy_card_text = element_button_data[current_enemy_choice] #gets the enemy card name
    enemy_card_label.config(text=enemy_card_text)
    game_window.after(1000, lambda: show_round_result(player_choice))

def show_round_result(player_choice):
    global player_score, computer_score, current_enemy_choice
    #checks if player wins
    player_wins = current_enemy_choice in element_beats[player_choice]
    if player_wins:
        player_score += 1
        round_message = random.choice(praises) #picks a random praise
    else:
        computer_score += 1
        round_message = random.choice(roasts) #picks a random roast
    result_label.place(relx=0.5, rely=0.5, anchor=CENTER)
    result_label.config(text=round_message)
    player_score_label.config(text=f"Player: {player_score}")
    computer_score_label.config(text=f"Computer: {computer_score}")
    game_window.after(3000, check_game_over)

def check_game_over():
    global player_total_wins, player_total_losses
    for button in player_hand:
        button.place_forget()
    enemy_card_label.place_forget()
# does everything based on who won, or start a new round if its unsettled
    if player_score >= 3:
        player_total_wins += 1
        result_label.config(text=f"You Win! Final Score: {player_score} - {computer_score}")
        play_again_button.place(relx=0.4, rely=0.7, anchor=CENTER)
        main_menu_button.place(relx=0.6, rely=0.7, anchor=CENTER)

    elif computer_score >= 3:
        player_total_losses += 1
        final_message = f"You Lose! Final Score: {player_score} - {computer_score}"
        brutal_roast = random.choice(brutal_roasts)
        result_label.config(text=f"{final_message}\n{brutal_roast}")
        play_again_button.place(relx=0.4, rely=0.7, anchor=CENTER)
        main_menu_button.place(relx=0.6, rely=0.7, anchor=CENTER)
    else:
        start_round()

def play_again():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    start_round()

def show_main_menu():
    save_data()
    play_again_button.place_forget(); main_menu_button.place_forget(); result_label.place_forget()
    player_score_label.place_forget(); computer_score_label.place_forget(); enemy_card_label.place_forget()
    for button in player_hand:
        button.place_forget()
    big_label.place(relx=0.5, rely=0.1, anchor=CENTER)
    small_label.place(relx=0.5, rely=0.25, anchor=CENTER)
    account_label.place(relx=0.5, rely=0.35, anchor=CENTER)
    exit_button.place(relx=0.2, rely=0.9, anchor=CENTER)
    play_button.place(relx=0.4, rely=0.9, anchor=CENTER)
    rules_button.place(relx=0.6, rely=0.9, anchor=CENTER)
    galore_button.place(relx=0.8, rely=0.9, anchor=CENTER)

play_again_button.config(command=play_again)
main_menu_button.config(command=show_main_menu)
play_button.config(command=start_round)
exit_button.config(command=lambda: (save_data(), game_window.destroy(), subprocess.Popen(["python3", "Python/gameselection.py", username])))
rules_button.config(command=lambda: (save_data(), game_window.destroy(), subprocess.Popen(["python3", "rps_rules.py", username])))
galore_button.config(command=lambda: (save_data(), game_window.destroy(), subprocess.Popen(["python3", "rps_galore.py", username])))

load_stats()
show_main_menu()

game_window.mainloop()