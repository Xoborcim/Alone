inventory = []
maxInventory = 1


# Sebastian, Adds item to your inventory if you have room
def addItem(item):
    global inventory
    if len(inventory) <= maxInventory:
        inventory.append(item)
    else:
        print("Your inventory full")


# Sebastian, Removes item from your inventory if you have that item
def removeItem(item):
    global inventory
    if item in inventory:
        inventory.remove(item)
    else:
        print("You don't have this item")


# Sebastian, Prints your inventory
def showInventory():
    print("Inventory:\n", inventory)
