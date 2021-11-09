import enemies
import inventoryManagement
import resourceManagement
import forest

inCave = False
# Room booleans to find player location
inRoomCaveEntrance = True
inRoomCaveEast = False
inRoomCaveWest = False
inRoomCaveExit = False

encounteredEnemy = False
choicePath = ""

keyObtained = False


# Sebastian
def caveEntrance():
    global choicePath
    global inRoomCaveEntrance
    global encounteredEnemy
    global inCave
    global inRoomCaveEast
    global inRoomCaveWest
    print("\035[1;32;40m\n")
    resourceManagement.step()
    if not encounteredEnemy:
        enemies.startEncounter("Troll")
        encounteredEnemy = True
    while inRoomCaveEntrance:
        print("You enter a dark cave. There are gems in the wall that have a faint glow.\n Do gems always glow?")
        print("Possible paths:East, West, South")
        choicePath = input()
        # in this part of the code the player is presented with directions and they can chose where to go
        if choicePath.lower() == "east":
            encounteredEnemy = False
            print("You walked East")
            inRoomCaveEntrance = False
            inRoomCaveEast = True
            caveEast()
        elif choicePath.lower() == "west":
            encounteredEnemy = False
            inRoomCaveEntrance = False
            inRoomCaveWest = True
            print("You walk West")
            caveWest()
        elif choicePath.lower() == "south":
            encounteredEnemy = False
            print("You walk South")
            forest.inForest = True
            inCave = False
            inRoomCaveEntrance = False
            forest.inRoomDarkEast = True
            forest.forestDarkEast()
        elif choicePath.lower() == "inventory":
            inventoryManagement.showInventory()
            # player asks to open inventory and the inventory is shown
        elif choicePath.lower() == "eat":
            resourceManagement.consumeFood("Apple")
            # player can eat an apple
        else:
            print("Not an option")
            caveEntrance()
            # if player inputs an invalid option the code will print "Not an option"


# Sarim
def caveEast():
    global choicePath
    global inRoomCaveEntrance
    global encounteredEnemy
    global inCave
    global inRoomCaveEast
    global keyObtained

    resourceManagement.step()
    if not encounteredEnemy:
        enemies.startEncounter("Sprite")
        encounteredEnemy = True
    while inRoomCaveEast:
        print(
            "You enter a small section of the cave. There are no gems and the room is very dark\n except for the glow from the room before.")
        if not keyObtained:
            print("You spot a small crimson key on the ground")
        print("Possible paths: West")
        choicePath = input()
        if choicePath.lower() == "west":
            encounteredEnemy = False
            inRoomCaveEast = False
            inRoomCaveEntrance = True
            print("You walked West")
        elif choicePath.lower() == "inventory":
            inventoryManagement.showInventory()
        elif choicePath.lower() == "eat":
            resourceManagement.consumeFood("Apple")
        elif choicePath.lower() == "pickup" and not keyObtained:
            inventoryManagement.addItem("Crimson Key")
            keyObtained = True
            print("You have obtained the 'Crimson Key'")
        else:
            print("Not an option")
            caveEast()


# Sarim
def caveWest():
    global choicePath
    global inRoomCaveWest
    global encounteredEnemy
    global inRoomCaveEntrance
    global inRoomCaveExit
    global keyObtained

    resourceManagement.step()
    if not encounteredEnemy:
        enemies.startEncounter("Sprite")
        encounteredEnemy = True
    while inRoomCaveWest:
        print("You enter a Path, you feel a breeze ahead of you and there is a light at the end of this path.\nOn the "
              "walls there is drawings of the Earth Absorbing all Life Energy from its inhabitants")
        print(7 - resourceManagement.day, "Days Left until your Life Energy is gone.")
        # game shows how many day are left until you die
        print("Possible paths: North, East")
        choicePath = input()
        if choicePath.lower() == "east":
            encounteredEnemy = False
            inRoomCaveWest = False
            inRoomCaveEntrance = True
            print("You walked West")
            caveEntrance()
        elif choicePath.lower() == "north":
            if keyObtained:
                encounteredEnemy = False
                inRoomCaveWest = False
                inRoomCaveExit = True
                print("You walked North")
                caveExit()
            else:
                print("You need the key to do go there")
        elif choicePath.lower() == "inventory":
            inventoryManagement.showInventory()
        elif choicePath.lower() == "eat":
            resourceManagement.consumeFood("Apple")
        else:
            print("Not an option")
            caveEast()


# Sebastian
# Exit of the cave
def caveExit():
    print("You exit the cave into a beautiful meadow. On the massive Tree in front of you you see drawings "
          "\nexplaining that here you are immune from the Earth.")
    # if player killed 0 enemies run code below
    if enemies.enemiesKilled == 0:
        print("At last you have finally found a place where you can live out in peace.")
        print("As you analyze your surroundings you realize that you are the only one there.")
        resourceManagement.gameOver("You feel your body collapse from exhaustion as you fall asleep...")
        # if player killed 1 or more enemies run code below
    elif enemies.enemiesKilled != 0:
        print("As you walk into the meadow you feel a sharp pain in your gut.")
        print("All the souls you have taken away from those 'monsters' begin transforming you into something that is "
              "not you.")
        resourceManagement.gameOver("You have lost everything that keeps you attached to your humanity.\nYou stumble "
                                    "through the meadow as you disappear, consumed by the souls and your own guilt.")
