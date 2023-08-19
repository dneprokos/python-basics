# Example file for working with lambda expressions

data = [10, 6, 23, 1, 9, 2, 36, 8, 7, 5, 4]

# reular sort

print("Sorted data: ")
result = sorted(data)
print(result)

# sort with lambda
print("Sorted data with lambda: ")
result = sorted(data, key=lambda x: str(x)[0])
print(result)

