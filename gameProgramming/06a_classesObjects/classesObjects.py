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

#A class is a blueprint to make an object
examplePerson1 = Person(37,"4'8\"", "black", "Gerald", 45, "April 03")
examplePerson2 = Person(43,"10'11\"", "red", "Harold", 863, "March 25")
print(examplePerson1)
print(examplePerson2)

#Changing properties after creating an object
print(examplePerson1.weight)
examplePerson1.weight = 245
print(examplePerson1.weight)