# Example of using built-in functions

unsortedNumbers = [1, 5, 3, 2, 4, 7, 6, 9, 8]
names = ['John', 'Bob', 'Alice', 'Mary', 'Jack', 'Jill', 'Harry', 'Sally']
somestring = "Only those who dare to fail greatly can ever achieve greatly."

# TODO: len() - returns the length of the object
print(len(unsortedNumbers)) # 9
print(len(names)) # 8
print(len(somestring)) # 62

# TODO: min() and max() - returns the minimum or maximum value
print(min(unsortedNumbers)) # 1
print(max(unsortedNumbers)) # 9

# TODO: min() and max() also use a key function to provide comparable values
print(min(names, key=lambda n: len(n))) # Bob
print(max(names, key=lambda n: len(n))) # Harry

# TODO: sorted() - returns a new sorted list from the items in iterable
print(sorted(unsortedNumbers)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sorted(names)) # ['Alice', 'Bob', 'Harry', 'Jack', 'Jill', 'John', 'Mary', 'Sally']

# TODO: any() and all() - return True if any or all of the items in an iterable are True
print(any(unsortedNumbers)) # True
print(all(unsortedNumbers)) # True

# TODO: any() and all() also use a key function to provide comparable values
print(any(names, key=lambda n: len(n) > 4)) # True
print(all(names, key=lambda n: len(n) > 4)) # False

# TODO: sum() - returns the sum of all items in an iterable
print(sum(unsortedNumbers)) # 45

# TODO: sum() can start with an optional value. Optional value is added to the sum of items in an iterable
print(sum(unsortedNumbers, 10)) # 55

# TODO: enumerate() - returns an enumerate object. It contains the index and value of all the items in an iterable
print(list(enumerate(names))) # [(0, 'John'), (1, 'Bob'), (2, 'Alice'), (3, 'Mary'), (4, 'Jack'), (5, 'Jill'), (6, 'Harry'), (7, 'Sally')]
