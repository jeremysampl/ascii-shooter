'''
Author: Jeremy Sampl

* MUST BE RUN ON CMD OR POWERSHELL TO PLAY GAME AT THE END (IDLE DOES NOT PRINT PROPERLY) *
* RUN ON POWERSHELL FOR BEST EXPERIENCE *
* ENTER 'py ' + FILE LOCATION (ex: 'py C:\\Users\\Jerem\\Documents\\Python\\TerraExodus2122.py') *

* ALL ASCII ART WAS MADE BY MYSELF WITH OCCASIONAL INSPIRATION FROM OTHER ASCII ART OR IMAGES *

Using ASCII art, this program takes in user input to display a story seemingly controlled by the user.
Every choice is recorded and used later which allows customization for the game at the end.
At the end, the user gets to play a game that uses all the options the user selected.

The goal of the game:
- Defeat all enemies of the user's choosing using the plane and weapons chosen by the user as well.
- The enemies will attempt to drop bombs in order to defeat the player, which will damage the plane.
- If the player's plane's health falls below or at 0, the player loses and may play again.
- However, if the player defeats all enemies, the player wins.
'''

# Imports
from time import *
from os import *
from random import *
from msvcrt import *

# Declare variables
minScreenHeight = 30
minScreenWidth = minScreenHeight * 2
maxScreenHeight = 100
maxScreenWidth = maxScreenHeight * 2
screenHeight = 50
screenWidth = screenHeight * 2
screen = [[" " for _ in range(screenWidth)] for _ in range(screenHeight)]
collisions = [[" " for _ in range(screenWidth)] for _ in range(screenHeight)]

title = ["Welcome to Terra Exodus: 2122!",
         "The year is 2122 and it has been decades since 'The Event'.",
         "You're one of the only survivors of the nuclear blasts that nearly destroyed the planet.",
         "However, there has been a recent discovery that a massive asteroid is headed to Earth and will surely cause human extinction.",
         "You need to leave NOW. Find a plane, fix it up, and fit it with some weapons... y'know just in case.",
         "Good thing there is an old abandoned military facility nearby. Go there to find your supplies.",
         "Good luck on your adventures!"]

menuInstructions = ["'W' - UP | 'A' - LEFT | 'S' - DOWN | 'D' - RIGHT",
                    "Type in any of the letters above to increase/decrease screen width/height.",
                    "Default screen size works great, but increase screen size for more room.",
                    "Smaller screen size may result in harder difficulty and vice-versa.",
                    "Press 'ENTER' to start."]

controls = "'W' - UP | 'A' - LEFT | 'S' - DOWN | 'D' - RIGHT | 'SPACE' - SHOOT"

story = [[ "_________________________________",
          "|       _   _             _       |",
          "|   ^  |_| |_  ^         |_  /|   |",
          "|  /-\ | \ |_ /-\         _| _|_  |",
          "|  _____________________________  |",
          "| |                             | |",
          "| |             -|-             | |",
          "| |          __ _|_ __          | |",
          "| |            /___\            | |",
          "| |     .------|/|\|------.     | |",
          "| |      `'O-O-\___/-O-O'`      | |",
          "|_|__________000___000__________|_|"],
         ["  _____________                _______  ",
          " |\____________\              |\______\ ",
          " ||.----.|.----.|             || A-103 |",
          " |||    |||    ||             || .---. |",
          " \||____|||____|| -----+----- \|_|___|_|",           
          "     _             ___|_|___          __",
          "   _/_\_ ___     _/| |   |  |________/_/",
          "  /_+_+_\---'   (    |___|   ________x/ ",
          " |_______|      `--_________/           ",
          "(O_o_o_o_O)         _|___|_             "],
         [          "_____",
                ",-'`\_\) `'-,", 
              ".'|  . ,`  . (/'.",
             "/ (  _ /     ,'`' \\",
          "  |   \( `'    ( _,-. | ,",
      "      |    \\\..    '~__','| ~~ ->",
          "  |    (   `,   (_ `, | `",
             "\    | .'      ) |/",
              "`.  |/        `.'",
                "`'-._____.-'`"],
         [                 "_____",
                    "___----     ----___",
                ",-'`                   `'-,", 
              ".'                           '.",
             "/   /`:._  _____ _____  _.:`\   \\",
            "|   /  /  /|     |  _  |\  \  \   |",
            "|  /  /  / |     |\(ü)/| \  \  \  |",
           "|  (__/__/_/|_____|__|__|\_\__\__)  |",
           "|            `-._____.-`            |",
          "|                                     |",
          "|               .-----.               |",
          "|             .'       '.             |",
           "|           |           |           |",
           "|           |           |           |",
            "|           `,       ,`           |",
            "|             `-----`             |",
             "\                               /",
              "`.                           .'",
                "`'-.___             ___.-'`",
                       "----_____----"]]

storyText = [["You made it to Area 51!",
              "This used to be one of the most well-known American military facilities.",
              "Some said it contained aliens, while others said this is where the government tested its most sophisticated equipment at the time.",
              "Either way, go found out for yourself!"],
             ["Keep looking around. You're going to need to find lots of supplies to get the plane in running condition.",
              "Perhaps there is a storage facility for spare equipment and vehicle parts.",
              "Keep an eye out for weapons specifically as you will need them. Trust me."],
             ["Lift-off!",
              "You scrapped together enough to get the plane off the ground and hopefully safely exit the Earth's atmosphere.",
              "Now steer your plane to wherever your heart desires. There are infinite possibilities in space."],
             ["Miraculously, the plane has successfully entered the planet's atmosphere without burning up.",
              "Looks like you did an excellent job at repairing the plane.",
              "It should be relatively smooth sailing from now on. Congratulations."],
             ["Press 'ENTER' to continue."]]

