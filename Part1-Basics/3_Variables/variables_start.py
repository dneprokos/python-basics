# Example of using variables in Python

# TODO: Variables can be delcared without any explicit type
f = 0
print(f)
b = True
print(b)

# ---------------------------------------------------------

# TODO: Re-declaring the variable works
f = "abc"
print(f)

# ---------------------------------------------------------

# TODO: Error: variables of different types cannot be combined
print("String type" + 123) # Will throw an error - TypeError: can only concatenate str (not "int") to str

print("String type" + str(123)) # Will work

# ---------------------------------------------------------

# TODO: Global vs. local variables in functions

def someFunction():
    l # This is a local variable
    l = "def"
    print(l)

def someFunction2():
    global g # This is a global variable
    g = "def"
    print(g)

print(l) # Will throw an error - NameError: name 'l' is not defined
print(g) # Will print "def" as it is a global variable

# ---------------------------------------------------------

# TODO: Use del operator to remove a variable from memory

del f # This will remove the variable f from memory
print(f) # Will throw an error - NameError: name 'f' is not defined

# ---------------------------------------------------------


