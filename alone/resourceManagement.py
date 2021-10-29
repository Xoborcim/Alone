# Sarim
import inventoryManagement
steps = 0
day = 0
hunger = 3
hungerSteps = 0
hungerDrain = 5
timeSteps = 12
playerDead = False


def step():
    global hungerSteps
    global steps
    steps += 1
    hungerSteps += 1
    print(steps)
    print(day)
    print(hunger)
    timeTracker()


def timeTracker():
    global timeSteps
    global hungerSteps

    if not playerDead:
        global steps
        global day
        global hunger
        global hungerDrain
        global hungerSteps

        if steps >= timeSteps:
            day += 1
            timeSteps += 12
        if hungerSteps >= hungerDrain:
            hunger -= 1
            hungerDrain += 5
        if day >= 14:
            gameOver("Your life was drained by the Earth. You feel your body lose energy. You can't di...")
        if hunger <= 0:
            gameOver("You starved to death")


# Sebastian if you consume food it refills your hunger
def consumeFood(food):
    global hungerDrain
    global hunger
    global hungerSteps

    if food == "Apple":
        if hunger < 3:
            inventoryManagement.removeItem(food)
            hungerDrain = 5
            hunger = 3
        else:
            inventoryManagement.removeItem(food)
            inventoryManagement.playerHealth = 10
    else:
        print("You can't eat that")


# Sebastian Checks the player's health
def healthCheck():
    if inventoryManagement.playerHealth <= 0:
        gameOver("You feel your body lose energy. You can't di...")

# Sebastian If the player dies it will print a custom game over text
def gameOver(message):
    print(message)
    exit()
