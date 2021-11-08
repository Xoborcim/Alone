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


def weaponAdd(name, attack):
    global playerAttack
    addItem(name)
    playerAttack += attack
    print("You gained", attack, "attack")


def weaponRemove(name, attack):
    global playerAttack
    removeItem(name)
    playerAttack -= attack
    print("You lost", attack, "attack")


def armorAdd(name, defense, evasiveness):
    global playerDefense
    global playerEvasiveness

    addItem(name)
    playerDefense += defense
    playerEvasiveness += evasiveness
    print("You gained", defense, "armor.")
    if evasiveness != 0:
        print("You gained", evasiveness, "evasiveness.")


def armorRemove(name, defense, evasiveness):
    global playerAttack
    global playerEvasiveness

    removeItem(name)
    playerAttack -= defense
    playerEvasiveness -= evasiveness
    print("You lost", defense, "attack")
    if evasiveness != 0:
        print("You gained", evasiveness, "evasiveness.")


def stats():
    print("Attack:", playerAttack, "\nDefense:", playerDefense, "\nHealth", playerHealth, "\nEvasiveness", playerEvasiveness)