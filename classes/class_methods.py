# Example 1: Object Methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
print()


# Example 2: Methods with Parameters
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self, greeting):
        print(greeting + ", my name is " + self.name)

p1 = Person("John", 36)
p1.greet("Hello")
p1.greet("Hi")
print()


# Example 3: Methods with Return Value
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

r1 = Rectangle(5, 10)
print("Area:", r1.area())
print()


# Example 4: Multiple Methods
class Calculator:
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y

calc = Calculator()
print(calc.add(10, 5))
print(calc.subtract(10, 5))
print()


# Example 5: Static Methods
class Math:
    @staticmethod
    def add(x, y):
        return x + y

print(Math.add(5, 10))
