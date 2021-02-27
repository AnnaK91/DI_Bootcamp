class Human:
    
    def __init__(self, name, age, color_of_eyes, speed):
        self.name = name
        self.age = age
        self.eye_color = color_of_eyes
        self.speed = speed

        self.passenger_of = None

    def introduce(self):
        print(f"{self.name} has {self.eye_color} eyes and is {self.age} years old")

    def set_eye_color(self, new_color):
        self.eye_color = new_color

    def birthday(self):
        """
        Prints a happy birthday message and increments the age by 1
        :return:
        """
        print(f"Happy birthday {self.name} !")
        self.age += 1

    def run(self, distance):
        """
        Return the time that it takes to this human to run this distance
        (reminder time = distance/speed)
        :param distance: distance in km
        :return:
        """
        return distance/self.speed

    def say_hello(self, other):
        """
        Say hello to another human
        :param other: (Human) the human to say hello to
        """
        print(f"{self.name} says hello to {other.name}")

    def is_older(self, other):
        """
        Checks if this human is older than the other
        It should print someething like:
            "Bill (42) is older than matt (22)"
        :param other: (Human)
        :return:
        """

        if self.age > other.age:
            # Self is older
            print(f"{self.name} ({self.age}) is older than {other.name} ({other.age})")

        elif other.age > self.age:
            # The other is older
            print(f"{other.name} ({other.age}) is older than {self.name} ({self.age})")

        else:
            print(f"{self.name} and {other.name} are both {self.age}")

    def race(self, other, distance):
        """
        Make a race between two humans
        It should print something like:
            "Bill arrived first (in 6 seconds), Matt arrived after 8 seconds"
        :param other:
        :param distance: distance to run
        :return:
        """

        self_time = self.run(distance)
        other_time = other.run(distance)

        if self_time < other_time:
            print(f"{self.name} arrived first ({self_time} seconds), {other.name} arrived after {other_time} seconds")
        elif other_time < self_time:
            print(f"{other.name} arrived first ({other_time} seconds), {self.name} arrived after {self_time} seconds")
        else:
            print(f"{self.name} and {other.name} both arrived in {self_time} seconds")

class Car:

    def __init__(self, color, manufacturer):
        self.color = color
        self.manufacturer = manufacturer

        self.travelled_km = 0
        self.passengers = []

    def add_passenger(self, passenger):
        """add a paggenger to the car"""

        self.passengers.append(passenger)

    def print_info(self):
        print(f"This {self.color} {self.manufacturer} travelled {self.travelled_km} km")

    def travel(self, distance):
        # Print we're travelling
        print(f"The car is travelling {distance} km")

        # Adding the distance to current kilometers of the car
        self.travelled_km += distance

bill = Human("Bill", 17, "Blue", 9)
bills_car = Car("Red", "Toyota")

bills_car.add_passenger(bill)

print(bills_car.passengers)

print("Bill is a passenger of:", bill.passenger_of)