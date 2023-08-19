# Example of magic methods in Python

class magicmethods():
    def __init__(self, name, size):
        self._name = name
        self._size = size

    # __str__ is used to return a string representation of the object. Different from __repr__ in that it is meant to be readable
    def __str__(self):
        return f"{self._name} is {self._size} feet tall"
    
    # __repr__ is used to return a string representation of the object. Different from __str__ in that it is meant to be unambiguous
    def __repr__(self):
        return f"magicmethods class(name:{self._name}), (size:{self._size})"
    
    # __eq__ is used to compare two objects. It is used when the == operator is used
    def __eq__(self, other):
        return self._name == other.name and self._size == other.size

    # __gt__ is used to compare two objects. It is used when the > operator is used
    def __gt__(self, other):
        return self._size > other.size
    
    # __lt__ is used to compare two objects. It is used when the < operator is used
    def __lt__(self, other):
        return self._size < other.size
    
    # __ge__ is used to compare two objects. It is used when the >= operator is used
    def __ge__(self, other):
        return self._size >= other.size
    
    # __le__ is used to compare two objects. It is used when the <= operator is used
    def __le__(self, other):
        return self._size <= other.size
    
    # __add__ is used to add two objects. It is used when the + operator is used
    def __add__(self, other):
        return self._size + other.size
    
    # __sub__ is used to subtract two objects. It is used when the - operator is used
    def __sub__(self, other):
        return self._size - other.size
    
    # __mul__ is used to multiply two objects. It is used when the * operator is used
    def __mul__(self, other):
        return self._size * other.size
    
    # __truediv__ is used to divide two objects. It is used when the / operator is used
    def __truediv__(self, other):
        return self._size / other.size
    
    # __floordiv__ is used to divide two objects. It is used when the // operator is used
    def __floordiv__(self, other):
        return self._size // other.size
    
    # __mod__ is used to divide two objects. It is used when the % operator is used
    def __mod__(self, other):
        return self._size % other.size
    
    # __pow__ is used to divide two objects. It is used when the ** operator is used
    def __pow__(self, other):
        return self._size ** other.size
    
    # __and__ is used to divide two objects. It is used when the & operator is used
    def __and__(self, other):
        return self._size & other.size
    
    # __or__ is used to divide two objects. It is used when the | operator is used
    def __or__(self, other):
        return self._size | other.size
    
    # __xor__ is used to divide two objects. It is used when the ^ operator is used
    def __xor__(self, other):
        return self._size ^ other.size

mm1 = magicmethods("mm1", 1)
mm2 = magicmethods("mm2", 2)
mm3 = magicmethods("mm1", 1)

print(mm1) # Will print the __str__ method
print(repr(mm1)) # Will print the __repr__ method
print(mm1 == mm2) # Will print False
print(mm1 == mm3) # Will print True
print(mm1 > mm2) # Will print False
print(mm1 < mm2) # Will print True
print(mm1 >= mm2) # Will print False
print(mm1 <= mm2) # Will print True
print(mm1 + mm2) # Will print 3
print(mm1 - mm2) # Will print -1
print(mm1 * mm2) # Will print 2
print(mm1 / mm2) # Will print 0.5
print(mm1 // mm2) # Will print 0. Will round down to nearest integer
print(mm1 % mm2) # Will print 1. Will return the remainder of the division
print(mm1 ** mm2) # Will print 1. Will return the result of the exponentiation
print(mm1 & mm2) # Will print 0. Will return the result of the bitwise AND operation
print(mm1 | mm2) # Will print 3. Will return the result of the bitwise OR operation
print(mm1 ^ mm2) # Will print 3. Will return the result of the bitwise XOR operation