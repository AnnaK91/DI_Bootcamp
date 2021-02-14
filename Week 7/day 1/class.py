def calculation(a,b):
    return a+b, a-b

example = calculation(5,100)

print(example)



def say_hi_group(name_list):
    for name in name_list:
        print(f'hello {name}')

names = ['Arica', 'Andrew', 'Othello']

say_hi_group(names)


def add_name(name_list, new_name):
    name_list.append(new_name)

add_name(names, "Kitty")

print(names)