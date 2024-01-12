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
    for rnaBase, dnaBase in zip(rnaBase, dnaBase):
        if rnaBase == "U" and dnaBase != "T":
            break
        elif rnaBase == "T" and dnaBase != "A":
            break
        elif rnaBase == "G" and dnaBase != "C":
            break
        elif rnaBase == "C" and dnaBase != "G":
            break
        elif rnaBase != "U" or "T" or "G" or "C":
            break
        else:
            isMatch = True



    return isMatch






# dna = genDNA()
# print(dna)

gameIntro()

dna = genDNA()
print(dna)

rna = genRNA(dna)
print(rna)

print(checkSequence(dna, rna))
























































