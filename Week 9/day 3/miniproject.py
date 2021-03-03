class Character:
    def __init__(self, life, attack):
        life = 20


        Python Instructor20:48
list_of_everyone = []
while True:
    personal_info = input('Please enter your name, age and score, seperated by commas. If there are no more, enter "quit"')
    if personal_info == 'quit':
        break
    else :
        personal_info_tuple = tuple(personal_info.split(', '))
        list_of_everyone.append(personal_info_tuple)
sorted_list = sorted(list_of_everyone, key=lambda tup: (tup[0], tup[1], tup[2]))
print(sorted_list)