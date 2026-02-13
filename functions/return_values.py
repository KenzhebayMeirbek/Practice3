# Example 1: Return Values
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
print()


# Example 2: Simple Return
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
print()


# Example 3: Return Multiple Values
def get_person():
    name = "John"
    age = 36
    return name, age

name, age = get_person()
print(name)
print(age)
print()


# Example 4: Conditional Return
def is_adult(age):
    if age >= 18:
        return True
    else:
        return False

print(is_adult(20))
print(is_adult(15))
print()


# Example 5: Function Without Return (None)
def my_function(x):
    print(x + 5)

result = my_function(3)
print(result)
