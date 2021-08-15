// This is button a function. It starts a 60 second countdown.
input.onButtonPressed(Button.A, function () {
    game.startCountdown(60000)
})
// This is the logo up fuction. It choses a random item from the list, displays its string, and removes it from the list for one round.
input.onGesture(Gesture.LogoUp, function () {
    Index = randint(0, text_list.length)
    basic.showString("" + (text_list[Index]))
    text_list.removeAt(Index)
})
// This is the screen down fuction. It adds a point to the score indicating the guess was correct.
input.onGesture(Gesture.ScreenDown, function () {
    game.addScore(1)
})
// This is button b function. It starts a 120 second coundown.
input.onButtonPressed(Button.B, function () {
    game.startCountdown(120000)
})
// This is starting the game. It sets the score to 0, creates a list of things to act out, and shows the time for each button.
let Index = 0
let text_list: string[] = []
game.setScore(0)
text_list = [
"Dog",
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
"Boogalee!!"
]
basic.showString("A=60sec B=120sec")
