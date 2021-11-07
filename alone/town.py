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
        print("You enter a Small town with three houses")
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
        elif choicePath.lower() == "house 2":
            encounteredEnemy = False
            print("You entered the second house")
            inTownCentre = False
            inHouse2 = True
            house2()
        elif choicePath.lower() == "house 3":
            encounteredEnemy = False
            print("You entered the third house")
            inTownCentre = False
            inHouse3 = True
            house3()
        elif choicePath.lower() == "inventory":
            inventoryManagement.showInventory()
        elif choicePath.lower() == "eat":
            resourceManagement.consumeFood("Apple")
        else:
            print("Not an option")
            townCentre()


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


def house2():
    global choicePath
    global inHouse2
    global encounteredEnemy
    global inTownCentre

    while inHouse2:
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
