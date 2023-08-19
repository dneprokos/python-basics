# Example of arrays and lists in Python

# Arrays are used to store multiple values in one single variable:

fruits = [] # Empty list
listWithValues = ["apple", 1, True, ""] # List with values

# TODO: Append data to list
fruits.append("apple") # Add data to the end of the list
fruits.extend(["orange", "banana"]) # Add multiple data to the end of the list
print(fruits) # ['apple', 'orange', 'banana']

# TODO: Insert data at specific index
fruits.insert(1, "grape") # Add data at index 1
print(fruits) # ['apple', 'grape', 'orange', 'banana']

# TODO: Search for the data in the list
print("pear" in fruits) # False. Returns True if the data is found in the list. Otherwise, returns False
print(fruits.index("apple")) # True. Returns the index of the data. Will throw an error if the data is not found

# TODO: Modify data in the list
fruits[3] = "pear" # Change the data at index 3
print(fruits) # ['apple', 'grape', 'orange', 'pear']

# TODO: Remove data from the list
fruits.remove("apple") # Remove the data from the list
print(fruits) # ['grape', 'orange', 'pear']

# TODO: Empty the list
fruits.clear() # Empty the list

#TODO: lists can be created using the list() global function
# Difference between list() and [] is that list() can be used to create a list from an iterable object.
fruits = list(("apple", "orange", "banana")) # Create a list using the list() global function

nums = list(range(3, 99, 3)) # Create a list of numbers from 3 to 99 with a step of 3
print(nums) # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96]
