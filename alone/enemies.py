import inventoryManagement
import random

health = 0
attack = 0
evasiveness = 0
perception = 0


def startEncounter(enemy):
    global health
    global attack
    global evasiveness
    global perception

    getStats(enemy)
    print("You encountered a", enemy)
    print(health)
    while health > 0 and inventoryManagement.playerHealth > 0:
        print("Options: Fight, Check, Run Away")
        choice = input()
        if choice.lower() == "fight":
            hit = random.randint(1, evasiveness)
            if hit == 1:
                health -= inventoryManagement.playerAttack
                print("Your attack hit for", inventoryManagement.playerAttack)
            else:
                print("Your attack missed")
        elif choice.lower() == "run away":
            ranaway = random.randint(1, perception)
            if ranaway == 1:
                print("You ran away")
                health = 0
            else:
                print("You couldn't run away")
        elif choice.lower() == "check":
            print("Health:", health, "Attack:", attack, "Evasiveness:", evasiveness, "Perception:", perception)
        else:
            "Not an option"
        print("The,", enemy, "Attacks")
        enemyHit = random.randint(1, inventoryManagement.player)
        if enemyHit == 1:
            inventoryManagement.playerHealth -= (inventoryManagement.playerDefense - attack)
        else:
            print()
        choice = ""


def getStats(enemy):
    global health
    global attack
    global evasiveness
    global perception

    print("got stats")

    if enemy == "Goblin":
        # Goblin
        health = 3
        attack = 2
        evasiveness = 4
        perception = 3
    elif enemy == "Slime":
        # Slime
        health = 2
        attack = 1
        evasiveness = 2
        perception = 2
    elif enemy == "Troll":
        # Troll
        health = 5
        attack = 3
        evasiveness = 1
        perception = 1
