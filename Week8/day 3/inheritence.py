# excercise

class Telephone():
    def __init_(self, phone_number, price):
        self.phone_number = phone_number
        self.price = price
    
    def call(self, number):
        print(f"{self.phone_number} is calling {number}")


class Smartphone(Telephone):
    def send_message(self, number, content):
        print(f"{self.phone_number} to {number}: {content}")
