class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Bombay(Cat):
    def sing(self, sounds):
        return f'{sounds}'


my_cats = []

my_cats.append(Bengal)
my_cats.append(Chartreux)
my_cats.append(Bombay)


#Don't understand 3 and 4


# Exercise 2 : Dogs
# Create a class named Dog with the attributes name, age, weight
# Implement the following methods for the class:
# bark: returns a string of “ barks”.
# run_speed: returns the dogs running speed (weight/age *10).
# fight : gets parameter of other_dog, returns string of which dog won the fight between them, whichever has a higher run_speed x weight should win.
# Create 3 dogs and use some of your methods


class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def bark(self):
        print(f'{self.name} barks')


    def run_speed(self):
        print (f'{self.name} is running with {self.weight / self.age*10} km/h')


Maxi = Dog("Maxi",10,20)


Maxi.run_speed()



