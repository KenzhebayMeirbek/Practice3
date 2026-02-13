# Example 1: Double each number
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)
print()


# Example 2: Square each number
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)
print()


# Example 3: Convert to uppercase
words = ["apple", "banana", "cherry"]
upper = list(map(lambda x: x.upper(), words))
print(upper)
print()


# Example 4: Add two lists
a = [1, 2, 3, 4]
b = [10, 20, 30, 40]
result = list(map(lambda x, y: x + y, a, b))
print(result)
print()


# Example 5: Format strings
prices = [100, 200, 300]
formatted = list(map(lambda x: "$" + str(x), prices))
print(formatted)
