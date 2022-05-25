intro = "My name is Jeff!"

print(intro[0])  # prints M

# apply slicing

intro[0:2]  # prints out 'My'. last index is non-inclusive.

intro[-5:-1]  # can also print out letters in the back. Code prints: 'Jeff'

intro1 = "My name is Jeff!"
intro2 = "Hello all!"
intro3 = "Hi there."
len(intro1)  # evaluates 16
len(intro2)  # evaluates 10
len(intro3)  # evaluates 9

intro = "My name is Jeff!"
print(intro.lower())  # prints 'my name is jeff!'
print(intro.upper())  # prints 'MY NAME IS JEFF!'
print(intro.title())  # prints 'My Name Is Jeff!'

intro = "My name is Jeff!"
print(intro.split())  # prints ['My', 'name', 'is', 'Jeff!']
print(intro.split('name'))  # prints ['My ', ' is Jeff!']
print(intro.split('!'))  # prints ['My name is Jeff', '']

# lists are ordered collections of items that can contain
# different data types such as strings, integers, float values
# and many more.

lst = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]

print(lst[0])  # prints abc

print(lst[4:6])  # prints [62, ['g', 'h', 'i']]

lst1 = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]
lst2 = [0, 1, 2, 3, 4]
lst3 = ['I love sushi so much!', 'I also love curry!']

print(len(lst1))  # prints 6
print(len(lst2))  # prints 5
print(len(lst3))  # prints 2

lst = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]
lst.append(99)  # appends 99 at the end of the list
print(lst)

lst.remove(62)  # removes 62 from the list
print(lst)

lst.pop()  # removes ['g', 'h', 'i']
print(lst)

lst.pop(0)  # removes 'abc' or the element at the given index
print(lst)

# Tuples are one of the built-in data structures in Python.
# Just like lists, tuples can hold a sequence of items and have a few key advantages:
# Tuples are more memory efficient than lists
# Tuples have a slightly higher time efficiency than lists
# This is mostly because tuples are immutable, meaning we can’t modify a tuple’s
# elements after creating one, and do not require an extra memory block like lists.
# Because of this, tuples are great to work with if you are working with data that
# won’t need to be changed in your code.
# Just like lists, tuples are sequences and can hold objects of different data types.

my_tuple = ('abc', 123, 'def', 456, 789, 'ghi')

print(my_tuple[0])  # prints abc
print(my_tuple[3:5])  # prints (456, 789)

# In contrast to lists, tuples have a limited number of built-in functions as they are immutable

my_tuple = ('abc', 123, 'def', 456, 789, 'ghi')
print(len(my_tuple))  # prints 6
# The built-in function max() returns the tuple’s maximum value.
# Note that this function requires all of the values to be of the same data type.
# If used with numerical values, the function returns the maximum value.
# If used with string values, the function returns the value at the tuple’s maximum index.

my_tuple = (65, 2, 88, 101, 25)
max(my_tuple)  # returns 101

my_tuple = ('abc', 'def', 'ghi', 'jkl')
max(my_tuple)  # returns jkl

my_tuple = ('abc', 234, 567, 'def')
# max(my_tuple)  # throws an error! all needs to be same data type

my_tuple = (65, 2, 88, 101, 25)
min(my_tuple)  # returns 2
my_tuple = ('abc', 'def', 'ghi', 'jkl')
min(my_tuple)  # returns abc
my_tuple = ('abc', 234, 567, 'def')
# min(my_tuple) # throws an error!

my_tuple = ('abc', 234, 567, 'def')
my_tuple.index('abc')  # returns 0
my_tuple.index(567)  # returns 2

my_tuple = ('abc', 'abc', 2, 3, 4)
my_tuple.count('abc')  # returns 2
my_tuple.count(3)  # returns 1

# Python, dictionaries are defined with curly brackets {}
#  keys must be an immutable data type such as strings, numbers or tuples.
#
#
#

groceries = {'fruits': ['mangoes', 'bananas', 'kiwis'],
             'protein': ['beef', 'pork', 'salmon'],
             'carbs': ['rice', 'pasta', 'bread'],
             'veggies': ['lettuce', 'cabbage', 'onions']}

party_planning = {'Yes': 10,
                  'No': 15,
                  'Maybe': 30,
                  'Location': 'Our Backyard',
                  'Date': '2022/05/01'}

party_planning['Location']  # returns 'Our Backyard'

len(party_planning)  # returns 5

# The built-in method update() takes in a dictionary as an argument to update an existing dictionary.
#  Any new key-value pairs will be added to the existing dictionary, but overlapping key-value pairs from
#  the new dictionary will overwrite the key-value pairs in the existing dictionary
#

shopping_list1 = {'jewelry': 'earrings', 'clothes': 'jeans', 'budget': 200}
shopping_list2 = {'shoes': 'sandals', 'budget': 350}

shopping_list1.update(shopping_list2)

print(shopping_list1)  # prints {'jewelry': 'earrings', 'clothes': 'jeans', 'budget': 350, 'shoes': 'sandals'}

shopping_list = {'jewelry': 'earrings', 'clothes': 'jeans', 'budget': 200}

shopping_list.keys()  # returns dict_keys(['jewelry', 'clothes', 'budget'])
shopping_list.values()  # returns dict_values(['earrings', 'jeans', 200])

# A set is an immutable, unordered collection of unique elements that can consist of integers, floats,
# strings and tuples. However, sets cannot hold mutable elements such as lists, sets or dictionaries.
#
#

set1 = {'Jenny', 26, 'Parker', 10.5}
print(set1)  # prints {10.5, 26, 'Jenny', 'Parker'}

#  Note that this will drop any duplicate elements in the list,
#  as sets can only contain unique, non-duplicated elements.

lst = ['Jenny', 26, 'Parker', 'Parker', 10.5]
set2 = set(lst)
print(set2)  # prints {10.5, 26, 'Jenny', 'Parker'}

# Sets do not have indexes or keys. We can use in to check to see if the element exists in the set

students = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry'}

print('Chau' in students)  # returns True

students = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry'}

students.add('George')
print('George' in students)  # returns True

# built-in method .update() takes in any iterable object,
# such as tuples, lists, dictionaries or sets, and adds the
# object to an existing set. Any duplicated elements will not be added.

students1 = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry'}
students2 = {'Alice', 'Lily', 'Zhuo', 'Amy', 'Jane'}

students1.update(students2)
print(students1)

# Similarly, the built-in method .union() takes an iterable object
# and joins the new object with the existing object:

students1 = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry'}
students2 = {'Alice', 'Lily', 'Zhuo', 'Amy', 'Jane'}

students3 = students1.union(students2)

students = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry'}
students.remove('Bridgette')
print(students)

count_down = set([9, 8, 7, 6, 5, 4, 3, 2, 1])

for num in count_down:
    print(num, 'seconds left!')


count_up = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

for num in count_up:
    print(num, 'seconds left!')