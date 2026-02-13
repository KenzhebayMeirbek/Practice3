# Example 1: Creating a Function
def my_function():
    print("Hello from a function")

my_function()
print()


# Example 2: Arguments
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
print()


# Example 3: Parameters or Arguments?
def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Refsnes")
print()


# Example 4: Default Parameter Value
def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
print()


# Example 5: Passing a List as an Argument
def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)
