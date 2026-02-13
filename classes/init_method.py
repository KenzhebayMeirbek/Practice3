# Example 1: Create a class with __init__()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)
print()


# Example 2: __init__() with print statement
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("A new person object has been created")

p1 = Person("John", 36)
print()


# Example 3: __init__() with default value
class Person:
    def __init__(self, name, age = 18):
        self.name = name
        self.age = age

p1 = Person("John", 36)
p2 = Person("Anna")
print(p1.name, p1.age)
print(p2.name, p2.age)
print()


# Example 4: __init__() with calculation
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = 3.14 * radius * radius

c1 = Circle(5)
print("Radius:", c1.radius)
print("Area:", c1.area)
print()


# Example 5: __init__() with list
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
    
    def add_grade(self, grade):
        self.grades.append(grade)

s1 = Student("John")
s1.add_grade(85)
s1.add_grade(90)
print(s1.name)
print(s1.grades)
