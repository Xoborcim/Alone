import enemies
import inventoryManagement
import resourceManagement
import cave
import town

start = False

inForest = True

# Global variables
choicePath = ""

encounteredEnemy = False

# Booleans for each room to see where the player is
inRoomBeginning = True
inRoomDarkSouth = False
inRoomDarkNorth = False
inRoomCrossRoads = False
inRoomDarkWest = False
inRoomDarkEast = False

# Item booleans
oStonePickedUp = False
bagPickedUp = False
applePickedUp = False
stickPickedUp = False
sheetPickedUp = False
swordObtained = False
armorObtained = False


# Sebastian forestDarkSouth room
def forestDarkSouth():
    global oStonePickedUp
    global inRoomDarkSouth
    global choicePath
    global inRoomBeginning
    global encounteredEnemy
    global armorObtained

    choicePath = ""
    resourceManagement.step()  # Adds one step to the time manager
    if not encounteredEnemy:
        enemies.startEncounter("Slime")
        encounteredEnemy = True
    while inRoomDarkSouth:  # While in room
        print("You walked down the southern path.\nYou are now in an especially dark section of the forest.")  # Gives you your choices
        if not oStonePickedUp:
            print("There is an Ominous Stone on the ground.")
        if swordObtained and not armorObtained:
            print("You find a piece of Armor Covered in Thorns")
            armorObtained = True
            inventoryManagement.armorAdd("Leeching Thorn Armor", 10, 5)
        print("Possible Paths: North")
        choicePath = input()
        if choicePath.lower() == "north":
            encounteredEnemy = False
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
    global encounteredEnemy

    resourceManagement.step()

    while inRoomDarkNorth:
        print("You enter another section of the forest")
        if not bagPickedUp:
            print("There is an empty bag on the ground")
        print("Possible paths: North, South")
        choicePath = input()
        if choicePath.lower() == "north":
            encounteredEnemy = False
            inRoomDarkNorth = False
            inRoomCrossRoads = True
            forestCrossRoads()
        elif choicePath.lower() == "south":
            encounteredEnemy = False
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
    global encounteredEnemy

    choicePath = ""
    resourceManagement.step()
    while inRoomBeginning:
        if not start:
            resourceManagement.instructions()
            print(
                "You awake from your deep slumber.\nYou are in a forest so dense you cannot see the sky.\nPossible "
                "paths: North, South")
            start = True
        else:
            print("You are in a very dense forest.\n Possible paths: North, South")

        choicePath = input()
        if choicePath.lower() == "north":
            encounteredEnemy = False
            inRoomBeginning = False
            inRoomDarkNorth = True
            forestDarkNorth()
        elif choicePath.lower() == "south":
            encounteredEnemy = False
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
    global inRoomDarkWest
    global inRoomDarkEast
    global encounteredEnemy
    global inForest

    resourceManagement.step()
    if not encounteredEnemy:
        enemies.startEncounter("Goblin")
        encounteredEnemy = True
    while inRoomCrossRoads:
        print("You enter a section of the forest that is a crossroad")
        if not applePickedUp:
            print("There is an apple on the ground")
        print("Possible paths:West, East, South, North")
        choicePath = input()
        if choicePath.lower() == "west":
            encounteredEnemy = False
            inRoomCrossRoads = False
            inRoomDarkWest = True
            forestDarkWest()
        if choicePath.lower() == "east":
            encounteredEnemy = False
            inRoomCrossRoads = False
            inRoomDarkEast = True
            forestDarkEast()
        elif choicePath.lower() == "south":
            encounteredEnemy = False
            inRoomCrossRoads = False
            inRoomDarkNorth = True
            forestDarkNorth()
        elif choicePath.lower() == "north":
            encounteredEnemy = False
            print("You walked North")
            inForest = False
            inRoomCrossRoads = False
            town.inTown = True
            town.inTownCentre = True
            town.townCentre()
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
    global inRoomCrossRoads
    global encounteredEnemy

    resourceManagement.step()
    if not encounteredEnemy:
        enemies.startEncounter("Slime")
        encounteredEnemy = True
    while inRoomDarkWest:
        print("You follow the western path")
        if not stickPickedUp:
            print("There is a hole in the ground, a stick is in the hole.")
        print("Possible paths:East")
        choicePath = input()
        if choicePath.lower() == "east":
            encounteredEnemy = False
            inRoomDarkWest = False
            inRoomCrossRoads = True
            forestCrossRoads()
        elif choicePath.lower() == "inventory":
            inventoryManagement.showInventory()
        elif choicePath.lower() == "pickup" and not stickPickedUp:
            inventoryManagement.maxInventory = 10
            print("You picked up the stick.")
            inventoryManagement.weaponAdd("Stick", 2)
            stickPickedUp = True
        elif choicePath.lower() == "eat":
            resourceManagement.consumeFood("Apple")
        else:
            print("Not an option")
            forestDarkWest()


def forestDarkEast():
    global sheetPickedUp
    global inRoomDarkEast
    global choicePath
    global inRoomCrossRoads
    global encounteredEnemy
    global inForest
    global swordObtained

    resourceManagement.step()
    if not encounteredEnemy:
        enemies.startEncounter("Goblin")
        encounteredEnemy = True
    while inRoomDarkEast:
        print("You follow the eastern path")
        if not sheetPickedUp:
            print("You see a pair of eyes in the shadows. Once you blink the eyes are gone.\nYou go to investigate "
                  "and find a metal sheet the size of a coin.")
        print("Possible paths:North, South")
        choicePath = input()
        if choicePath.lower() == "north":
            encounteredEnemy = False
            print("You walked North")
            inForest = False
            inRoomDarkEast = False
            cave.inCave = True
            cave.inRoomCaveEntrance = True
            cave.caveEntrance()
        elif choicePath.lower() == "west":
            encounteredEnemy = False
            inRoomDarkEast = False
            inRoomCrossRoads = True
            forestCrossRoads()
        elif choicePath.lower() == "inventory":
            inventoryManagement.showInventory()
        elif choicePath.lower() == "pickup" and not sheetPickedUp:
            sheetPickedUp = True
            inventoryManagement.addItem("Metal Sheet")
            if sheetPickedUp and oStonePickedUp:
                print("You picked up the sheet. The 'Ominous Stone' and the 'Metal Sheet' combine into the 'Sword of "
                      "the Wanderer'\nThe sword is pointing the where the stone was found.")
                inventoryManagement.removeItem("Metal Sheet")
                inventoryManagement.removeItem("Ominous Stone")
                inventoryManagement.weaponAdd("Sword of the Wanderer", 10)
                swordObtained = True
        elif choicePath.lower() == "eat":
            resourceManagement.consumeFood("Apple")
        else:
            print("Not an option")
            forestDarkEast()

