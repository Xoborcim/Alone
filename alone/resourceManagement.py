# Sarim
import inventoryManagement
steps = 0
day = 0
hunger = 5
hungerSteps = 0
hungerDrain = 5
timeSteps = 12
playerDead = False
beatOnce = False


# Sarim
# Adds steps to the time tracker every time player does a movement between roooms
def step():
    global hungerSteps
    global steps
    global hunger
    steps += 1
    hungerSteps += 1
    timeTracker()


# Sarim Tracks the time passed and if enough time passes you become hungrier and the days tick away
def timeTracker():
    global timeSteps
    global hungerSteps
    global steps
    global day
    global hunger
    global hungerDrain
    global hungerSteps

    if not playerDead:
        if steps >= timeSteps:
            day += 1
            timeSteps += 12
        if hungerSteps >= hungerDrain:
            print("You feel hungrier")
            hunger -= 1
            hungerDrain += 5
        if day >= 7:
            gameOver("Your life was drained by the Earth. You feel your body lose energy. You can't di...")
        if hunger <= 0:
            gameOver("You starved to death")


# Sebastian if you consume food it refills your hunger
def consumeFood(food):
    global hungerDrain
    global hunger
    global hungerSteps

    if food == "Apple":
        if "Apple" in inventoryManagement.inventory:
            if hunger < 3:
                inventoryManagement.removeItem(food)
                hungerDrain += 5
                hunger = 3
                print("You ate an apple your hunger was restored.")
            else:
                inventoryManagement.removeItem(food)
                inventoryManagement.playerHealth = 10
                print("Your health is full so you healed your health back.")
    else:
        print("You can't eat that")


# Sebastian Checks the player's health
def healthCheck():
    if inventoryManagement.playerHealth <= 0:
        gameOver("You feel your body lose energy. You can't di...")


# Sebastian If the player dies it will print a custom game over text
def gameOver(message):
    global beatOnce
    beatOnce = True
    print(message)
    file = open("playedOnce.txt", "w")
    file.truncate(0)
    file.write(str(beatOnce))

    file.close()
    input("Press 'Enter' to close.")
    exit()


# Sebastian Prints all the instructions
def instructions():
    print("\033[1;36;40m\n")
    print("You can move by typing in a possible path which is presented to you in each room.")
    print("You can type 'inventory' to view your inventory and your stats.")
    print("You can type 'eat' to eat food to refill your hunger or heal you.")
    print("If there is an item on the ground you can pick it up using 'pickup'")
    print("In battle you have 4 options, Fight, Eat, Check, Run")
    print("Fight deals damage")
    print("Eat can refill your health or hunger depending on how hungry you are")
    print("Check gets the enemies stats and prints them")
    print("Run lets you attempt an escape")
    print("\033[1;32;40m\n")



# Sebastian Checks to see if they have beaten the game once before, if yes the game will become harder and will change
# some dialogue
def load():
    global beatOnce
    global day

    file = open("playedOnce.txt", "r")
    data = file.readlines()
    beatOnce = data[0]
    if beatOnce:
        day = 4
