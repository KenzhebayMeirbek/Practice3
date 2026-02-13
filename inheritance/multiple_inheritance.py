# Example 1: Basic Multiple Inheritance
class Father:
    def gardening(self):
        print("I enjoy gardening")

class Mother:
    def cooking(self):
        print("I love cooking")

class Child(Father, Mother):
    pass

c = Child()
c.gardening()
c.cooking()
print()


# Example 2: Multiple Inheritance with __init__()
class A:
    def __init__(self):
        print("A init")

class B:
    def __init__(self):
        print("B init")

class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)

obj = C()
print()


# Example 3: Method Resolution Order (MRO)
class A:
    def method(self):
        print("A method")

class B(A):
    def method(self):
        print("B method")

class C(A):
    def method(self):
        print("C method")

class D(B, C):
    pass

d = D()
d.method()
print("MRO:", [cls.__name__ for cls in D.__mro__])
print()


# Example 4: Diamond Problem
class A:
    def method(self):
        print("A method")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

d = D()
d.method()
print()


# Example 5: Practical Multiple Inheritance
class Flyable:
    def fly(self):
        print("I can fly")

class Swimmable:
    def swim(self):
        print("I can swim")

class Duck(Flyable, Swimmable):
    def quack(self):
        print("Quack!")

duck = Duck()
duck.fly()
duck.swim()
duck.quack()
