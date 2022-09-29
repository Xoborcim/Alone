import enemies
import inventoryManagement
import resourceManagement
import forest

inTown = False

inTownCentre = True
inHouse1 = False
inHouse2 = False
inHouse3 = False

encounteredEnemy = False
choicePath = ""

pickedUpCoat = False
knifePickedUp = False


# Sebastian
def townCentre():
    global choicePath
    global inTownCentre
    global encounteredEnemy
    global inTown
    global inHouse1
    global inHouse2
    global inHouse3

    while inTownCentre:
        print("\033[1;33;40mYou enter a small town with 3 houses.\n")
        print("Possible paths:House 1, House 2, House 3, South")
        choicePath = input()
        if choicePath.lower() == "south":
            print("You walked South back into the forest")
            inTown = False
            forest.inForest = True
            forest.inRoomCrossRoads = True
            forest.forestCrossRoads()
        elif choicePath.lower() == "house 1":
            encounteredEnemy = False
            inTownCentre = False
            inHouse1 = True
            print("You entered the first house")
            house1()
            # if you enter the first house it will run the code for the first house
        elif choicePath.lower() == "house 2":
            encounteredEnemy = False
            print("You entered the second house")
            inTownCentre = False
            inHouse2 = True
            house2()
            # if you enter the first house it will run the code for the first house
        elif choicePath.lower() == "house 3":
            encounteredEnemy = False
            print("You entered the third house")
            inTownCentre = False
            inHouse3 = True
            house3()
            # if you enter the first house it will run the code for the first house
        elif choicePath.lower() == "inventory":
            inventoryManagement.showInventory()
        elif choicePath.lower() == "eat":
            resourceManagement.consumeFood("Apple")
        else:
            print("Not an option")
            townCentre()


# code for house 1
def house1():
    global choicePath
    global inHouse1
    global encounteredEnemy
    global inTownCentre
    global pickedUpCoat

    while inHouse1:
        print("You enter a small house.")
        if not pickedUpCoat:
            print("There is a coat on the ground.")
        print("Possible paths: Exit")
        choicePath = input()
        if choicePath.lower() == "exit":
            inHouse1 = False
            inTownCentre = True
            print("You exited the house")
        elif choicePath.lower() == "inventory":
            inventoryManagement.showInventory()
        elif choicePath.lower() == "eat":
            resourceManagement.consumeFood("Apple")
        elif choicePath.lower() == "pickup" and not pickedUpCoat:
            inventoryManagement.armorAdd("Coat", 2, 1)
            pickedUpCoat = True
        else:
            print("Not an option")
            house1()


# code for house 2
def house2():
    global choicePath
    global inHouse2
    global encounteredEnemy
    global inTownCentre

    while inHouse2:
        if forest.swordObtained and forest.armorObtained:
          secretBoss()
        print("You enter a small house. There is nothing in this house.")
        print("Possible paths: Exit")
        choicePath = input()
        if choicePath.lower() == "exit":
            inHouse2 = False
            inTownCentre = True
            print("You exited the house")
        elif choicePath.lower() == "inventory":
            inventoryManagement.showInventory()
        elif choicePath.lower() == "eat":
            resourceManagement.consumeFood("Apple")
        else:
            print("Not an option")
            house2()


# code for house 3
def house3():
    global choicePath
    global inHouse3
    global encounteredEnemy
    global inTownCentre
    global knifePickedUp

    while inHouse3:
        print("You enter a small house.")
        if not knifePickedUp:
            print("There is a knife on the table.")
        print("Possible paths: Exit")
        choicePath = input()
        if choicePath.lower() == "exit":
            inHouse3 = False
            inTownCentre = True
            print("You exited the house")
        elif choicePath.lower() == "inventory":
            inventoryManagement.showInventory()
        elif choicePath.lower() == "eat":
            resourceManagement.consumeFood("Apple")
        elif choicePath.lower() == "pickup" and not knifePickedUp:
            inventoryManagement.weaponAdd("Knife", 3)
            knifePickedUp = True
        else:
            print("Not an option")
            house3()


def secretBoss():
  if forest.swordObtained and forest.armorObtained:
            # game checks if you have 2 specific items
            print("A mysterious being walks out from behind the tree.")
            if enemies.enemiesKilled == 0:
                if resourceManagement.beatOnce:
                    # if player has killed 0 enemies and has beaten the game once print message below
                    print("'You have beaten this game before it seems. Well no need to repeat myself. Let's get straight to it!")
                else:
                    # if player has not beaten game once run code below
                    print(
                        "The being speaks in your head. 'You have managed to escape that cursed place without spilling any "
                        "blood and you have found the sword and the armor. For that I applaud you. I have been here for so "
                        "long with nothing to do. Why not give me a fight?")
                    input("Fight this being?")
                    print("'You really think that you have a choice?'")
                enemies.startEncounter("Yorbkx")
                defeated()
                if resourceManagement.beatOnce:
                    resourceManagement.gameOver(
                        "'Are you satisfied now? You shouldn't just keep playing. You really don't gain much'")
                else:
                    resourceManagement.gameOver(
                        "'You have beat me, I will be your ally and help you rebuild this broken "
                        "world.' You and the being begin planning on how you can stop the Earth")
                    # if player has killed an enemy run code below
            else:
                # if player beat the game once run code below
                if resourceManagement.beatOnce:
                    print(
                        "'Have you really come back just to kill them again? Well this time I will make sure to stop you for it you monster.'")
                    # if player has not beaten game once run code below
                else:
                    print("'You think you can get away with murder? Well I will make sure you are punished for it'")
                enemies.startEncounter("Yorbkx")
                defeated()
                if resourceManagement.beatOnce:
                    resourceManagement.gameOver("You have killed it again. You grin in satisfaction.")
                else:
                    resourceManagement.gameOver(
                        "You have killed the being. You stumble through the forest.\nYou feel the "
                        "souls of the monsters you killed try to fight you but you fight it off.")


def defeated():
  file = open("playedOnce.txt", "w")
  file.truncate(0)
  file.write(str(resourceManagement.beatOnce))

  file.close()