# Example of conditional statement 
#Run: python conditional_start.py

x = 10
y = 20
z = 30

# TODO: Define if-elif-else statement

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
elif z > x and z > y:
    print("z is greater than x and y")
else:
    print("x is equal to y")


# TODO: Use compact if-else statement format
print("x is greater than y") if x > y else print("x is less than or equal to y")