choices = []

choicesText = [["You found some planes!",
               "They might need a little bit of work, but they should all work just fine... hopefully anyways.",
               "Take your pick!"],
              ["You came across some weapons!",
               "They may not all be designed for planes, but I'm sure you can make it work.",
               "Well, what are you waiting for? We don't have much time left."],
              ["Alright, here's the thing. The plane doesn't have much fuel left.",
               "You're going to have to land at a nearby planet. I have located 3 of the closest for you.",
               "They're all dangerous in their own way, so it's completely up to you."],
              ["Oh no, you've been surrounded by enemies! You're going to have to choose to fight one of them!",
               "I'd say they're all equally as difficult, so don't overthink it!"]]

choiceInstructions = ["Enter '1', '2', or '3' (left to right) to select your choice.",
                      "To confirm your choice, press 'ENTER'."]

planet = [[         "_____",
                ",-'` o   `'-,", 
              ".'          o  '.",
             "/   o  o  o       \\",
            "|  o            o   |",
            "|      o  o  o      |",
            "|           o   o   |",
             "\  o    o     o   /",
              "`.        o    .'",
                "`'-._____.-'`"],
           [        "_____",
                ",-'`_    `'-,", 
              ".'   /_)       '.",
             "/       \_  _  __ \\",
            "|  (\    ( |//  | ) |",
            "|   \)    \_|   |/  |",
            "|      /\_   |\_    |",
             "\    |_  )   \_)  /",
              "`.    (/       .'",
                "`'-._____.-'`"],
           [        "_____",
                ",-'`    ;`'-,", 
              ".'  ~   ,    ` '.",
             "/ .   -.  ,  .    \\",
            "|     '         .   |",
            "|   `     -   :   ` |",
            "| `   0       .     |",
             "\  '    `  '   ,  /",
              "`.    -      . .'",
                "`'-._____.-'`"]]

planetText = [["Planet Xenos! You'll be flabbergasted- Hmmm... poor choice of words.",
               "It may look slick, but it is completely filled with poisoneous gas.",
               "Just to be clear, that means the gas is deadly. Really DEADLY.",
               "However, the plane should protect you... assuming you assembled it correctly."],
              ["Planet Glacio! I've heard this planet is pretty cool- literally.",
               "As the name suggests, it is full of glaciers and is the coldest planet.",
               "It also filled with many deep vallies... Who knows what may lurk down there.",
               "As long as you built the plane properly, it should resist the cold... hopefully."],
              ["Planet Aris! Sounds very similar to a word I know...",
               "Well, it contains slightly more water than the Sahara Desert, if that's something...",
               "Don't worry though, it's relatively cold compared to the core of the sun.",
               "Constructed well, the plane could possibly handle the heat. No promises, though."]]

plane = []

planeText = [["Ah, the B-2 Spirit! Excellent choice!",
              "These high-tech planes were some of the best stealth bombers of their time.",
              "This one shouldn't need too many repairs, but some extra firepower wouldn't hurt."],
             ["The SR-71 Blackbird. An oldie but a goodie!",
              "Built in the 1960s, these planes remained relevant going into the 21st century.",
              "Designed for reconnaissance, but could possibly be modified to accommodate a space flight."],
             ["A passenger plane!? You do realize you're going in space, right??",
              "Well, better get working on it because it's going to need a lot.",
              "Try not to overload it, though. These planes are not meant to carry lots of weight."]]

missile = []

weapon = []

weaponText = [["A light, fast firing, high-powered mounted machine gun.",
                "This should be able to spray down any enemies you may encounter."],
               ["An aircraft-fitted missile launcher!",
                "This bad boy should have no trouble obliterating any enemies that come near."],
               ["Double aircraft-fitted missile launchers!",
                "You know what they say, two is always better than one. The more firepower, the better."]]

bomb = ["___",
        "\|/",
        "(_)"]

enemy = []

enemyText = [["Aliens! Specifically, the B-402 branch.",
              "This species of aliens can be extremely protective of their territory. Use this to your advantage.",
              "However, this also means that they will do whatever is necessary to defend themselves. Be careful."],
             ["Aliens! These ones are named after their cupcake-shaped aircrafts.",
              "They are some of the least dangerous known aliens, which should give you some relief at least.",
              "However, this does not mean you can just lay back. Get in there and fight!"],
             ["Is that a military plane?? I was expecting some aliens. But at least you now know you're not alone...",
              "However, they do not look peaceful. You're going to have to fight through them.",
              "Clearly they don't want you getting whatever is on that planet. Find out what it is."]]

explosion = [["*"],
             [ "^",
              "<*>",
               "v"],
             [ "-^-",
              "<-*->",
               "-v-"], 
             ["' . '",
              "- : -",
              ", . ,"]]
                  

particles = [["\u00b0", "0", "o", "O"],
             ["/", "\\", "_", "(", ")", "|"],
             [",", ".", "'", "`", "~", "-", "*", ";", ":"]]

wonText = ["Congratulations!"
           "You successfully beat the enemies and made it to safety on the chosen planet!",
           "Would you like to play again? ('1' - YES | '2' - NO)"]

