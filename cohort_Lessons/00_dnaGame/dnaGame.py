#DNA Replication Game, Eliot Blanton, v0.0a

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

def genRNA(dnaSequence: str) -> tuple:
    print(f"The DNA sequence is {dnaSequence}.\n")
    print("You need to enter the correct RNA sequence based on the DNA sequence.\n")
    print("Remember, the RNA base will have a U base to match with an A base from DNA.\n")
    #START TIMER
    rnaStart = time.time()
    rnaSequence = input("Please type the correct RNA sequence with no spaces, then press enter.\n")
    rnaStop = time.time()
    rnaTime = rnaStop - rnaStart
    return (rnaSequence, rnaTime) #Tuples are ordered (index), Unchangable, allows duplicates

def checkSequence(dnaSequence: str, rnaSequence: str) -> bool:
    isMatch = False
    for rnaBase, dnaBase in zip(rnaSequence, dnaSequence):
        if rnaBase == "U" and dnaBase != "T":
            break
        elif rnaBase == "T" and dnaBase != "A":
            break
        elif rnaBase == "G" and dnaBase != "C":
            break
        elif rnaBase == "C" and dnaBase != "G":
            break
        else:
            isMatch = True

    return isMatch

def calcScore(time: float, dnaSequence: str) -> int:
    score = 0.0
    if time < 1.0:
        score += 100000
    elif time < 2.0:
        score += 95000
    elif time < 3.0:
        score += 90000
    elif time < 5.0:
        score += 70000
    elif time < 10.0:
        score += 50000
    elif time < 20.0:
        score += 30000
    elif time < 30.0:
        score += 10000
    elif time < 60.0:
        score += 7000
    elif time < 120.0:
        score += 2000
    else:
        score += 0

    if len(dnaSequence) >= 30:
    score *= 2.3
    if len(dnaSequence) >= 25 :
    score *= 2.0
    if len(dnaSequence) >= 20 :
    score *= 1.8
    if len(dnaSequence) >= 15 :
    score *= 1.6
    if len(dnaSequence) >= 10 :
    score *= 1.4
    if len(dnaSequence) >= 5 :
    score *= 1.2





 



# dna = genDNA()
# print(dna)

gameIntro()

dna = genDNA()
print(dna)

rna = genRNA(dna)
print(rna)

print(checkSequence(dna, rna[0]))
























































