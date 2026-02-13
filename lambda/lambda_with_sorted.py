# Example 1: Sort by string length
words = ["apple", "banana", "cherry", "date"]
sorted_words = sorted(words, key = lambda x: len(x))
print(sorted_words)
print()


# Example 2: Sort tuples by second element
tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_tuples = sorted(tuples, key = lambda x: x[1])
print(sorted_tuples)
print()


# Example 3: Sort by absolute value
numbers = [-5, 3, -2, 8, -10, 1]
sorted_numbers = sorted(numbers, key = lambda x: abs(x))
print(sorted_numbers)
print()


# Example 4: Sort list of dictionaries
students = [
    {"name": "John", "age": 25},
    {"name": "Jane", "age": 22},
    {"name": "Dave", "age": 28}
]
sorted_students = sorted(students, key = lambda x: x["age"])
print(sorted_students)
print()


# Example 5: Reverse sort
numbers = [5, 2, 9, 1, 5, 6]
sorted_desc = sorted(numbers, reverse = True)
print(sorted_desc)
