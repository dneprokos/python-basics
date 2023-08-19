# Example of using the loops

# TODO: define a for loop

for i in range(10):
    print(i, end=' ')

print('\n------------------')

for i in range(-5, 5, 2):
    print(i, end=' ')

print('\n------------------')

# ------------------

# TODO: use a for loop over a collection
thestring = "Hello World!"

for c in thestring:
    print(c + ', ', end='')

print('\n------------------')

# ------------------

# TODO: Use enumerate() function to get index

for i, c in enumerate(thestring):
    print(i, c)

print('\n------------------')

# ------------------

# TODO: use a while loop that exits on a condition. The is no do-while loop in Python

x = 0

while x < 10:
    print(x, end=' ')
    x += 1

print('\n------------------')

# ------------------