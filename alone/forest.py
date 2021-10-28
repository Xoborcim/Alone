import inventoryManagement

# Sebastian
start = False

# Global variables
choicePath = ""

# Booleans for each room to see where the player is
inRoomBeginning = True
inRoomDarkSouth = False
inRoomDarkNorth = False

# ForestDarkSouth Variables
oStonePickedUp = False

# ForestDarkNorth Variables
bagPickedUp = False


def forestDarkSouth():
    global oStonePickedUp
    global inRoomDarkSouth
    global choicePath
    global inRoomBeginning
    choicePath = ""

    while inRoomDarkSouth:
        print("You walked down the southern path. \n You are now in an especially dark section of the forest.")
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
        else:
            print("Not an option")
            forestDarkSouth()


def forestDarkNorth():
    global bagPickedUp
    global inRoomDarkNorth
    global choicePath
    global inRoomBeginning

    while inRoomDarkNorth:
        print("You follow the northern path")
        if not bagPickedUp:
            print("There is an empty bag on the ground")
        print("Possible paths: North, South")
        choicePath = input()
        if choicePath.lower() == "north":
            print("You walked north")
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
        else:
            print("Not an option")
