#DNA Replication Game, Eliot Blanton, v0.0

#import entire module
import time, datetime #bringing the entire toolbox

#import a specific method from a module
from random import choice #bringing one specific tool

dnaBases = ["A", "T", "G", "C"] #Adenine, Thymine, Guanine, and Cytocine

def gameIntro() -> None:
    print("Welcome to the DNA sequence game!\nIn this game, you will match the RNA sequence to the DNA sequence you are given. \nU goes with T\nT goes with A\nG goes with C\nC goes with G")

def genDNA() -> str:
    basesGenerated = 0
    basesRequested = int(input("Please enter a positive integer value for the number of bases to generate.\n"))
    dnaSequence = ""

    while basesGenerated < basesRequested:
        dnaSequence += choice(dnaBases)
        basesGenerated += 1


    return dnaSequence

def doTranscription(dnaSequence: str) -> tuple:
    print(f"The DNA sequence is {dnaSequence}.\n")
    print("You need to enter the correct RNA sequence based on the DNA sequence.\n")
    print("Remember, the RNA base will have a U base to match with an A base from DNA.\n")
    #START TIMER
    rnaStart = time.time()
    rnaSequence = input("Please type the correct RNA sequence with no spaces, then press enter.\n").upper()
    rnaStop = time.time()
    rnaTime = rnaStop - rnaStart
    return (rnaSequence, rnaTime) #Tuples are ordered (index), Unchangable, allows duplicates

def checkSequence(dnaSequence: str, rnaSequence: str) -> bool:
    isMatch = False
    for rnaBase, dnaBase in zip(rnaSequence, dnaSequence):
        if rnaBase == "U" and dnaBase != "A":
            break
        elif rnaBase == "A" and dnaBase != "T":
            break
        elif rnaBase == "G" and dnaBase != "C":
            break
        elif rnaBase == "C" and dnaBase != "G":
            break
        else:
            isMatch = True

    return isMatch

def calcScore(rnaTime: float, dnaSequence: str) -> int:
    score = 0.0
    if rnaTime < 1.0:
        score += 100000
    elif rnaTime < 2.0:
        score += 95000
    elif rnaTime < 3.0:
        score += 90000
    elif rnaTime < 5.0:
        score += 70000
    elif rnaTime < 10.0:
        score += 50000
    elif rnaTime < 20.0:
        score += 30000
    elif rnaTime < 30.0:
        score += 10000
    elif rnaTime < 60.0:
        score += 7000
    elif rnaTime < 120.0:
        score += 2000
    else:
        score += 0

    if len(dnaSequence) >= 30:
        score *= 3.0
    elif len(dnaSequence) >= 25 :
        score *= 2.3
    elif len(dnaSequence) >= 20 :
        score *= 1.8
    elif len(dnaSequence) >= 15 :
        score *= 1.5
    elif len(dnaSequence) >= 10 :
        score *= 1.3
    else:
        score *= 1.1

    return score

def saveScore(dna: str, rna: str, rnaTime: float, score: int) -> None:
    firstName = input("What is your first name?")
    lastName = input("What is your last name?")
    fullName = firstName + " " + lastName

    #Saving files
    #step 1: Create filename
    fileName = "dnaReplicationScore" + fullName + ".txt"
    #dnaReplicationScoreEliotBlanton.txt
    # step 2: open file as variable
    saveData = open(fileName, "a")# first parameter: file name, second parameter: file mode
    #3 main file modes: 
    #"w" -- create file, if file exists, overwrites what is in the file.
    #"a" -- create file, if file exists, append to end of file
    #"x" -- create file, if file exists, exit with error message

    #step 3: write the data to the file
    saveData.write(f"\nScore generated on: {datetime.datetime.now()} \nTime taken: {rnaTime} \nPlayer Name: {fullName} \nDNA sequence: {dna} \nRNA sequence: {rna} \nScore: {score}\n\n")

    #step 4: close the file
    saveData.close()


#Function calls
gameIntro()
dna = genDNA()
rna = doTranscription(dna)
if checkSequence(dna, rna[0]):
    score = calcScore(rna[1], rna[0])
    saveScore(dna, rna[0], rna[1], score)
else: 
    print("Your RNA sequence did not correctly match. Please try again")
























































