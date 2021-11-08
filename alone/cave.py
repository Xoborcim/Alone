import enemies
import inventoryManagement
import resourceManagement
import forest

inCave = False

inRoomCaveEntrance = True
inRoomCaveEast = False
inRoomCaveWest = False
inRoomCaveExit = False

encounteredEnemy = False
choicePath = ""


# Sebastian
def caveEntrance():
    global choicePath
    global inRoomCaveEntrance
    global encounteredEnemy
    global inCave
    global inRoomCaveEast
    global inRoomCaveWest

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
        elif choicePath.lower() == "eat":
            resourceManagement.consumeFood("Apple")
        else:
            print("Not an option")
            caveEntrance()


def caveEast():
    global choicePath
    global inRoomCaveEntrance
    global encounteredEnemy
    global inCave
    global inRoomCaveEast

    resourceManagement.step()
    if not encounteredEnemy:
        enemies.startEncounter("Sprite")
        encounteredEnemy = True
    while inRoomCaveEast:
        print("You enter a small cavern.")
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
        else:
            print("Not an option")
            caveEast()


def caveWest():
    global choicePath
    global inRoomCaveWest
    global encounteredEnemy
    global inRoomCaveEntrance
    global inRoomCaveExit

    resourceManagement.step()
    if not encounteredEnemy:
        enemies.startEncounter("Sprite")
        encounteredEnemy = True
    while inRoomCaveWest:
        print("You enter a Path, you feel a breeze ahead of you and there is a light at the end of this path.\nOn the "
              "walls there is drawings of the Earth Absorbing all Life Energy from its inhabitants")
        print(7 - resourceManagement.day, "Days Left until your Life Energy is gone.")
        print("Possible paths: North, East")
        choicePath = input()
        if choicePath.lower() == "east":
            encounteredEnemy = False
            inRoomCaveWest = False
            inRoomCaveEntrance = True
            print("You walked West")
            caveEntrance()
        elif choicePath.lower() == "north":
            encounteredEnemy = False
            inRoomCaveWest = False
            inRoomCaveExit = True
            print("You walked North")
            caveExit()
        elif choicePath.lower() == "inventory":
            inventoryManagement.showInventory()
        elif choicePath.lower() == "eat":
            resourceManagement.consumeFood("Apple")
        else:
            print("Not an option")
            caveEast()


def caveExit():
    print("You exit the cave into a beautiful meadow. On the massive Tree in front of you you see drawings "
          "\nexplaining that here you are immune from the Earth.")
    if forest.swordObtained and forest.armorObtained:
        print("A mysterious being walks out from behind the tree.")
        if enemies.enemiesKilled == 0:
            if resourceManagement.beatOnce:
                print("'You have beat this game before it seems. Well no need to repeat myself now.'")
            else:
                print(
                    "The being speaks in your head. 'You have managed to escape that cursed place without spilling any "
                    "blood and you have found the sword and the armor. For that I applaud you. I have been here for so "
                    "long with nothing to do. Why not give me a fight?")
                input("Fight this being?")
                print("'You really think that you have a choice?'")
            enemies.startEncounter("Yorbkx")
            if resourceManagement.beatOnce:
                resourceManagement.gameOver("'Are you satisfied now?'")
            else:
                resourceManagement.gameOver("'You have beat me, I will be your ally and help you rebuild this broken "
                                            "world.' You and the being begin planning on how you can stop the Earth")
        else:
            if resourceManagement.beatOnce:
                print(
                    "'Have you really come back just to kill them again? Well this time I will make sure to stop you for it you monster.'")
            else:
                print("'You think you can get away with murder? Well I will make sure you are punished for it'")
            enemies.startEncounter("Yorbkx")
            if resourceManagement.beatOnce:
                resourceManagement.gameOver("You have killed it again. You grin in satisfaction.")
            else:
                resourceManagement.gameOver("You have killed the being. You stumble through the forest.\nYou feel the "
                                            "souls of the monsters you killed try to fight you but you fight it off.")
    elif enemies.enemiesKilled == 0:
        print("At last you have finally found a place where you can live out in peace.")
        print("As you analyze your surroundings you realize that you are the only one there.")
        resourceManagement.gameOver("You feel your body collapse from exhaustion as you fall asleep...")
    elif enemies.enemiesKilled != 0:
        print("As you walk into the meadow you feel a sharp pain in your gut.")
        print("All the souls you have taken away from those 'monsters' begin transforming you into something that is "
              "not you.")
        resourceManagement.gameOver("You have lost everything that keeps you attached to your humanity.\nYou stumble "
                                    "through the meadow as you disappear, consumed by the souls and your own guilt.")
