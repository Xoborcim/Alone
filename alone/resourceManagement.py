# Sarim
steps = 0
day = 0
hunger = 3


def step():
    global steps
    steps += 1
    print(steps)


def timeTracker():
    global steps
    global day
    global hunger

    if steps > 12:
        day += 1
    elif steps > 5:
        hunger -= 1


def gameOver():
    print("You died of hunger")
    exit()
