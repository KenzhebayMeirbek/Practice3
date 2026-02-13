# Example 1: Override a Method
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()
print()


# Example 2: Call Parent Method
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")

d = Dog()
d.sound()
print()


# Example 3: Override __str__() Method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}({self.age})"

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    
    def __str__(self):
        return f"{self.name}({self.age}) - Grade: {self.grade}"

s = Student("John", 20, "A")
print(s)
print()


# Example 4: Override with Different Implementation
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

r = Rectangle(5, 10)
c = Circle(7)
print("Rectangle area:", r.area())
print("Circle area:", c.area())
print()


# Example 5: Polymorphism with Overriding
class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def start(self):
        print("Car starts with key")

class Motorcycle(Vehicle):
    def start(self):
        print("Motorcycle starts with button")

vehicles = [Car(), Motorcycle(), Vehicle()]
for v in vehicles:
    v.start()
