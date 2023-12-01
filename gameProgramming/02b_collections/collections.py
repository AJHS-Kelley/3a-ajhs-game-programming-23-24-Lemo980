# #Adding Items
# playerInventory = []
# while len(playerInventory) <10:
#     item = input("Please choose an item to add to your inventory.\n")
#     playerInventory.append(item)
# playerInventory.sort()
# # . whatever is known as a method. It means "Do this to that".
# print(playerInventory)

# #Removing items
# while len(playerInventory) > 5:
#     item = input("Please choose an item to remove from your inventory.\n")
#     playerInventory.remove(item)
# playerInventory.sort()
# print(playerInventory)

#Fixed inventory system
# weaponList = [
#     True, #crossbow
#     False, #longsword
#     True, #dagger
#     True, #magic staff
#     False  #gauntlets
# ]
# #Each item in a list is called an element
# #The location of each element is called the index
# #First element is index[0]
# #index[-1] is the last element in a list
# weaponNum = 0
# while weaponNum < len(weaponList) :
#     if weaponNum == 0 and weaponList[0] == True:
#         print("Your character is equipped with a powerful steel crossbow.\n")
#     if weaponNum == 1 and weaponList[1] == True:
#         print("Your character is equipped with a heavy iron longsword.\n")
#     if weaponNum == 2 and weaponList[2] == True:
#         print("Your character is equipped with a small silver dagger.\n")   
#     if weaponNum == 3 and weaponList[3] == True:
#         print("Your character is equipped with a glowing magic staff.\n")
#     if weaponNum == 4 and weaponList[4] == True:
#         print("Your character is equipped with a pair of spiked gauntlets.\n")
#     weaponNum += 1

#Keys
# doorKeys = [
#     "red",
#     "green",
#     "purple",
#     "blue",
#     "yellow"
# ]
# item = input("Which key do you require?\n").lower()
# if item in doorKeys:
#     print(f"You have the {item} key!")
# else:
#         print(f"You do not have the {item} key!")

#Random enemy generator
enemyBase = [
    "Skeleton",
    "Gremlin",
    "Dragon",
    "Ghost",
    "Crab"
    ]
enemyType = [
    "Bomber",
    "Swordsman",
    "Wizard",
    "Assassin",
    "Brawler"
    ]
enemyPrefix = [
    "Giant",
    "Flying",
    "Flaming",
    "Armored",
    "Small"
    ]


import random

#Index range (0, 4)
enemyNames = []
while len(enemyNames) < 15:
    enemyBaseGen = enemyBase[random.randint(0,4)]
    enemyTypeGen = enemyType[random.randint(0,4)]
    enemyPrefixGen = enemyPrefix[random.randint(0,4)]
    newEnemy = enemyPrefixGen + " " + enemyBaseGen + " " + enemyTypeGen
    enemyNames.append(newEnemy)

    print(newEnemy)























