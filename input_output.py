def square(num):
    numSquared = num * num
    return numSquared


# print(square(2))
# name = input("What is your name?")
# print('Very nice to meet you, ', name, '!')
# print(f'Very nice to meet you, {name.upper()}!')
# print('Very nice to meet you, {}!'.format(name))

def greet_someone():
    name = input("What is your name?")
    hometown = input("And where are you from?")
    print('Very nice to meet you, {}!'.format(name), f'from {hometown}!')


greet_someone()
