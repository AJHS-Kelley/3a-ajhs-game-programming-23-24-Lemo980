#DNA Replication Game, Eliot Blanton, v0.0a

#import entire module
import time, datetime #bringing the entire toolbox

#import a specific method from a module
from random import choice #bringing one specific tool

dnaBases = ["A", "T", "G", "C"] #Adenine, Thymine, Guanine, and Cytocine

def gameIntro() -> None:
    pass

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
    print("Remember, the RNA base will have a U bawse to match with an A base from DNA.\n")
    #START TIMER
    rnaStart = time.time()
    rnaSequence = input("Please type the correct RNA sequence with no spaces, then press enter.\n")
    rnaStop = time.time()
    rnaTime = rnaStop - rnaStart
    return (rnaSequence, rnaTime) #Tuples are ordered (index), Unchangable, allows duplicates

# dna = genDNA()
# print(dna)

dna = genDNA()
print(dna)

rna = genRNA(dna)
print(rna)


























































