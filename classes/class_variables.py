# Example 1: Class Variable
class Person:
    species = "Human"
    
    def __init__(self, name):
        self.name = name

p1 = Person("John")
p2 = Person("Jane")
print(p1.species)
print(p2.species)
print(Person.species)
print()


# Example 2: Counter with Class Variable
class Car:
    count = 0
    
    def __init__(self, brand):
        self.brand = brand
        Car.count += 1

c1 = Car("Toyota")
c2 = Car("BMW")
c3 = Car("Ford")
print("Total cars:", Car.count)
print()


# Example 3: Modify Class Variable
class MyClass:
    x = 5

MyClass.x = 10
obj = MyClass()
print(obj.x)
print()


# Example 4: Class Variable vs Instance Variable
class Person:
    nationality = "Norwegian"
    
    def __init__(self, name):
        self.name = name

p1 = Person("John")
p2 = Person("Jane")

Person.nationality = "Swedish"
print(p1.nationality)
print(p2.nationality)
print()


# Example 5: Constants with Class Variables
class Math:
    PI = 3.14159
    
    def circle_area(self, radius):
        return Math.PI * radius * radius

m = Math()
print("Area:", m.circle_area(5))
