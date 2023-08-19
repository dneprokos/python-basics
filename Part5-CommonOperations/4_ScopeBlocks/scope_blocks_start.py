# Example of using scope blocks in Python

# TODO: Python uses "with" keyword to create scope blocks

# TODO: Use "with" to open a file and read data from it
with open("test.txt", "r") as file:
    print(file.read())

# TODO: Use "with" to open a file and count the number of lines in it
with open("test.txt", "r") as file:
    count = 0
    for line in file:
        count += 1
    print("Number of lines in the file:", count)

# TODO: Use "with" inside of class to create a scope block
class MyClass:
    def __init__(self):
        print("Constructor is called")
    def __enter__(self):
        print("Enter is called")
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit is called")

with MyClass() as obj:
    print("Inside the scope block")
    raise Exception("Exception is raised")
    print("This line is not executed")

