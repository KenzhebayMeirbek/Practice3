# Example 1: Arbitrary Arguments (*args)
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
print()


# Example 2: Sum with *args
def sum_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_numbers(1, 2, 3))
print(sum_numbers(10, 20, 30, 40))
print()


# Example 3: Arbitrary Keyword Arguments (**kwargs)
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
print()


# Example 4: Print Info with **kwargs
def print_values(**data):
    for key, value in data.items():
        print(key + ": " + str(value))

print_values(name = "John", age = 36, country = "Norway")
print()


# Example 5: Combining Regular, *args, and **kwargs
def my_function(name, *args, **kwargs):
    print("Name:", name)
    print("Args:", args)
    print("Kwargs:", kwargs)

my_function("John", 100, 200, age = 36, city = "Oslo")
