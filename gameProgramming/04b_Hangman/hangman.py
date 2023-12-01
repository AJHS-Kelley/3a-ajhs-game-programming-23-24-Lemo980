import random
wordList = 'dog cow tortilla bird extraterrestrial undeniable disasterous explosive fortitude alligator symbiosis runner wheat foggy vision king loops showered typed untouchable invincible frog pool marshmallow buffet flying envious skeleton cranium gallows'.split()
#.split() will split a string into seperate elements, by default set to space
#VARIABLE_NAMES that are ALL CAPS are constants and are not meant to change.
HANGMAN_BOARD = ['''
x-----x
      |
      |
      |
      |
      |
 0=========0 ''' , '''
x-----x
O     |
      |
      |
      |
      |
 0=========0 ''' , '''
x-----x
O     |
|     |
      |
      |
      |
 0=========0 ''' , '''
x-----x
O     |
|\    |
      |
      |
      |
 0=========0 ''' , '''
 x-----x
 O     |
/|\    |
       |
       |
       |
  0=========0 ''' , '''
 x-----x
 O     |
/|\    |
  \    |
       |
       |
  0=========0 ''' , '''
 x-----x
 O     |
/|\    |
/ \    |
       |
       |
  0=========0''']

def getRandomWord(wordList):
    wordIndex = random.randint(0 , len(wordList) - 1)
    #len(listName) - 1 is most common way to prevent index out of range errors.
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters , secretWord):
    print(HANGMAN_BOARD[len(missedLetters)])
    print()

    #Display incorrect guesses
    print('Missed letters:', end = ' ')
    for letter in missedLetters:
        print(letter, end = ' ')
    print()
    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
                # the : character is used to slice things into pieces
                #[:i] means slice from the start until index i
                #[i+1:] means slice from i+1 to the end
                #[startingPoint:endingPoint]
    for letter in blanks:
        print(letter, end = ' ')
    print()
     
def getGuess(alreadyGuessed):
    #Only allow: single character, A-Z only, hasnt been guessed
    while True:
        print('Please guess a letter and press enter')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter. \n')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter an English letter only')   
        elif guess in alreadyGuessed:
            print('This letter has already been guessed. Please enter a different letter')             
        else:
            return guess

def playAgain():
    print("Would you like to play again? Type yes or no then press enter.")
    return input().lower().startswith('y') # return true or false based on input

#Start the actual game
print('Let\'s play hangman!') # \ escapes special characters (allows for them to be printed)
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(wordList)
print('Secret testing word:' + secretWord)
gameIsDone = False

#GAME LOOP BEGINS HERE
while True: #99% of the time the game loop is done this way
    #Two ways to exit while True: return or break
    #Display board
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord: # is the guess in the secret word?
        correctLetters = correctLetters + guess

        #CHECK FOR VICTORY
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Congradulations! You have guessed correctly. \n')
            gameIsDone = True
    else: #missed letter guess
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_BOARD) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have used all of your guesses. You have failed')
            print('The secret word was ' + secretWord)
            gameIsDone = True
             
    if gameIsDone:
        if playAgain(): 
            secretWord = getRandomWord(wordList) # You did not have the parameter here. 
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
        else:
            break
                      