gameOver = [[" ________   _________   __     __   ______ ",
             "|        | |   ___   | |  |___|  | |   ___|",
             "|  ,-----' |  |   |  | |         | |  |___ ",
             "|  | ____  |  |___|  | |   ___   | |      |",
             "|  ||_   | |   ___   | |  |   |  | |  ,---'",
             "|  |__|  | |  |   |  | |  |   |  | |  '---,",
             "|________| |__|   |__| |__|   |__| |______|",
             " ________   __     __    ______    _______ ",
             "|        | |  |   |  |  |   ___|  |  ____ |",
             "|  ____  | |  |   |  |  |  |___   | |    ||",
             "| |    | | |  |   |  |  |      |  | |____||",
             "| |____| | |  |___|  |  |  ,---'  |   __  |",
             "|        | |         |  |  '---,  |  |  | |",
             "|________| |_________|  |______|  |__|  |_|"],
            [" __    __   _________   __     __  ",
             "|  |  |  | |         | |  |   |  | ",
             "|  |  |  | |  _____  | |  |   |  | ",
             "|  |__|  | | |     | | |  |   |  | ",
             "|__    __| | |_____| | |  |___|  | ",
             "   |  |    |         | |         | ",
             "   |__|    |_________| |_________| ",
             " __  __  __   _______   ______  __ ",
             "|  ||  ||  | |       | |      ||  |",
             "|  ||  ||  | '--, ,--' |  ||  ||  |",
             "|  ||  ||  |    | |    |  ||  ||  |",
             "|  ||  ||  |    | |    |  ||  ||  |",
             "|          | ,--' '--, |  ||  ||  |",
             "|__________| |_______| |__||______|"]]

gameOverText = [["You were defeated!",
                 "Input '1' to try again or '2' to quit."],
                ["Congratulations! You successfully destroyed the enemies.",
                 "You have safely made it on the planet. On to the next adventure!",
                 "Input '1' to play again or '2' to quit."]]

maxLength = []

entities = []
explosions = []
planetParticles = []
missileLocation = []
playAgain = True
playing = False
choosing = True
inMenu = True
won = False
missileTime = time()
missileDelay = int()
enemiesRemaining = int()
health = int()
startTime = time()
timeSeconds = int()
timeMinutes = int()
planeMinimumY = 10
storyCount = int()

'''
Function that initializes certain variables needing to be reset if the user would like to play again.
'''
def initializeVariables():
    # Declare global variables
    global choices, entities, explosions, planetParticles, missileLocation, playAgain, playing, choosing, inMenu, won, missileDelay, enemiesRemaining, health, timeSeconds, timeMinutes, storyCount, enemy, plane, missile, weapon, maxLength

    #Initialize variables
    choices = []
    entities = []
    explosions = []
    planetParticles = []
    missileLocation = []
    playAgain = True
    playing = False
    choosing = True
    inMenu = True
    won = False
    missileDelay = 1.5
    enemiesRemaining = randint(15, 30)
    health = 100
    timeSeconds = 0
    timeMinutes = 0
    storyCount = 0

    enemy = [[     "___",
               "___/ ^ \___",
              "/ - - - - - \\",
              "'--_______--'"],
             [    ".-'-.",
               "_.'-----'._",
              "(___________)",
                 "\_____/"],
         [        "-|-",
               "__ _|_ __",
                 "/___\\",
          ".------|/|\|------.",
           "`'O-O-\___/-O-O'`"]]

    weapon = [[  "_ _",
                 "| |",
                 "| |",
                 "| |",
                "/ + \\",
                "|   |",
               "/  +  \\",
              "(-------)",
               "\_____/"],
          [   "^",
             "/ \\",
             "| |",
             "| |",
            "/ + \\",
            "| + |",
            "| + |",
           "/ ___ \\",
           "|/***\|"],
          [   "^       ^",
             "/ \     / \\",
             "| |     | |",
             "| |     | |",
            "/ + \   / + \\",
            "| + |   | + |",
            "| + |   | + |",
           "/ ___ \ / ___ \\",
           "|/***\| |/***\|"]]

    missile = [["|"],
               ["^",
                "|"]]

    plane = [[        "^",
                     "/_\\",
                    "//_\\\\",
                   "/     \\",
                 "_/ /| |\ \_",
                "|/ |_| |_| \|",
                "/           \\" ,
               "/             \\",
              "/               \\",
             "/ _  _       _  _ \\",
             "\/ /\ /\   /\ /\ \/",
             " \/  V  \ /  V  \/",
                      "'"],
        [    "|",
            ".^.",
            "| |",
            "| |",
            "| |",
         "/\/   \/\\",
         "|   |   |",
        "/|   |   |\\",
        "-|_| | |_|-",
            "'V'"],
         [       "_",
               "./_\\.",
               "|' '|",
               "|   |",
            "_  |   |  _",
         "__|_|_|   |_|_|__",
        "/      |   |      \\",
       "'-------|   |-------'",
               "|   |",
              "_|_|_|_",
             "/_______\\",
                "\_/"]]

    maxLength = [[len(plane[0][9]), len(plane[1][7]), len(plane[2][7])],
                 [len(weapon[0][7]), len(weapon[1][7]), len(weapon[2][7])],
                 [len(planet[0][5]) for _ in range(3)],
                 [len(enemy[0][2]), len(enemy[1][2]), len(enemy[2][3])]]

########################

'''
Main function that controls the entire game through other functions
'''
def main():
    # Declare global variables
    global choosing, playing, startTime

    while playAgain:
        initializeVariables()
        menu()
        system('cls')
        displayScreen()
        keyboardInputLoop()
        choosing = True

        # For loop going through every choice
        for i in range(len(maxLength)):
            clearScreen()
            displayStory()
            displayScreen()
            input()
            clearScreen()
            displayChoice(i)
            displayScreen()
            keyboardInputLoop()
            clearScreen()
            displaySelectedChoice(i, choices[i])
            displayScreen()
            input()

        # One-time necessary operations
        confirmChoices()
        spawnPlane()
        spawnEnemy()
        startTime = time()
        playing = True

        # Playing loop to continue to update the screen while playing (~15 times per second)
        while playing:
            checkKeyboardInput()
            checkSpecialEntities()
            clearScreen()
            updateEntities()
            updateExplosions()
            showParticles()
            displayScreen()
            displayGameInfo()

        # Calls the end of the game
        gameEnd()

