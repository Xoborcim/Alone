import inventoryManagement

start = False
oStonePickedUp = False


# Sebastian
def forestBeginning():
    global start

    def forestDarkNorth():
        print("You are here")

    def forestDarkSouth():
        global oStonePickedUp
        while 1 == 1:
            print("You walk up the northern path. \n You are now in an especially dark section of the forest.")
            if not oStonePickedUp:
                print("There is an ominous stone on the ground. Pick it Up?")
                pickup = input()
                if pickup.lower() == "yes":
                    inventoryManagement.addItem("Ominous Stone")
                    print("You picked up the 'Ominous Stone'.")
                    oStonePickedUp = True
                elif pickup.lower() == "no":
                    print("You did not pick up the stone")
                else:
                    print("Not an option")
            print("Possible paths: North")
            choicePath = input()
            if choicePath.lower() == "north":
                forestBeginning()
            else:
                print("Not an option")
                break

    if not start:
        print(
            "You awake from your deep slumber.\n You are in a forest so dense you cannot see the sky. \n Possible paths: North, South")
        start = True
    else:
        print("You are in a very dense forest. \n Possible paths: North, South")
    choicePath = input()
    if choicePath.lower() == "north":
        forestDarkNorth()
    elif choicePath.lower() == "south":
        forestDarkSouth()
    else:
        print("Not an option")
