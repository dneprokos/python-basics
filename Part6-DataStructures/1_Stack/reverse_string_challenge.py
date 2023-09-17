import stack_implementation

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
s = stack_implementation.Stack()

for char in string:
    s.push(char)

for char in range(s.size()):
    reversed_string += s.pop()

# Second approach
#while not s.is_empty():
    #reversed_string += s.pop()

print(reversed_string)