#########################################################################################################################################################################################

'''
Function that controls the appearance of the menu.
- Formats and centres the text to the proper position, relative to the screen size.
'''
def menu():
    # Reformats title in order to display properly in the selected screen size
    formattedTitle = formatText(title)
    # Prints title in center of screen
    titleY = int(screenHeight / 2) - int(len(formattedTitle) / 2)
    for y in range(len(formattedTitle)):
        titleX = int(screenWidth / 2) - int(len(formattedTitle[y]) / 2)
        for x in range(len(formattedTitle[y])):
            screen[titleY + y][titleX + x] = formattedTitle[y][x]

    # Reformats menu instructions in order to display properly in the selected screen size
    formattedInstructions = formatText(menuInstructions)
    # Prints menu instructions near bottom centre of the screen
    controlsY = screenHeight - int(screenHeight / 15) - len(formattedInstructions)
    for y in range(len(formattedInstructions)):
        controlsX = int(screenWidth / 2) - int(len(formattedInstructions[y]) / 2)
        for x in range(len(formattedInstructions[y])):
            screen[controlsY + y][controlsX + x] = formattedInstructions[y][x]

'''
Function that displays the storyline.
- Formats and centres text based on the screen size.
- Uses uniquely designed ASCII art to help visualize the story.
'''
def displayStory():
    # Declare global variable
    global storyCount

    # Prints the ASCII art for the storyline in the centre top of the screen
    offsetY = 1
    for y in range(len(story[storyCount])):
        offsetX = int(screenWidth / 2) - int(len(story[storyCount][y]) / 2)
        for x in range(len(story[storyCount][y])):
            screen[offsetY + y][offsetX + x] = story[storyCount][y][x]

    # Formats the text for the screen size and prints the storyline near the bottom centre of the screen
    formattedStory = formatText(storyText[storyCount])
    formattedStory.append(storyText[len(storyText) - 1][0])
    offsetY = screenHeight - len(formattedStory)
    for y in range(len(formattedStory)):
        offsetX = int(screenWidth / 2) - int(len(formattedStory[y]) / 2)
        for x in range(len(formattedStory[y])):
            screen[offsetY + y][offsetX + x] = formattedStory[y][x]

    # Keeps count of which part of the storyline is to be displayed
    storyCount += 1

'''
Function that takes in the index (number) of the choice and displays it to the user.

'''
def displayChoice(choiceIndex):
    # Declare global variable and resets the boolean to true
    global choosing
    choosing = True

    # Obtains the name of the choice from a seperate function (used in multiple areas)
    choiceName = getChoiceName(choiceIndex)

    # Displays all three ASCII art visuals for each option
    for i in range(3):
        # Sets the X value depending on which one is being printed (left, centred, right)
        startX = 3
        if i == 1:
            startX = int(screenWidth / 2) - int(maxLength[choiceIndex][i] / 2)
        elif i == 2:
            startX = screenWidth - maxLength[choiceIndex][i] - 4
            
        # Obtains the vertical and horizontal lengths of the objects in order to display properly
        # Character by character, adds to the screen to be printed afterwards
        exec("verticalLength = len(%s[i])" % choiceName, locals(), globals())
        for y in range(verticalLength):
            exec("horizontalLength = len(%s[i][y])" % choiceName, locals(), globals())
            offsetX = startX + int((maxLength[choiceIndex][i] - horizontalLength) / 2)
            for x in range(horizontalLength):
                exec("screen[3 + y][offsetX + x] = %s[i][y][x]" % choiceName, locals(), globals())

    # Formats the text of the choice that has to be made and embeds in the screen to be printed later
    choicesText[choiceIndex] = formatText(choicesText[choiceIndex])
    offsetY = int(screenHeight / 1.5) - int(len(choicesText[choiceIndex]) / 2)
    for y in range(len(choicesText[choiceIndex])):
        offsetX = int(screenWidth / 2) - int(len(choicesText[choiceIndex][y]) / 2)
        for x in range(len(choicesText[choiceIndex][y])):
            screen[offsetY + y][offsetX + x] = choicesText[choiceIndex][y][x]

    # Formats and centres the instructions for selecting an option to be printed later
    formattedInstructions = formatText(choiceInstructions)
    offsetY = screenHeight - len(formattedInstructions)
    for y in range(len(formattedInstructions)):
        offsetX = int(screenWidth / 2) - int(len(formattedInstructions[y]) / 2)
        for x in range(len(formattedInstructions[y])):
            screen[offsetY + y][offsetX + x] = formattedInstructions[y][x]

'''
Function that takes in the choice being made and the user's selected choice to display it.
'''
def displaySelectedChoice(choiceIndex, choiceNumber):
    # Obtains the name of the choice from a seperate function (used in multiple areas)
    choiceName = getChoiceName(choiceIndex)

    # Sets and centres the choice's associated ASCII art to be displayed later
    offsetY = int(screenHeight / 2) - int(maxLength[choiceIndex][choiceNumber] / 2)
    exec("lengthY = len(%s[choiceNumber])" % choiceName, locals(), globals())
    for y in range(lengthY):
        exec("lengthX = len(%s[choiceNumber][y])" % choiceName, locals(), globals())
        offsetX = int(screenWidth / 2) - int(lengthX / 2)
        for x in range(lengthX):
            exec("screen[offsetY + y][offsetX + x] = %s[choiceNumber][y][x]" % choiceName, locals(), globals())

    # Formats, sets and centres the text associated with the user's choice in the storyline
    exec("formattedText = formatText(%sText[choiceNumber])" % choiceName, locals(), globals())
    formattedText.append("Press 'ENTER' to continue.")
    textY = screenHeight - len(formattedText)
    for y in range(len(formattedText)):
        textX = int(screenWidth / 2) - int(len(formattedText[y]) / 2)
        for x in range(len(formattedText[y])):
            screen[textY + y][textX + x] = formattedText[y][x]

