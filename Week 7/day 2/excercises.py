# Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter.
# Call the function, and make sure the message displays correctly.


# def display_message():
#     print("We're learning about python functions")

# display_message()

# Exercise 2: What’s Your Favorite Book ?
# Write a function called favorite_book() that accepts one parameter, title.
# The function should print a message, such as “One of my favorite books is Alice in Wonderland”.
# Call the function, making sure to include a book title as an argument in the function call.

# def favorite_book(title):
#     print("My favorite book is "+title)

# favorite_book("Lord Of The Rings")


# Exercise 3 : Some Geography
# Write a function called describe_city() that accepts the name of a city and its country.
# The function should print a simple sentence, such as “Reykjavik is in Iceland”.
# Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the default country.

# def describe_city(city, country = "Russia"):
#     print(city+ " is in "+country)

# describe_city("Reykjavik","Iceland")
# describe_city("St. Petersburg")


# Exercise 4 : Random
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message to the user, otherwise show a fail message and display both numbers

# import random

# def random_number(user_num):
#     random_number = random.randint(1, 100)

#     if user_num == random_number:
#         print("You got it!")
    
#     else:
#         print("Try again")

# random_number(6)

# Exercise 5 : Let’s Create Some Personalized Shirts !
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt.
# Call the function a second time using keyword arguments.
# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

# def make_shirt(size, text):


#     Exercise 6 : Magicians …
# Make a list of magician’s names.
# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
# Call show_magicians() to see that the list has actually been modified.


def show_magicians(magic):
    for x in magic:
        print(x)

Magicians = ["Houdini", "Copperfield", "Lafayette"]

# show_magicians(Magicians)

def make_great(great):
    for i in range(len(great)):
        great[i] = great[i]+"The great"

make_great(Magicians)
show_magicians(Magicians)

