# Example of using keyword-only parameters in python

# Example of a function that uses keyword-only parameters
def my_func(arg1, arg2, suppress_exceptions=False):
    print(arg1, arg2, suppress_exceptions)

# Example of a function that uses keyword-only parameters
def my_func2(arg1, arg2, *, suppress_exceptions=False):
    print(arg1, arg2, suppress_exceptions)

my_func(1, 2, True) # 1 2 True

# my_func2(1, 2, True) # TypeError: my_func2() takes 2 positional arguments but 3 were given

my_func2(1, 2, suppress_exceptions=True) # 1 2 True