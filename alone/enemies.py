import inventoryManagement
import random

import resourceManagement

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
    while health != 0:
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
                return
            else:
                print("You couldn't run away")
        elif choice.lower() == "check":
            print("Health:", health, "\nAttack:", attack, "\nEvasiveness:", evasiveness, "\nPerception:", perception)
        elif choice.lower() == "consume":
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
        health = 5
        attack = 3
        evasiveness = 1
        perception = 1
