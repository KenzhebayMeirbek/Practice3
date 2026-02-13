# Example 1: super() in __init__()
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.firstname, x.lastname, x.graduationyear)
print()


# Example 2: super() with Methods
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barks")

d = Dog()
d.speak()
print()


# Example 3: super() in Method Chain
class A:
    def method(self):
        print("A method")

class B(A):
    def method(self):
        print("B method")
        super().method()

obj = B()
obj.method()
print()


# Example 4: super() with Multiple Levels
class Grandparent:
    def __init__(self):
        print("Grandparent")

class Parent(Grandparent):
    def __init__(self):
        print("Parent")
        super().__init__()

class Child(Parent):
    def __init__(self):
        print("Child")
        super().__init__()

c = Child()
print()


# Example 5: super() to Extend Functionality
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

s = Square(5)
print("Area:", s.area())