'''
Function that performs all necessary operations to transition from the storyline to the game.
- Formats the entities for use in the game.
'''
def confirmChoices():
    # Declare global variables
    global plane, missile, enemy, missileDelay

    # Sets the entities to the user's choices in order to adhere to the format used in displaying the entities on the screen
    plane = plane[choices[0]]
    enemy = enemy[choices[3]]

    # Checks the missile (weapon on plane) choice of the player in order to change the workings of the missile
    if choices[1] < len(missile):
        # Sets the missile to the user's choice and adjusts the firing delay if necessary
        missile = missile[choices[1]]
        if choices[1] == 0:
            missileDelay -= 0.5
    else:
        # Sets the missile to the user's choice and adjusts the firing delay if necessary
        missile = missile[1]
        missileDelay += 0.5

        # Sets the locations of the double missiles depending on the choice of plane by the user
        if choices[0] == 0:
            for i in [5, 4, 14]:
                missileLocation.append(i)
        elif choices[0] == 1:
            for i in [5, 2, 8]:
                missileLocation.append(i)
        else:
            for i in [5, 5, 15]:
                missileLocation.append(i)

    # Sets the background of the screen depending on the user's planet choice
    for _ in range(int(screenHeight * screenWidth / 100)):
        planetParticles.append([choice(particles[choices[2]]), randrange(screenHeight), randrange(screenWidth)])

#########################################################################################################################################################################################

'''
Function that controls the user's keyboard input in the menu and choices sections and makes sure that no errors arise.
'''
def keyboardInputLoop():
    # Declare global variables
    global choosing, inMenu, screenHeight, screenWidth

    # Loop until the user has chosen a valid option
    while choosing:
        # Obtain user input
        userInput = input().capitalize()

        # Checks whether the user is in the menu or selecting an option
        if inMenu:
            # Series of checks to see if the user wants to and can decrease/increase the screen height/width
            if userInput in ['W', 'A', 'S', 'D']:
                if 'W' in userInput and screenHeight - 1 >= minScreenHeight:
                    screenHeight -= 1
                if 'A' in userInput and screenWidth - 2 >= minScreenWidth:
                    screenWidth -= 2
                if 'S' in userInput and screenHeight + 1 <= maxScreenHeight:
                    screenHeight += 1
                if 'D' in userInput and screenWidth + 2 <= maxScreenWidth:
                    screenWidth += 2
                clearScreen()
                updateMenu()
                menu()
                # Clears screen (CMD or PowerShell)
                system('cls')
                displayScreen()

            # Exits the menu if the user presses enter with a blank input
            elif userInput == "":
                inMenu = False
                break
        else:
            # Saves the user's choice and moves on to the next part of the story
            if userInput in ['1', '2', '3']:
                choices.append(int(userInput) - 1)
                break

'''
Function that updates the menu when the user changes the screen size.
'''
def updateMenu():
    # Checks if the user modified the screen height
    if len(screen) != screenHeight:
        # Obtains the amount which the user has increased/decreased the height by and determines whether to add or remove rows
        difference = abs(len(screen) - screenHeight)
        if len(screen) > screenHeight:
            for i in range(difference):
                screen.pop(len(screen) - 1)
                collisions.pop(len(collisions) - 1)
        else:
            for i in range(difference):
                screen.append([" " for _ in range(len(screen[0]))])
                collisions.append([" " for _ in range(len(collisions[0]))])

    # Checks if the user modified the screen width
    if len(screen[0]) != screenWidth:
        # Obtains the amount which the user has increased/decreased the width by and determines whether to add or remove columns
        difference = abs(len(screen[0]) - screenWidth)
        if len(screen[0]) > screenWidth:
            for y in range(len(screen)):
                for i in range(difference):
                    screen[y].pop(len(screen[y]) - 1)
                    collisions[y].pop(len(collisions[y]) - 1)
        else:
            for y in range(len(screen)):
                for i in range(difference):
                    screen[y].append(" ")
                    collisions[y].append(" ")

'''
Function that formats text according to the screen width in order to fit it inside the canvas.
'''
def formatText(unformattedText):
    # Puts the unformatted text into a new variable (to avoid changing the old variable)
    text = []
    for i in unformattedText:
        text.append(i)

    # Goes through the text and splits it up by words
    # Attempts to move the words that exceed the screen width to a new line
    # Reapeats the action until the text fits the canvas
    i = 0
    while i < len(text):
        if len(text[i]) > screenWidth:
            tempText = text[i].split(" ")
            i += 1
            text.insert(i, "")
            while len(" ".join(tempText)) > screenWidth:
                text[i] = tempText.pop(len(tempText) - 1) + " " + text[i]
            text[i - 1] = " ".join(tempText)
            text[i] = text[i][:-1]
        else:
            i += 1
    # Return the formatted version
    return text

'''
Function that takes in the choice index and returns the list associated to the choice.
Used to remove the need to create a seperate function for each choice.
'''
def getChoiceName(index):
    choiceName = ""
    if index == 0:
        choiceName = "plane"
    elif index == 1:
        choiceName = "weapon"
    elif index == 2:
        choiceName = "planet"
    elif index == 3:
        choiceName = "enemy"
    return choiceName

#########################################################################################################################################################################################
#########################################################################################################################################################################################

