import inventoryManagement
import random

import resourceManagement

health = 0
attack = 0
evasiveness = 0
perception = 0

enemiesKilled = 0


# Starts enemy encounter
def startEncounter(enemy):
    global health
    global attack
    global evasiveness
    global perception
    # Gets enemy's stats
    getStats(enemy)
    print("\033[1;31;40m\n")
    print("You encountered a", enemy)
    # Checks if Enemy is alive
    while health > 0:
        # Gives you your options
        print("Options: Fight, Eat, Check, Run")
        choice = input()
        # If the player fights it will check if you will hit the enemy, if it hits it will do damage based on attack
        # and if not it will print that your attack missed
        if choice.lower() == "fight":
            hit = random.randint(1, evasiveness)
            if hit == 1:
                health -= inventoryManagement.playerAttack
                print("Your attack hit for", inventoryManagement.playerAttack)
                if health <= 0:
                    health = 0
                    enemyDead()
                    return
            else:
                print("Your attack missed")
        # If you choose to run it will check if you are able to get away without being stopped
        elif choice.lower() == "run":
            ranaway = random.randint(1, perception)
            if ranaway == 1:
                print("You ran away")
                print("\033[1;32;40m\n")
                return
            else:
                print("You couldn't run away")
        # If you choose to check you will be able to see the enemies stats
        elif choice.lower() == "check":
            print("Health:", health, "\nAttack:", attack, "\nEvasiveness:", evasiveness, "\nPerception:", perception)
        # If you eat it will call the consume food function which checks if you're hunger is full, if it is you will heal
        # your health back and if not you will fill up your hunger
        elif choice.lower() == "eat":
            resourceManagement.consumeFood("Apple")
        else:
            print("Not an option")
        # After your turn the enemy will attack, it will first run a check to see if it hits then calculate damage done
        # Damage done is based on your defense
        # If defense blocks all of the damage you will take 0 damage and not negative damage
        print("The", enemy, "Attacks")
        enemyHit = random.randint(1, inventoryManagement.playerEvasiveness)
        if enemyHit == 1 and health > 0:
            if attack - inventoryManagement.playerDefense >= 0:
                enemyDamage = attack - inventoryManagement.playerDefense
                inventoryManagement.playerHealth -= enemyDamage
                print("You took", enemyDamage, "damage.")
            else:
                print("You took 0 damage.")
                enemyDamage = 0
            resourceManagement.healthCheck()
        else:
            print("You dodged the", enemy + "'s", "attack.")
        choice = ""


# If you win you will get an apple and the enemies killed variable will be increased
def enemyDead():
    global enemiesKilled
    print("You won! You got an apple!")
    inventoryManagement.addItem("Apple")
    enemiesKilled += 1
    print("\033[1;32;40m\n")


# Gets stats for the enemy
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
        health = 150
        attack = 15
        evasiveness = 5
        perception = 9999999
