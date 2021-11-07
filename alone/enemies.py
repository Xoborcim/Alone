import inventoryManagement
import random

import resourceManagement

health = 0
attack = 0
evasiveness = 0
perception = 0

enemiesKilled = 0


def startEncounter(enemy):
    global health
    global attack
    global evasiveness
    global perception
    global enemiesKilled

    getStats(enemy)
    print("You encountered a", enemy)
    while health != 0:
        print("Options: Fight, Eat, Check, Run")
        choice = input()
        if choice.lower() == "fight":
            hit = random.randint(1, evasiveness)
            if hit == 1:
                health -= inventoryManagement.playerAttack
                print("Your attack hit for", inventoryManagement.playerAttack)
            else:
                print("Your attack missed")
        elif choice.lower() == "run":
            ranaway = random.randint(1, perception)
            if ranaway == 1:
                print("You ran away")
                return
            else:
                print("You couldn't run away")
        elif choice.lower() == "check":
            print("Health:", health, "\nAttack:", attack, "\nEvasiveness:", evasiveness, "\nPerception:", perception)
        elif choice.lower() == "eat":
            resourceManagement.consumeFood("Apple")
        else:
            "Not an option"
        print("The,", enemy, "Attacks")
        enemyHit = random.randint(1, inventoryManagement.playerEvasiveness)
        if enemyHit == 1:
            enemyDamage = attack - inventoryManagement.playerDefense
            inventoryManagement.playerHealth -= enemyDamage
            print("You took", enemyDamage, "damage.")
            resourceManagement.healthCheck()
        else:
            print("You dodged the", enemy + "'s", "attack.")
        choice = ""
    if health == 0:
        print("You won! You got an apple!")
        inventoryManagement.addItem("Apple")
        enemiesKilled += 1


def getStats(enemy):
    global health
    global attack
    global evasiveness
    global perception

    if enemy == "Goblin":
        # Goblin
        health = 3
        attack = 1
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
        health = 4
        attack = 3
        evasiveness = 1
        perception = 1
    elif enemy == "Sprite":
        health = 1
        attack = 2
        evasiveness = 5
        perception = 5
    elif enemy == "Yorbkx":
        health = 100
        attack = 10
        evasiveness = 3
        perception = 100
