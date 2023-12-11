#Classes and Objects, Eliot Blanton, v0.0


class Person: #Ckass names should be PascalCase
    def __init__(self, age, height, hairColor, name, weight, birthday ):
        #The self keyword refers to the specific object that you are dealing with.
        self.age = age
        self.height = height
        self.hairColor = hairColor
        self.name = name
        self.weight = weight
        self.birthday = birthday
    #__str__ method Format
    def __str__(self):
        return f"{self.name} is {self.age} years old. \n They have {self.hairColor} hair and weigh {self.weight} pounts. \n They were born on {self.birthday} and stands {self.height} tall."
    

    #Functions in a class
    def tooOld(self):
        print("Hello, this function will determine if you are too old to ride \n")
        print("If you are older than 25, you cannot ride this ride \n")
        if self.age > 25:
            print("You are too old, find a different ride \n")
        else:
            print("Welcome aboard \n")

    def tooHeavy(self):
        print("Hello, this function will determine if you are too heavy to ride \n")
        print("If you are heavier than 300 pounds, you cannot ride this ride \n")
        if self.weight > 300:
            print("You are too heavy, find a different ride \n")
        else:
            print("Welcome aboard \n")


#A class is a blueprint to make an object
examplePerson1 = Person(37,"4'8\"", "black", "Gerald", 45, "April 03")
examplePerson2 = Person(5,"10'11\"", "red", "Harold", 863, "March 25")

examplePerson2.tooOld()
examplePerson2.tooHeavy()
# print(examplePerson1)
# print(examplePerson2)

# #Changing properties after creating an object
# print(examplePerson1.weight)
# examplePerson1.weight = 245
# print(examplePerson1.weight)