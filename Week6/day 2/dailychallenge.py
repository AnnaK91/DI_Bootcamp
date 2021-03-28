# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”
# If it’s more than 10 characters, print a message which states “string too long”
# Then, print the first and last characters of the given text
# Construct the string character by character: Print the first character, then the second, then the third, until the full string is printed
# Example:
# The user enters “Hello Word”
# Then, you have to construct the string character by character
# H
# He
# Hel
# … etc
# Hello World
# Swap some characters around then print the newly jumbled string (hint: look into the shuffle method)
# Example:
# Hlrolelwod

import random

string = input("Please give me a word:")
first_letter = string[0]
last_letter = string[-1]

if len(string) < 10:
    print (f' The word "{string}" is not long enough.')

if len(string) > 10:
    print( f'The word "{string}" is too long')

    print(first_letter, last_letter)

else:

    for i in range(0, len(string)):
        print(string[:i+1])
    print(string.split())


random_word = string
new_list = list(random_word)
random.shuffle(new_list)
final_word = ''.join(new_list)
print(final_word)