'''
Function that takes user input in order to control the plane in the game. (CMD or PowerShell ONLY)
- Alleviates the need of the need of the user pressing 'ENTER' between every key press.
- Does not require any external sources.
'''
def checkKeyboardInput():
    # Declare global variables
    global missileTime, playing, inMenu, choosing, selectedChoice, screenHeight, screenWidth

    # Obtains key presses for a short amount of time
    start = time()
    keyboardInput = []
    while time() - start < 0.1:
        if kbhit():
            keyboardInput.append(getwch().capitalize())
        sleep(0.01)

    # Quits the game if the user held the escape key for a significant amount of time
    if keyboardInput.count(chr(27)) > 3:
        exit()

    # Checks and sets the plane's intended movement based on the keys pressed by the player
    if 'W' in keyboardInput and 'S' not in keyboardInput:
        entities[0][6] = -1
    elif 'S' in keyboardInput and 'W' not in keyboardInput:
        entities[0][6] = 1
    else:
        entities[0][6] = 0
    if 'A' in keyboardInput and 'D' not in keyboardInput:
        entities[0][5] = -2
    elif 'D' in keyboardInput and 'A' not in keyboardInput:
        entities[0][5] = 2
    else:
        entities[0][5] = 0

    # Shoots a missile if the user hit the specified key and the delay timer is over
    if ' ' in keyboardInput and time() - missileTime > missileDelay and entities[0][2] >= len(missile):
        shootMissile()
        missileTime = time()

'''
Function that updates special tasks done by independent entities.
- Makes the enemy bounce side to side.
- Controls the spawning of bombs by the enemy.
- Controls the disappearance of missiles and boms.
'''
def checkSpecialEntities():
    # Loops until it has checked every entity
    entityCount = len(entities)
    i = 0
    while i < entityCount:
        # Checks if the entity is a special entity in need of special updates
        if entities[i][0] == "enemy":
            # Controls the side to side movement of the enemy
            if entities[i][1] <= 0 or entities[i][1] + entities[i][3] >= screenWidth - 1:
                entities[i][5] = -entities[i][5]

            # Acts as a timer for the dropping of bombs for every enemy.
            if time() - entities[i][8] > entities[i][7]:
                entities.append(["bomb", entities[i][1] + int(entities[i][3] / 2) + entities[i][5], entities[i][2] + entities[i][4] - 1, len(bomb[0]), len(bomb), 0, 1])
                entities[i][8] = time()
                entities[i][7] = randint(3, 8)
        elif entities[i][0] == "missile":
            # Controls the removal of missiles if they reach the top of the canvas
            if entities[i][2] <= 0:
                collisionZoneRemove(i)
                removeEntity(i)
                entityCount -= 1
                i -= 1
        elif entities[i][0] == "bomb":
            # Controls the removal of bombs once they reach the bottom of the canvas
            if entities[i][2] + entities[i][4] >= screenHeight - 1:
                collisionZoneRemove(i)
                removeEntity(i)
                entityCount -= 1
                i -= 1
        # Counter
        i += 1

'''
Function that clears the screen (canvas).
- If on CMD or Powershell, clears console.
- Removes every character saved in the screen.
'''
def clearScreen():
    # Clears screen (CMD or PowerShell)
    system('cls')

    # Iterates through every row and column to remove everything, leaving a blank screen
    for y in range(len(screen)):
        for x in range(len(screen[y])):
            screen[y][x] = " "

'''
Function that controls collisions and saving the entities to the canvas to be printed later.
- Uses an overlapping collisions map which mirrors the visible screen, but saves which character on the screen belongs to which entity.
- Uses this information to determine whether a collision has occured or not and what is to be done with the entities involved.
'''
def updateEntities():
    # Declare global variablbes
    global enemiesRemaining, health, playing, won

    # Loops through all entities
    for i in range(len(entities)):
        # Rechecks that the entity being checked exists in order to avoid errors (for loops do not update the length of lists through every iteration)
        if i < len(entities):
            # Calls methods that remove old collision zones and update the movement of entities
            collisionZoneRemove(i)
            checkMovement(i)

            # Declaration of variable used to break through the second loop if needed (after removing entities)
            nextEntity = False

            # Double loops to iterate through every character of the entity (2-Dimensional)
            for y in range(entities[i][4]):
                # Breaks the loop if an entity was removed in order to avoid errors
                if nextEntity:
                    nextEntity = False
                    break

                # Obtains the row and column information needed to check every character of the entity on the screen
                row = y + entities[i][2]
                exec("rowLength = len(%s[y])" % (entities[i][0]), locals(), globals())
                column = int((entities[i][3] - rowLength) / 2) + entities[i][1]
                for x in range(rowLength):
                    # Obtains the entity associated with the location on the screen and checks whether it belongs to a different entity or not
                    entity = collisions[row][column]
                    if entity == " " or entity == i:
                        # Collision has not occured, sets the character to its designated location on the screen and updates the collision map with the current entity
                        exec("character = %s[%d][%d]" % (entities[i][0], y, x), locals(), globals())
                        if character != " ":
                            screen[row][column] = character
                        collisions[row][column] = i
                        column += 1

                    # Series of checks to avoid errors before handling collisions between certain entities
                    elif entities[i][0] not in ["plane", "enemy"] or entities[entity][0] not in ["plane", "enemy", "bomb"]:
                        removeBoth = False
                        if entities[i][0] in ["plane", "missile"] and entities[entity][0] in ["plane", "missile"]:
                            continue
                        elif entities[i][0] in ["bomb", "enemy"] and entities[entity][0] in ["bomb", "enemy"]:
                            continue
                        elif entities[i][0] in ["missile", "enemy"] and entities[entity][0] in ["missile", "enemy"]:
                            # Handles the removal of enemies and checks how many are left
                            removeBoth = True
                            enemiesRemaining -= 1
                            if enemiesRemaining <= 0:
                                playing = False
                                won = True
                        elif entities[i][0] in ["bomb", "missile"] and entities[entity][0] in ["bomb", "missile"]:
                            removeBoth = True
                        elif entities[i][0] == "bomb" and entities[entity][0] == "plane":
                            # Handles the player's health and whether or not they lost by depleting their entire health
                            health -= 20
                            if health <= 0:
                                playing = False

                        # Handles calling explosions
                        if entities[i][0] not in ["bomb", "missile"]:
                            smallExplosion(entity)
                        else:
                            smallExplosion(i)

                        # Uses a boolean variable to determine whether or not both or just the current entity must be removed
                        if removeBoth:
                            # Checks whether the entity that the current entity collided with was before or after the entity currently being updated
                            # Uses this information to remove the entities in the correct order to avoid errors
                            if entity > i:
                                for a in [entity, i]:
                                    collisionZoneRemove(a)
                                    removeEntity(a)
                                i -= 1
                            else:
                                for a in [i, entity]:
                                    collisionZoneRemove(a)
                                    removeEntity(a)
                                i -= 2
                        else:
                            # Removes the entity that was in the collision
                            collisionZoneRemove(i)
                            removeEntity(i)
                            i -= 1

                        # Breaks through both the Y and X for loops for the entity and moves on to the next entity
                        nextEntity = True
                        break

