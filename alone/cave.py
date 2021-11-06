import enemies
import inventoryManagement
import resourceManagement
import forest

inCave = True
inRoomCaveEntrance = True
encounteredEnemy = False
choicePath = ""


def caveEntrance():
    global choicePath
    global inRoomCaveEntrance
    global encounteredEnemy
    global inCave

    resourceManagement.step()
    if not encounteredEnemy:
        enemies.startEncounter("Troll")
        encounteredEnemy = True
    while inRoomCaveEntrance:
        print("You enter a dark cave.")
        print("Possible paths:East, West, South")
        choicePath = input()
        if choicePath.lower() == "east":
            encounteredEnemy = False
            print("You walked East")
        elif choicePath.lower() == "west":
            encounteredEnemy = False
            print("You walk West")
        elif choicePath.lower() == "south":
            encounteredEnemy = False
            print("You walk South")
            forest.inForest = True
            inCave = False
            inRoomCaveEntrance = False
        elif choicePath.lower() == "inventory":
            inventoryManagement.showInventory()
        elif choicePath.lower() == "eat":
            resourceManagement.consumeFood("Apple")
        else:
            print("Not an option")
            caveEntrance()
