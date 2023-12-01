# Example Game Functions, Eliot Blanton, v8.2
import random
#Variable Declarations
weaponList = ["Wooden club", "Stone hammer", "Bone spear", "Magic staff of flame", "Steel greatsword", "Silver dagger", "Magical ice mace" ] #List of items in inventory
hitPoints = 150.5 #How much total health a player has
enemyList = ["Skeleton warrior", "Giant hog", "Dark mage", "Venomous serpent", "Goblin warrior", "Giant warrior", "Tree monster", "Werewolf"] #List of possible enemies
playerAlive = True #Is the player alive or not
playAgain = "y" #Does the player want to play again

#Function Definitions

def weaponChoice(weaponList): #Allows the user to choose a weapon then returns chosen weapon
    print("""Your weapon options are:
        1: Wooden club
        2: Stone hammer
        3: Bone spear
        4: Magic staff of flame
        5: Steel greatsword
        6: Silver dagger
        7: Magical ice mace""")
    equippedWeapon = weaponList[int(input("Please choose a weapon using a number 1 - 7 \n")) - 1]
    return equippedWeapon

def damage(equippedWeapon, enemy): #Determines how much damage an enemy will take when hit with different weapons then returns damage value
    if equippedWeapon == "Wooden club":
        if enemy == "Skeleton warrior":
            damage = 25
        elif enemy == "Giant hog":
            damage = 30
        elif enemy == "Dark mage":
            damage = 20
        elif enemy == "Venomous serpent":
            damage = 50
        elif enemy == "Goblin warrior":
            damage = 21
        elif enemy == "Giant warrior":
            damage = 10
        elif enemy == "Tree monster":
            damage = 5
        elif enemy == "Werewolf":
            damage = 15
    elif equippedWeapon == "Stone hammer":
        if enemy == "Skeleton warrior":
            damage = 30
        elif enemy == "Giant hog":
            damage = 35
        elif enemy == "Dark mage":
            damage = 25
        elif enemy == "Venomous serpent":
            damage = 60
        elif enemy == "Goblin warrior":
            damage = 21
        elif enemy == "Giant warrior":
            damage = 15
        elif enemy == "Tree monster":
            damage = 10
        elif enemy == "Werewolf":
            damage = 18
    elif equippedWeapon == "Bone spear":
        if enemy == "Skeleton warrior":
            damage = 10
        elif enemy == "Giant hog":
            damage = 60
        elif enemy == "Dark mage":
            damage = 30
        elif enemy == "Venomous serpent":
            damage = 20
        elif enemy == "Goblin warrior":
            damage = 24
        elif enemy == "Giant warrior":
            damage = 15
        elif enemy == "Tree monster":
            damage = 5
        elif enemy == "Werewolf":
            damage = 20
    elif equippedWeapon == "Magic staff of flame":
        if enemy == "Skeleton warrior":
            damage = 20
        elif enemy == "Giant hog":
            damage = 40
        elif enemy == "Dark mage":
            damage = 50
        elif enemy == "Venomous serpent":
            damage = 30
        elif enemy == "Goblin warrior":
            damage = 30
        elif enemy == "Giant warrior":
            damage = 35
        elif enemy == "Tree monster":
            damage = 90
        elif enemy == "Werewolf":
            damage = 30
    elif equippedWeapon == "Steel greatsword":
        if enemy == "Skeleton warrior":
            damage = 50
        elif enemy == "Giant hog":
            damage = 35
        elif enemy == "Dark mage":
            damage = 35
        elif enemy == "Venomous serpent":
            damage = 30
        elif enemy == "Goblin warrior":
            damage = 60
        elif enemy == "Giant warrior":
            damage = 80
        elif enemy == "Tree monster":
            damage = 30
        elif enemy == "Werewolf":
            damage = 30
    elif equippedWeapon == "Silver dagger":
        if enemy == "Skeleton warrior":
            damage = 15
        elif enemy == "Giant hog":
            damage = 15
        elif enemy == "Dark mage":
            damage = 15
        elif enemy == "Venomous serpent":
            damage = 20
        elif enemy == "Goblin warrior":
            damage = 18
        elif enemy == "Giant warrior":
            damage = 5
        elif enemy == "Tree monster":
            damage = 5
        elif enemy == "Werewolf":
            damage = 100
    elif equippedWeapon == "Magical ice mace":
        if enemy == "Skeleton warrior":
            damage = 30
        elif enemy == "Giant hog":
            damage = 35
        elif enemy == "Dark mage":
            damage = 60
        elif enemy == "Venomous serpent":
            damage = 30
        elif enemy == "Goblin warrior":
            damage = 50
        elif enemy == "Giant warrior":
            damage = 20
        elif enemy == "Tree monster":
            damage = 20
        elif enemy == "Werewolf":
            damage = 20
    return damage

def enemyAttack(enemy): #Sets attack damage for each enemy then returns the enemy's attack
    if enemy == "Skeleton warrior":
        enemyAttack = 40
    elif enemy == "Giant hog":
        enemyAttack = 35
    elif enemy == "Dark mage":
        enemyAttack = 50
    elif enemy == "Venomous serpent":
        enemyAttack = 60
    elif enemy == "Goblin warrior":
        enemyAttack = 50
    elif enemy == "Giant warrior":
        enemyAttack = 90
    elif enemy == "Tree monster":
        enemyAttack = 100
    elif enemy == "Werewolf":
        enemyAttack = 300
    return enemyAttack

def gameFunction(hitPoints, enemyAttack): #Chooses random enemy, runs weapon choosing function, damages the enemy based on the weapon, damages the player based on the enemy, then loops damaging until the player or enemy have been killed
    enemyHealth = 100 #Enemy can take 100 damage before dying
    playerAlive = True
    enemy = enemyList[random.randint(0, 7)] #Selects enemy from list
    print(f"A {enemy} crosses your path and begins battle")
    weapon = weaponChoice(weaponList)
    while playerAlive and enemyHealth > 0:
        enemyHealth -= damage(weapon, enemy) #Damages enemy
        if enemyHealth > 1:
            hitPoints -= enemyAttack(enemy) #Damages player
            if hitPoints > 0:
                playerAlive = True
            else:
                playerAlive = False
                print("You have died")
        else:
            print(f"You have killed the {enemy}")

while playAgain == "y": #Allows the user to decide to play again
    gameFunction(hitPoints, enemyAttack)
    print("Would you like to play again?")
    playAgain = input("Please type y for yes or n for no\n")
    if playAgain == "n":
        break

#













# Code Review by Zac Scott 