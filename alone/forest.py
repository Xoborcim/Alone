import inventoryManagement
import resourceManagement

start = False

# Global variables
choicePath = ""

# Booleans for each room to see where the player is
inRoomBeginning = True
inRoomDarkSouth = False
inRoomDarkNorth = False
inRoomCrossRoads = False
inRoomDarkWest = False
inRoomDarkEast = False
# ForestDarkSouth Variables
oStonePickedUp = False

# ForestDarkNorth Variables
bagPickedUp = False

applePickedUp = False
stickPickedUp = False

# ForestDarkEast Variables

sheetPickedUp = False


# Sebastian forestDarkSouth room
def forestDarkSouth():
    global oStonePickedUp
    global inRoomDarkSouth
    global choicePath
    global inRoomBeginning
    choicePath = ""
    resourceManagement.step() # Adds one step to the time manager
    while inRoomDarkSouth: # While in room
        print("You walked down the southern path. \n You are now in an especially dark section of the forest.") # Gives you your choices
        if not oStonePickedUp:
            print("There is an ominous stone on the ground.")
        print("Possible paths: North")
        choicePath = input()
        if choicePath.lower() == "north":
            inRoomDarkSouth = False
            inRoomBeginning = True
            forestBeginning()
        elif choicePath.lower() == "inventory":
            inventoryManagement.showInventory()
        elif choicePath.lower() == "pickup" and not oStonePickedUp:
            inventoryManagement.addItem("Ominous Stone")
            print("You picked up the 'Ominous Stone'.")
            oStonePickedUp = True
        elif choicePath.lower() == "eat":
            resourceManagement.consumeFood("Apple")
        else:
            print("Not an option")
            forestDarkSouth()


# Sebastian
def forestDarkNorth():
    global bagPickedUp
    global inRoomDarkNorth
    global choicePath
    global inRoomBeginning
    global inRoomCrossRoads

    resourceManagement.step()

    while inRoomDarkNorth:
        print("You follow the northern path")
        if not bagPickedUp:
            print("There is an empty bag on the ground")
        print("Possible paths: North, South")
        choicePath = input()
        if choicePath.lower() == "north":
            inRoomDarkNorth = False
            inRoomCrossRoads = True
            forestCrossRoads()
        elif choicePath.lower() == "south":
            inRoomDarkNorth = False
            inRoomBeginning = True
            forestBeginning()
        elif choicePath.lower() == "inventory":
            inventoryManagement.showInventory()
        elif choicePath.lower() == "pickup" and not bagPickedUp:
            inventoryManagement.maxInventory = 10
            print("You picked up the bag, max inventory size increased.")
            bagPickedUp = True
        elif choicePath.lower() == "eat":
            resourceManagement.consumeFood("Apple")
        else:
            print("Not an option")
            forestDarkNorth()


# Sebastian
def forestBeginning():
    global start
    global inRoomBeginning
    global inRoomDarkNorth
    global inRoomDarkSouth
    global choicePath
    choicePath = ""
    resourceManagement.step()
    while inRoomBeginning:
        if not start:
            print(
                "You awake from your deep slumber.\n You are in a forest so dense you cannot see the sky. \n Possible "
                "paths: North, South")
            start = True
        else:
            print("You are in a very dense forest. \n Possible paths: North, South")

        choicePath = input()
        if choicePath.lower() == "north":
            inRoomBeginning = False
            inRoomDarkNorth = True
            forestDarkNorth()
        elif choicePath.lower() == "south":
            inRoomDarkNorth = False
            inRoomDarkSouth = True
            forestDarkSouth()
        elif choicePath.lower() == "inventory":
            inventoryManagement.showInventory()
        elif choicePath.lower() == "eat":
            resourceManagement.consumeFood("Apple")
        else:
            print("Not an option")


# Sarim
def forestCrossRoads():
    global applePickedUp
    global inRoomDarkNorth
    global choicePath
    global inRoomBeginning
    global inRoomCrossRoads

    resourceManagement.step()

    while inRoomCrossRoads:
        print("You follow the northern path")
        if not applePickedUp:
            print("There is an apple on the ground")
        print("Possible paths:West,East,South")
        choicePath = input()
        if choicePath.lower() == "west":
            print("You walked west")
        if choicePath.lower() == "east":
            print("You walked east")
        elif choicePath.lower() == "south":
            inRoomCrossRoads = False
            inRoomDarkNorth = True
            forestDarkNorth()
        elif choicePath.lower() == "inventory":
            inventoryManagement.showInventory()
        elif choicePath.lower() == "pickup" and not applePickedUp:
            print("You picked up the apple.")
            applePickedUp = True
            inventoryManagement.addItem("Apple")
        elif choicePath.lower() == "eat":
            resourceManagement.consumeFood("Apple")
        else:
            print("Not an option")
            forestCrossRoads()


def forestDarkWest():
    global stickPickedUp
    global inRoomDarkWest
    global choicePath
    global inRoomBeginning

    resourceManagement.step()

    while inRoomDarkWest:
        print("You follow the western path")
        if not stickPickedUp:
            print("There is a whole in the ground, a stick is in the whole.")
        print("Possible paths:South")
        choicePath = input()
        if choicePath.lower() == "west":
            print("You walked west")
        if choicePath.lower() == "east":
            print("You walked east")
        elif choicePath.lower() == "south":
            inRoomDarkWest = False
            inRoomBeginning = True
            forestBeginning()
        elif choicePath.lower() == "inventory":
            inventoryManagement.showInventory()
        elif choicePath.lower() == "pickup" and not stickPickedUp:
            inventoryManagement.maxInventory = 10
            print("You picked up the stick, max inventory size increased.")
            stickPickedUp = True
        elif choicePath.lower() == "eat":
            resourceManagement.consumeFood("Apple")
        else:
            print("Not an option")
            forestCrossRoads()


def forestDarkEast():
    global sheetPickedUp
    global inRoomDarkEast
    global choicePath
    global inRoomCrossRoads

    resourceManagement.step()

    while inRoomDarkEast:
        print("You follow the eastern path")
        if not sheetPickedUp:
            print("You see a pair of eyes in the shadows.Once you blink the eyes are gone.You go to investigate and find a metal sheet the size of a coin.")
        print("Possible paths:North, South")
        choicePath = input()
        if choicePath.lower() == "west":
            print("You walked west")
        elif choicePath.lower() == "south":
            inRoomDarkEast = False
            inRoomCrossRoads = True
            forestCrossRoads()
        elif choicePath.lower() == "inventory":
            inventoryManagement.showInventory()
        elif choicePath.lower() == "pickup" and not sheetPickedUp:
            inventoryManagement.maxInventory = 10
            print("You picked up the sheet, max inventory size increased.")
            sheetPickedUp = True
        elif choicePath.lower() == "eat":
            resourceManagement.consumeFood("Apple")
        else:
            print("Not an option")
            forestDarkEast()
