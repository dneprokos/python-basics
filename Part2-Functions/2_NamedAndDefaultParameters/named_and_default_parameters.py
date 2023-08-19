# Example of using named and default parameters in python

# TODO: define a function with parameters and default values

def named_params(a, b, c=False):
    if c:
        print("'a' comes first")
        print(a)
        print(b)
    else:
        print("'b' comes first")
        print(b)
        print(a)

# TODO: call the function using named parameters

named_params(7, b="Hello", c=True) # 'a' comes first
named_params(b="Hello", a=7) # 'b' comes first 

