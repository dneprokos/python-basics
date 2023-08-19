# Example of using exceptions in Python

# Exceptions are errors
try:
    a = 10
    b = 0
    c = None

    if (a > b):
        raise ValueError("a is greater than b") # Raise an exception. Can be any type of exception
    
    x = a / b
    print("Result is:", x)

except ZeroDivisionError as e: # Exception type. Can be any type of exception
    print("Error: ", e)
except ValueError as e: # Exception type. Can be any type of exception
    print("Error: ", e)
except Exception as e: # Exception type. Can be any type of exception
    print("Error: ", e)
except BaseException as e: # Exception type. Can be any type of exception
    print("Error: ", e)
finally: # This block is always executed
    print("Finally block is executed")