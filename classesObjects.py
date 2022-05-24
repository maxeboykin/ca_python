# A class is a data type that encapsulates information and functions as a blueprint for objects An object is an
# object is an instance of a class, which means the object contains
# everything from the class that it’s instantiated from
# Constructors are special functions that are executed when an object is instantiated
#  the __init__() function is used as the constructor and is called when creating an object.
# Destructors are special functions that are called when an object gets deleted. In Python,
# the __del__() method is commonly used as the destructor and is called when an object is deleted

class ClassSchedule:
    def __init__(self, course):
        self.course = course


first = ClassSchedule('Chemistry')
print(first.course)


class ClassSchedule:
    def __init__(self, course):
        self.course = course

    def __del__(self):
        print('You successfully deleted your schedule')

sched = ClassSchedule('Chemistry')
del sched


class ClassSchedule:
    def __init__(self, course, instructor):
        self.course = course
        self.instructor = instructor

    def display_course(self):
        print(f'Course: {self.course}, Instructor: {self.instructor}')


sched = ClassSchedule('Chemistry', 'Mr. Doe')  # initializing

sched.display_course()  # prints Course: Chemistry, Instructor: Mr. Doe
sched.course  # prints 'Chemistry

# Protected access modifiers, denoted with the prefix _,
# prevent members from being accessed outside the class, unless it’s from a subclass
# The variables course and instructor are now protected members in the class.

class ClassSchedule:
    def __init__(self, course, instructor):
        self._course = course  # protected
        self._instructor = instructor  # protected

    def display_course(self):
        print(f'Course: {self._course}, Instructor: {self._instructor}')


sched = ClassSchedule('Biology', 'Ms. Smith')
sched.display_course()

# Private access modifiers, denoted with the prefix __,
# declare members to be accessible within the class only.
#

class ClassSchedule:
    def __init__(self, course, instructor):
        self.__course = course  # private
        self.__instructor = instructor  # private

    def display_course(self):
        # public

        print(f'Course: {self.__course}, Instructor: {self.__instructor}')


sched = ClassSchedule('Biology', 'Ms. Smith')

sched.__course  # this will throw an Attribute Error because we're trying to access a private member

sched.display_course()  # this won't throw an Attribute Error because this method is public