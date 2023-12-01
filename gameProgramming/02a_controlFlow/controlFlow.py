#control flow, Eliot Blanton, v0.4

#DECLARATIONS
favoriteColor = "blue"
luckyNumber = 7
myGPA = 3.0
myAge = 16
pineappleOnPizza = True

#if statement
if luckyNumber > 30: # luckyNumber > 30 is a CONDITIONAL EXPRESSION
    print("Wow, what a great number!")

if myGPA >= 3.8:
    print("Wow what a good GPA!")

#if-else statement

if myGPA >= 3.0:
    print("Congradulations on making the Honor roll!")
else:
    print("You did not make the honor roll.")

if pineappleOnPizza == True:
    print("You like Pinapple on pizza")
else:
    print("You do not like pineapple on pizza")

#if elif statement
if myAge >= 65:
    print("Please enjoy rerirement!")
elif myAge >= 55:
    print("You have earned a $10,000 bonus!")
elif myAge >= 40:
    print("You have earned a $5000 bonus!")
else:
    print("You have earned a $1000 bonus!")
#99% of the time check for highest values first.

#Nested if / elif  / else statements
if pineappleOnPizza == True:
    print("You have strange tastes. I bet you're old")
    if myAge >= 50:
        print("What was it like riding on a dinosaur to school?")
    else:
        print("Ok you're still young enough to be cool")
else:
    print("You eat pizza like a normal human")

if myAge < 0:
    print("You are a time traveler ")
    if pineappleOnPizza == True:
        print("You like pineapple on pizza.")
    else:
        print("What is wrong with you.")
else:
    print("You are not a time traveler.")

#while loop -- think musical chairs -- best used when you do not know how many times the loop will run.
# loopCounter = 0
# while loopCounter < 100:
#     print(f"The current loop count is {loopCounter}.")
#     loopCounter += 1

# while loopCounter >= 0:
#     print(f"The current loop count is {loopCounter}.")
#     loopCounter -= 1

loopCounter = 0
while loopCounter < 100:
    print(f"The current loop count is {loopCounter}.")
    if loopCounter % 2 == 0:
        print(f"{loopCounter} is even!")
    else:
         print(f"{loopCounter} is odd!")
    loopCounter += 1

#for loop -- think Go Fish! -- used when you know how many iterations are needed.
for eachNumber in range(10):
    #eachNumber is known as the iterable variable
    #range(x) specifies the numbers from 0 to x, NOT INCLUSIVE
    print(eachNumber)

