# Example of defining functions in python

# Defining a basic function

# in python, we use the keyword def to define a function
# the function name is followed by parentheses and a colon

# the function name convention is to use lowercase words separated by underscores if it is more than one word
def my_function():
    # the body of the function is indented
    print("This function returns nothing, it just prints this line")
    
# the function ends when the indentation ends

# function with parameters
def my_function_with_args(username, greeting):
    print(f"Hello, {username}, from My Function!, I wish you {greeting}")
    
# functions can return values
def sum_two_numbers(a, b):
    return a + b

# functions using args and kwargs

def my_function_with_args_and_kwargs(username, greeting, *args, **kwargs):
    print(f"Hello, {username}, from My Function!, I wish you {greeting}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

# fuunction return multiple values

def sum_and_product(a, b):
    return a + b, a * b

# calling functions

my_function()

my_function_with_args("John Doe", "a good day")

x = sum_two_numbers(1, 2)
print(x)

my_function_with_args_and_kwargs("John Doe", "a good day", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8)

sum, product = sum_and_product(1, 2)

