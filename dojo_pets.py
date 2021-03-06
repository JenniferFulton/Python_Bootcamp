# implement __init__( name , type , tricks ):
# implement the following methods:
# sleep() - increases the pets energy by 25
# eat() - increases the pet's energy by 5 & health by 10
# play() - increases the pet's health by 5
# noise() - prints out the pet's sound

class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 0
        self.health = 0
    
    def sleep(self):
        self.energy += 25
        return self
    
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    
    def play(self):
        self.health += 5
        return self

    def noise(self,noise):
        print(noise)
        return self

# implement __init__( first_name , last_name , treats , pet_food , pet )
# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
# feed() - feeds the ninja's pet invoking the pet eat() method
# bathe() - cleans the ninja's pet invoking the pet noise() method

class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , pet=Pet("Sophie","Doodle", "Smile")):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self
    
    def feed(self):
        self.pet.eat()
        return self
    
    def bathe(self):
        self.pet.noise(noise="WOOF!")
        return self

    def stats(self):
        print(f"{self.pet.name}'s Health: {self.pet.energy}")
        print(f"{self.pet.name}'s Health: {self.pet.health}")

Lucky = Pet("Lucky","Golden","roll-over")
Jen = Ninja("Jennifer","Fulton","softies","merrick", Lucky)

Jen.walk().feed().bathe().stats()