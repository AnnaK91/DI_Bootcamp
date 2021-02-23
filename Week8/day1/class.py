# class Human():

# name of classes are in CamelCase (not snake_case)


# executing a class creates a new istance

# class Human():
#     def sleep(self):
#         print("zzzz...")
# my_human = Human()
# bill = Human()
# matt = Human()
# bill.eye-color = "Green"

# class Human():
#     def __init__(self, eye_color, age):
#         print("a new human was born")
#         self.eye_color = eye_color
#         self.age = age
#     def sleep(self):
#         print("zzzz...")
# my_human = Human("green", 35)
# bill = Human("brown", 42)
# matt = Human("blue", 38)
# print(age)


class Human():
    def __init__(self, name, age, color_of_eyes,):
        self.name = name
        self.age = age
        self.eye_color = color_of_eyes
    def introduce(self):
        print(f"{self.name} is {self.age} years old and has {self.eye_color} eyes")

    # def set_eye_color(self, new_color):
    #     self.eye_color = new_color
    # This is how you change attribute
    
    def birthday(self):

        """
        Prints a happy birthday message and increments the age by 1
        :return:
        """
        print(f"Happy birthday {self.name}")
        self.age =+1

    def run(self, distance):





bill = Human("Bill", 42, "Green")
matt = Human("Matt", 22, "Brown")

# print(f"{bill.name} is {bill.age} years old and has {bill.eye_color} eyes")

# print(f"Bill is {bill.age} years old and has {bill.eye_color} eyes")
# print(f"Matt is {matt.age} years old and has {matt.eye_color} eyes")

# bill.set_eye_color("Blue")
# change the attribute

bill.birthday()
# matt.introduce()

# bill.eye_color = "Green"
# Better not tounct attributes outside the class
# Instead --> create a setter (new function)