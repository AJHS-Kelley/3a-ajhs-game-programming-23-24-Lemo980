# #Functions 10/18/23, Eliot Blanton

import random

# def functionName(): #Function signature
#     print("What is your name?")
#     name = input("Please type your name then press enter.\n")
#     print(f"Hello, {name}. \n")
    
# #Call the function
# functionName()

# def happyBirthday(numTimes, age):
#     count = 0
#     while count < numTimes:
#         print("Happy birthday\n")
#         count += 1
#     print(f"Wow you're {age} years old!\n")
    

# #happyBirthday(5, 16)

# def functionWithReturn(num1, num2):
#     sum = num1+ num2
#     quotient = sum / 5
#     return quotient #return immediately exits a function

# def functionWithoutReturn(num1, num2):
#     sum = num1+ num2
#     quotient = sum / 5

# example = functionWithoutReturn(5,10)
# print(example)
def rollDice(numRoll, sizeRoll):
     count = 0
     sum = 0
     while count < numRoll: 
         roll = random.randint (1,sizeRoll)
         sum += roll
         print(f"Roll # {count}: {roll}\n")
         count += 1
     print(sum)
     return sum

 #print("D4 rolls")
 #d4Sum = rollDice(10, 4)
 #print("D20 rolls")
 #d20Sum = rollDice(2, 20)

def genStat(): #Roll 4 D6, drop the lowest
    rolls = []
    count = 0
    while count < 4:
        rolls.append(rollDice (1, 6))
        count += 1
    
    rolls.sort()
    rolls.pop(0)
    print (sum(rolls))
    return (sum(rolls))

count = 0
while count < 10000:
    


strength = genStat()
print(f"Your strength: {strength}\n")