'''
Function that controls the attempted movement by entities.
- Completes a series of checks to make sure that the entity is not going off the screen or anywhere else it should not be
'''
def checkMovement(i):
    # Checks Y movements of entities
    # Checks if the new position of the enitity would fall inside the canvas
    if entities[i][2] + entities[i][6] >= 0 and entities[i][2] + entities[i][4] + entities[i][6] < screenHeight:
        # Special check to make sure the plane does not get near the enemy
        if entities[i][0] != "plane" or entities[i][2] + entities[i][6] >= planeMinimumY:
            # Moves the entity
            entities[i][2] += entities[i][6]
        else:
            entities[i][2] = planeMinimumY
    else:
        # Puts the entity against the top or bottom of the screen when attempted movement surpasses the top or bottom of the screen
        if entities[i][2] + entities[i][6] < 0:
            entities[i][2] = 0
        else:
            entities[i][2] = screenHeight - entities[i][4]

    # Checks X movements of entities
    # Checks if the new position of the entity would fall inside the canvas
    if entities[i][1] + entities[i][5] >= 0 and entities[i][1] + entities[i][3] + entities[i][5] < screenWidth:
        # Moves the entity to the new position
        entities[i][1] += entities[i][5]
    else:
        # Puts the entity against the sides of the screen when attempted movement surpasses the sides of the screen
        if entities[i][1] + entities[i][5] < 0:
            entities[i][1] = 0
        else:
            entities[i][1] = screenWidth - entities[i][3]

'''
Function that updates the current explosion animations.
'''
def updateExplosions():
    # Loops through all explosions
    explosionCount = len(explosions)
    i = 0
    while i < explosionCount:
        # Centres the explosion where it was initially detonated
        offsetY = int(len(explosion[explosions[i][0]]) / 2)
        for y in range(explosions[i][2] - offsetY, explosions[i][2] - offsetY + len(explosion[explosions[i][0]])):
            offsetX = int(len(explosion[explosions[i][0]][y + offsetY - explosions[i][2]]) / 2)
            for x in range(explosions[i][1] - offsetX, explosions[i][1] - offsetX + len(explosion[explosions[i][0]][y + offsetY - explosions[i][2]])):
                if 0 <= y < screenHeight and 0 <= x < screenWidth:
                    screen[y][x] = explosion[explosions[i][0]][y + offsetY - explosions[i][2]][x + offsetX - explosions[i][1]]

        # Checks and updates the stage of the explosion
        if time() - explosions[i][3] > 0.1:
            explosions[i][0] += 1
            # Removes the explosion when gone through all stages
            if explosions[i][0] == len(explosion):
                # Spawns a new enemy if the explosion is from the explosion of an enemy
                if explosions[i][2] < len(enemy):
                    spawnEnemy()
                explosions.pop(i)
                explosionCount -= 1
                i -= 1
            else:
                # Resets the timer for the next stage of the explosions
                explosions[i][3] = time()
                
        # Increase counter
        i += 1

'''
Function that shows the particles on the screen.
- Uses the randomized list that contains particles and their locations based on the user's chosen planet.
'''
def showParticles():
    for i in range(len(planetParticles)):
        if collisions[planetParticles[i][1]][planetParticles[i][2]] == " ":
            screen[planetParticles[i][1]][planetParticles[i][2]] = planetParticles[i][0] 

'''
Function that displays the screen with an outline around the edges.
'''
def displayScreen():
    print(" " + "_" * screenWidth)
    for y in range(screenHeight):
        print("|" + "".join(screen[y]) + "|")
    print("|" + "_" * screenWidth + "|")


'''
Function that displays essential game information underneath the canvas.
- This involves enemies remaining, player health, and elapsed time.
'''
def displayGameInfo():
    # Declare global variables
    global startTime, timeSeconds, timeMinutes

    # Saves the values in strins in order to format correctly
    showEnemyCount = "Enemies: {0}".format(enemiesRemaining)
    showHealth = "Health: {0}".format(health)
    timeSeconds = int(time() - startTime)
    # Formats the time elapsed properly
    if timeSeconds >= 60:
        timeSeconds = 0
        timeMinutes += 1
        startTime = time()
    if timeSeconds == 0:
        secondsFormatted = "00"
    elif timeSeconds < 10:
        secondsFormatted = "0" + str(timeSeconds)
    else:
        secondsFormatted = str(timeSeconds)
    showTime = "Time: {0}:{1}".format(timeMinutes, secondsFormatted)

    # Prints and formats the information below the canvas
    print(" " + showEnemyCount + " " * (int(screenWidth / 2 - 0.5) - len(showEnemyCount) - int(len(showHealth) / 2 - 0.5)) + showHealth + " " * (int(screenWidth / 2) - len(showTime) - int(len(showHealth) / 2 - 0.5)) + showTime)
    print("\n" + " " * int((screenWidth - len(controls)) / 2) + controls)

