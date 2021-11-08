inventory = []
maxInventory = 5
playerAttack = 1
playerDefense = 0
playerHealth = 10
playerEvasiveness = 2


# Sebastian, Adds item to your inventory if you have room
def addItem(item):
    global inventory
    if len(inventory) <= maxInventory:
        inventory.append(item)
    else:
        print("Your inventory is full")


# Sebastian, Removes item from your inventory if you have that item
def removeItem(item):
    global inventory
    if item in inventory:
        inventory.remove(item)
    else:
        print("You don't have this item")


# Sebastian, Prints your inventory
def showInventory():
    stats()
    print("Inventory:\n", inventory)


# Sebastian, Adds a weapon and gives you extra attack
def weaponAdd(name, attack):
    global playerAttack
    addItem(name)
    playerAttack += attack
    print("You gained", attack, "attack")


# Sebastian, adds a piece of armor which gives you defense and evasiveness
def armorAdd(name, defense, evasiveness):
    global playerDefense
    global playerEvasiveness

    addItem(name)
    playerDefense += defense
    playerEvasiveness += evasiveness
    print("You gained", defense, "armor.")
    if evasiveness != 0:
        print("You gained", evasiveness, "evasiveness.")


# Gets the player stats and prints them
def stats():
    print("Attack:", playerAttack, "\nDefense:", playerDefense, "\nHealth", playerHealth, "\nEvasiveness", playerEvasiveness)