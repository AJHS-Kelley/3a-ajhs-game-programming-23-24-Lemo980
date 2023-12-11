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
