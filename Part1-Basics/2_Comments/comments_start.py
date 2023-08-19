'''This is python program to demonstrate the use of comments in python
It contains both single line and multi-line comments
You can access it directly via the __doc__ attribute of the module
Comments can be placed in functions, classes, modules, etc.
'''

def main():
    """This is a function that prints Hello World!
    It is a multi-line comment
    """
    # TODO: Add document string that contain a multi-line comment
    print(main.__doc__)

    # The python comments are created using the hash symbol
    print("Hello World!")

if __name__ == "__main__":
    main()