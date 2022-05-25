# Inheritance is a feature of object-oriented programming (OOP) that enables the transfer of methods and
# properties of one class to another.
# Inheritance allows for reusability of code as well as extending
# the capability of new classes.
#

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f'{self.name} is {self.age} years old')

# The child class, also known as the derived class, is the class that
# inherits methods and properties from the parent class
# child class must contain the following:
# Name of the parent class in the definition of the child class
# Constructor of the parent class called within
# the constructor of the child class

class Person:
  def __init__(self, name, age):
      self.name = name
      self.age = age
  def print_info(self):
      print(self.name)
      print(self.age)

class Teacher(Person):
  def __init__(self, name, age, subject):
      self.subject = subject

      Person.__init__(self, name, age)


myTeacher = Teacher("Dr. Hirani", 49, "Computer Science")
myTeacher.print_info()
print(myTeacher.subject)

# Polymorphism in OOP is the concept
# of classes sharing methods with the same name
# This becomes useful when there are objects initiated
# from different classes that may share similar methods.

class Checking():
    def type(self):
        print('You have a checking account at the Codecademy Bank.')

    def balance(self):
        print('$20 left in your checking.')


class Savings():
    def type(self):
        print('You have a savings account at the Codecademy Bank.')

    def balance(self):
        print('$1000 left in your savings.')


account_a = Checking()
account_b = Savings()

for account in (account_a, account_b):
    account.type()
    account.balance()

