#Monsters, ELiot Blanton, v0.0


class Monster:
    def __init__(self, name, attackPower, health):
        self.name = name
        self.attackPower = attackPower
        self.health = health
        self.experience = 50000

    def __str__(self):
        return f"The {self.name} has {self.health} health, deals {self.attackPower} damage per hit, and drops 50000 experience points when killed. \n"
    
    def isDeadly(self):
        print("This function will check if the monster is deadly or not.\n")
        if self.attackPower > 500:
            print("Be careful, monster is very deadly\n")
        else:
            print("Don't worry, this is a weak monster\n")

myMonster = Monster("Goblin", 1000, 150)
print(myMonster)
myMonster.isDeadly()


