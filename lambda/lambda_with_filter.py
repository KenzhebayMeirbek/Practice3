# Example 1: Filter numbers greater than 10
numbers = [5, 12, 17, 8, 25, 3, 14]
result = list(filter(lambda x: x > 10, numbers))
print(result)
print()


# Example 2: Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)
print()


# Example 3: Filter by string length
words = ["cat", "elephant", "dog", "butterfly", "ant"]
long_words = list(filter(lambda x: len(x) > 5, words))
print(long_words)
print()


# Example 4: Filter positive numbers
numbers = [-5, 3, -2, 0, 7, -1, 10]
positive = list(filter(lambda x: x > 0, numbers))
print(positive)
print()


# Example 5: Combine filter and map
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(result)
