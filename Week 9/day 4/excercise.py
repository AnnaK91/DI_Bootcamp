Create a class Human, it has the following attributes:

name (str)
age (int)
living_place (Building - Default is None)
Create another class Building, it has the following attributes:

address (str)
inhabitants (List of Human objs - Default is empty)
Create a class City, it has the following attributes:

name (str)
buildings (List of Building objs - Default is empty)
Add the move(self, building) method to the Human class, it sets the living place of this human to the building and add this human to the building inhabitants.
Add the construct(self, address) method to the City class, it adds a building at the referenced address.
Add the info(self, address) method to the City class, it displays the number of buildings and the mean age of the citizens.


class Human:
    def __init__(self, name, age, living_place):
        self.name = name
        self.age = age
        self.living_place = None


class Building():
    def __init__(self, address, inhabitants):
        self.address = address
        self.inhabitants = []


class City:
    def __init__(self, name, buildings):
        self.name = name
        self.buildings = []
        