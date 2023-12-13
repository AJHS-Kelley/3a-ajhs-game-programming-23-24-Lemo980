import random

def rollDice(numRoll, sizeRoll):
    count = 0
    sum = 0
    while count < numRoll: 
        roll = random.randint (1, sizeRoll)
        #print(f"Roll # {count}: {roll}\n")
        sum += roll
        count += 1
    #print(sum)
    return sum

def rollDicePrint(numRoll, sizeRoll):
    count = 0
    sum = 0
    while count < numRoll: 
        roll = random.randint (1, sizeRoll)
        print(f"Roll # {count}: {roll}\n")
        sum += roll
        count += 1
    print(f"the sum is {sum} \n")
    return sum

def isExploding(roll, sizeRoll):
    if sizeRoll == roll:
        isExploding = True
    else:
        isExploding = False
    
    return isExploding

def isDouble(roll1, roll2):
    if roll1 == roll2:
        isDouble = True
    else: 
        isDouble = False
    return isDouble

roll1 = rollDice(1,6)
roll2 = rollDice(1,6)

print(f"The first roll is {roll1} and the second roll is {roll2}. \n")

if isDouble(roll1, roll2):
    print("It's a double!")
else:
    print("Womp womp, it's not a double")






















