# Example 1: A lambda function that adds 10
x = lambda a : a + 10
print(x(5))
print()


# Example 2: A lambda function that multiplies argument a with argument b
x = lambda a, b : a * b
print(x(5, 6))
print()


# Example 3: A lambda function that sums argument a, b, and c
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
print()


# Example 4: Use lambda functions as an anonymous function inside another function
def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
print()


# Example 5: Lambda with sorted()
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key = lambda pair: pair[1])
print(pairs)
