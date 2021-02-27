# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age



#     def oldest_cat(*cats):
#         oldest_cat = ''
#         age = 0



# Dennis = Cat("Dennis", 10)
# Kornelia = Cat("Kornelia", 5)
# McFurry = Cat("McFurry", 1)


# Exercise 2 : Dogs
# Create a class Dog.
# In this class, create a method __init__, that takes two parameters : nameand height. This function instantiates two attributes, which values are the parameters.
# Create a method named bark that prints “ goes woof!”
# Create a method jump that prints the following “ jumps cm high!” where x is the height*2.
# Outside of the class, create an object davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog by calling the methods.
# Create an object sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog by calling the methods.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.


# class Dog():
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
    
#     def bark(self):
#         print(f"{self.name} goes woof!")

#     def jump(self):
#         print(f"{self.name} jumps {self.height*2} cm high!")

#     def biggest_dog(self)
#         if self.height > height

# my_dog = Dog("Blinky", 40)
# my_dog.bark()
# my_dog.jump()

# davids_dog = Dog("Rex", 50)
# davids_dog.bark()
# davids_dog.jump()

# saras_dog = Dog("Teacup", 20)
# saras_dog.bark()
# saras_dog.jump()



# Exercise 3 : Who’s The Song Producer ?
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics(a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on his own line.
# Create an object, for example:
# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# Then, call the method sing_me_a_song. The output should be:
# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven


# class Song():
#     def __init__(self, lyrics = []):
#         self.lyrics = lyrics
    
#     def sing_me_a_song(self):
#         for x in self.lyrics:
#             print(x)



# stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])


# stairway.sing_me_a_song()


# Exercise 4 : Afternoon At The Zoo
# Create a class Zoo
# In this class create a method __init__ that takes one parameter: zoo_name
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list, only if the new_animal isn’t already in the list.
# Create a method get_animals that prints all the of animals in the zoo.
# Create a method sell_animal that takes one parameter animal_sold. This method removes the animal from the list, only if he was already in the list.
# Create a method sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# { 
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }
# Create a method get_groups that prints the animal/animals inside each group.
# Create an object ramat_gan_safari and call all the methods.
# Tip: for each method, the argument should be the answer of the zoo keeper.
# Example

# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)

class Zoo:

animals = []

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
    
    def new_animal(name):

