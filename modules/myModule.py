#Dice roll module, Eliot Blanton, v1.0
import random, time

def rollDice(numRoll, sizeRoll):
    count = 0
    sum = 0
    while count < numRoll: 
        roll = random.randint (1, sizeRoll)
        sum += roll
        count += 1
    return sum

def dispDice(numRoll, sizeRoll):
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
    if roll == sizeRoll:
        isExploding = True
    else:
        isExploding = False
    return isExploding

#Confirmed working on 12/13/23
def isDouble(roll1, roll2):
    if roll1 == roll2:
        isDouble = True
    else: 
        isDouble = False
    return isDouble



def getTime():
    return time.time()

def execTime(start, stop):
    return f"Execution Time: {stop - start} seconds."

