#########################################################################################################################################################################################

'''
Function that removes entity, while also updating the collision map with the entities' updated indexes.
- If entities are after the one being removed, indexes must be lowered by 1 in order to match the new indexes that will arise from removing an entity.
'''
def removeEntity(entity):
    for i in range(entity + 1, len(entities)):
        for y in range(entities[i][2], entities[i][2] + entities[i][4]):
            for x in range(entities[i][1], entities[i][1] + entities[i][3]):
                if collisions[y][x] != " " and collisions[y][x] > entity:
                    collisions[y][x] -= 1
    entities.pop(entity)

'''
Function that removes the collision zone of an entity on invisible collision map.
- Takes into consideration that an entity might have been moved.
'''
def collisionZoneRemove(entity):
    for y in range(entities[entity][2] - abs(entities[entity][6]), entities[entity][2] + entities[entity][4] + abs(entities[entity][6])):
        for x in range(entities[entity][1] - abs(entities[entity][5]), entities[entity][1] + entities[entity][3] + abs(entities[entity][5])):
            if 0 <= y < screenHeight and 0 <= x < screenWidth and collisions[y][x] == entity:
                collisions[y][x] = " "

'''
Function that adds an explosion to the list of active explosions.
- Appends its location.
'''
def smallExplosion(entity):
    # Format: Stage, X, Y, Current Time
    explosions.append([0, entities[entity][1], entities[entity][2], time()])

'''
Function that adds one or two missiles to the list of active entities, depending on the user's missile choice.
'''
def shootMissile():
    if choices[1] < 2:
        # Format: Entity Name, X, Y, Horizontal Width, Vertical Height, X Movement, Y Movement
        entities.append(["missile", entities[0][1] + int(entities[0][3] / 2) + entities[0][5], entities[0][2] + entities[0][6], len(missile[0]), len(missile), 0, -2])
    else:
        for i in range(2):
            # Format: Entity Name, X, Y, Horizontal Width, Vertical Height, X Movement, Y Movement
            entities.append(["missile", entities[0][1] + missileLocation[i + 1] + entities[0][5], entities[0][2] + missileLocation[0] + entities[0][6], len(missile[0]), len(missile), 0 , -2])

'''
Function that spawns the user's plane at the start of the game
'''
def spawnPlane():
    # Format: Entity Name, X, Y, Horizontal Width, Vertical Height, X Movement, Y Movement
    entities.append(["plane", int(screenWidth / 2) - int(maxLength[0][choices[0]] / 2), screenHeight - len(plane), maxLength[0][choices[0]], len(plane), 0, 0])

'''
Function used to spawn enemies, appending all necessary information with it.
'''
def spawnEnemy():
    # Format: Entity Name, X, Y, Horizontal Width, Vertical Height, X Movement, Y Movement, Bomb Time, Current Time
    entities.append(["enemy", randint(0, screenWidth - maxLength[3][choices[3]]), 0, maxLength[3][choices[3]], len(enemy), [-2, 2][randrange(2)], 0, randint(1, 3), time()])

#########################################################################################################################################################################################
#########################################################################################################################################################################################

'''
Function that determines the winner and notifies the player.
- Displays fireworks if the player wins
'''
def gameEnd():
    # Declare global variables
    global won, choosing

    # Clear screen
    clearScreen()

    # Ensure all enitities and their collision zones are removed
    for _ in range(len(entities)):
        collisionZoneRemove(0)
        removeEntity(0)

    # Display explosions if player won the game
    if won:
        startTime = time()
        explosionDelay = time()
        while time() - startTime < 8:
            if time() - explosionDelay >= 1:
                explosions.append([0, randrange(screenWidth), randrange(screenHeight), time()])
            updateExplosions()
            displayScreen()
            sleep(0.1)
            clearScreen()

    # Determine which text to print on the screen
    index = int()
    if won:
        index = 1
    else:
        index = 0

    # Centres and displays the ASCII art lettering to the screen
    offsetY = int(screenHeight / 2) - int(len(gameOver[index]) / 2)
    for y in range(len(gameOver[index])):
        offsetX = int(screenWidth / 2) - int(len(gameOver[index][y]) / 2)
        for x in range(len(gameOver[index][y])):
            screen[offsetY + y][offsetX + x] = gameOver[index][y][x]

    # Centres and displays text letting the player know whether the won or not and how to play again or quit
    formattedText = formatText(gameOverText[index])
    offsetY = screenHeight - len(formattedText) - 1
    for y in range(len(formattedText)):
        offsetX = int(screenWidth / 2) - int(len(formattedText[y]) / 2)
        for x in range(len(formattedText[y])):
            screen[offsetY + y][offsetX + x] = formattedText[y][x]

    # Prints the screen
    displayScreen()

    # Loops until the user inputs a valid option
    choosing = True
    while choosing:
        # Obtains user input
        userInput = input()
        
        # Checks if user input is one of the available options
        if userInput == '1':
            # Clears screen and exits the loop to restart the game
            clearScreen()
            break
        elif userInput == '2':
            # Exits the program
            exit()

#########################################################################################################################################################################################
#########################################################################################################################################################################################

# Start the program
main()
