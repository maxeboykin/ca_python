# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# -*- coding: utf-8 -*-

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


def square(num):
    numSquared = num * num
    return numSquared


print(square(2))
name = input("What is your name?")
print('Very nice to meet you, ', name, '!')
print(f'Very nice to meet you, {name.upper()}!')
print('Very nice to meet you, {}!'.format(name))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
