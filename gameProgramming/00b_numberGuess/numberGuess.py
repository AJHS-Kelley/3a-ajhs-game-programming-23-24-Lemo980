#pick number from a range of possible numbers
#provide the player with X number of guesses, based on range of numbers
#First player to reach 3 points will be declared the winner
    #player guesses a number
    #compare guess to secret number
    #if the guess is correct what should happen?
        #award the player a point
        #print a win message.
    #if the guess is incorrect what should happen?
        #indicate if guess is higher or lower than the guess
    #if the player runs out of guesses what should happen?
        #give point to CPU
        #print a loss message


# Guess a number, Eliot Blanton, v0.7
import random, tracemalloc, winsound
from PIL import Image
tracemalloc.start()

#DECLARATIONS
secretNumber = -1 #range: 0 -- 100
playerName = ""
playerScore = 0
cpuScore = 0
guessesUsed = 0
playerGuess = -1
difficulty = ""
randNumMax = -1
numGuesses = -1

loserSound = 'sfx/numberGuess/LoserSound.wav'
winnerSound = 'sfx/numberGuess/WinnerSound.wav'

imageWin = Image.open('img/numberGuess/WinnerPic.jpg') # FIXED -- MR. KELLEY 
imageLose = Image.open('img/numberGuess/LoserPic.jfif') # SEE ABOVE EXAMPLE 

print("""
      
      *____________________________*
      |                           | 
      |     Guess the number!     |
      |                           |
      |            By:            |
      |         Eliot.B           |
      |                           |
      |           2023            |
      |                           |
     0=============================0
      """)

playerName = input("What should I call you?\n Type your name then press enter.\n")
#verify input
print(f"You want me to call you {playerName}. Is that correct?\n")
isCorrect = input ("Please type yes if correct and no if incorrect.\n")
if isCorrect == "yes":
    print(f"Ok {playerName}, lets continue!\n")
else:
    playerName = input("What should I call you? \n Type your name then press enter.\n")

print("There are three different difficulties: \n easy- 8 guesses on a number 1-10 \n normal- 6 guesses on a number 1-20 \n hard- 7 guesses on a number 1-100 \n")
difficulty = input("Please type easy, normal, or hard to choose a difficulty level.\n")

# This works, but a more efficient method is adding an else: block to your if-elif block.  Make the else: the default values.  
if difficulty != "easy" and difficulty != "normal" and difficulty != "hard":
    while difficulty != "easy" and difficulty != "normal" and difficulty != "hard":
        print("You did not type easy, normal, or hard. Check your spelling and capitalization and try again.\n")
        difficulty = input("Please type easy, normal, or hard to choose a difficulty level.\n")


if difficulty == "easy":
    numGuesses = 8
    randNumMax = 10
elif difficulty == "hard":
    numGuesses = 7
    randNumMax = 100
else:
    numGuesses = 6
    randNumMax = 20

#player guess
print(f"you need to guess a number from 0-{randNumMax} in {numGuesses} guesses!\n")

while playerScore != 3 and cpuScore != 3:
    #pass #tells python to skip a loop without giving an error.  
    secretNumber = random.randint(0 , randNumMax) #inclusive [Add space between , and randNumMax]
    #print(secretNumber)
    print(f"Player score: {playerScore}\n CPU score: {cpuScore}\n")  
    guessesUsed = 0
    for guesses in range(numGuesses):
        print(f"You have {numGuesses - guessesUsed} guesses left in this round.\n")
        playerGuess = int(input("Please type your guess then press enter.\n"))
        #int() converts whaterver you input into an integer
        print(f"You have chosen {playerGuess}. Lets see if its a match!\n")
        if playerGuess == secretNumber:
            playerScore += 1
            print("Correct! You have earned one point.\n")
            winsound.PlaySound(winnerSound, winsound.SND_FILENAME) # FIXED -- MR. KELLEY 
            break
        else:
            if playerGuess < secretNumber:
                print("Your guess is too low!\n")
            else:
                print("Your guess is too high!\n")
        guessesUsed += 1
        if guessesUsed >= numGuesses:
            cpuScore += 1
            winsound.PlaySound(loserSound, winsound.SND_FILENAME) # FIXED -- MR. KELLEY 
            print(f"The number was {secretNumber}\n")

if playerScore >= 3:
    print("You have won the game!")
    imageWin.show()


else:
    print("The CPU has won. You lose.")
    imageLose.show()

print("Memory usage (current, peak)")
print(tracemalloc.get_traced_memory())
tracemalloc.stop
