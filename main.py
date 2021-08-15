# This is button a function. It starts a 60 second countdown.

def on_button_pressed_a():
    game.start_countdown(60000)
input.on_button_pressed(Button.A, on_button_pressed_a)

# This is the logo up fuction. It choses a random item from the list, displays its string, and removes it from the list for one round.

def on_gesture_logo_up():
    global Index
    Index = randint(0, len(text_list))
    basic.show_string("" + (text_list[Index]))
    text_list.remove_at(Index)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

# This is the screen down fuction. It adds a point to the score indicating the guess was correct.

def on_gesture_screen_down():
    game.add_score(1)
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

# This is button b function. It starts a 120 second coundown.

def on_button_pressed_b():
    game.start_countdown(120000)
input.on_button_pressed(Button.B, on_button_pressed_b)

# This is starting the game. It sets the score to 0, creates a list of things to act out, and shows the time for each button.
Index = 0
text_list: List[str] = []
game.set_score(0)
text_list = ["Dog",
    "Cat",
    "Airplane",
    "Haircut",
    "Chew",
    "Think",
    "Run",
    "Golf",
    "Slap",
    "Monkey",
    "Fish",
    "Snake",
    "Skate",
    "Yoga",
    "Rini",
    "Stuti",
    "Navya",
    "Viva (THE GREAT)",
    "Harry Potter",
    "Peeta Mellark",
    "Ice Cream",
    "Alex Russo",
    "Frozen",
    "Olympics",
    "DDLJ",
    "Joey Rooney",
    "Pant",
    "Fall",
    "Dora",
    "Cake",
    "Gum",
    "Car",
    "Mosquito",
    "Sloth",
    "Hopscotch",
    "TV",
    "Text",
    "Sleep",
    "Brush",
    "Teacher",
    "Exercise",
    "Die",
    "Slip",
    "Pizza",
    "Burger",
    "Water",
    "Sky",
    "Squishy",
    "Fart",
    "Bored",
    "Robot",
    "Punch",
    "Ring",
    "Pig",
    "Square",
    "Stare",
    "River",
    "Scratch",
    "Dance",
    "Fight",
    "Whine",
    "Baby",
    "Shock",
    "Shop",
    "Count",
    "Wait",
    "Jump",
    "Billy La Bufanda",
    "Barbie",
    "Bitmoji",
    "GamePigeon",
    "Potato",
    "Boogalee!!"]
basic.show_string("A=60sec B=120sec")