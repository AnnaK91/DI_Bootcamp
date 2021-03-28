# Ask a user for his birthdate (specify the format, for example: DD/MM/YYYY) and then:
# 2 Display him a little cake, like this:
#        ___iiiii___
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~

# The number of candles should be the last cypher of his age, if he is 53, then add 3 candles.

# Bonus : If he was born on a leap year, display two cakes !



from datetime import datetime





today = datetime.today().strftime("%Y-%m-%d")
date_list = today.split("-")
print(today)



birthdate = input('What is your age? input format: year/month/day\n')

age_list = birthdate.split("/")

age = (int(date_list[0]) - int(age_list[0]))


if int(date_list[1]) > int(age_list[1]):
    print(age)

elif int(date_list[1]) == int(age_list[1]):
    if int(date_list[1]) > int(age_list[1]):
        print(age -1)
    else:
        print(age)
else:
    print(age -1)


print("|:H:a:p::y:|")
print("|___________|__")
print("|^^^^^^^^^^^^^^^^^|")
print("|:B:i:r:t:h:d:a:y:|")
print("|                 |")
print("~~~~~~~~~~~~~~~~~~~")


# birth_year = int(input("What's your birth year ? /YYYY/\n"))
# birth_month = int(input("What's your birth month ? /MM/\n"))
# birth_day = int(input("What's your birth day ? /DD/\n"))

# # d = datetime.datetime.today().day
# # m = datetime.datetime.today().month
# # y = datetime.datetime.today().year


# print(birth_year, birth_month, birth_day)