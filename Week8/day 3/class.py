"""
Car Class
Attributes:
    - color
    - manufacturer
    - travelled_km
Methods:
    - print_info(self) --> Prints some info about the car
    - travel(self, distance) --> Travel the given distance
            (print "The car travelled 65km" and increment travelled_km by 65)
"""


class Car():

    def __init__(self, color, manufacturer, travelled_km):
        self.color = color
        self.manufacturer = manufacturer
        self.km = travelled_km

    def info(self):
    
        print(f"My cars color is {self.color}, and made by {self.manufacturer}, and went {self.km}")

    def travel(self, distance):
        print(f"The car travelled {distance} km")
        self.km +=distance
my_car = Car("black","Nissan", 2332)
my_car.info()
my_car.travel(80)
 