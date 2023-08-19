# Examples of data types in Python

# TODO: Text Type:	str
s = "This is a string"

print(s)

# ---------------------------------------------------------

# TODO: Numeric Types:	int, float, complex

i = 123 # int
print(i)

f = 123.456 # float
print(f)

c = 1j  # complex. Note: j is used to specify the imaginary part of a complex number
print(c)

# ---------------------------------------------------------

# TODO: Sequence Types:	list, tuple, range

l = ["a", "b", "c"] # list. Note: lists are ordered and changeable
print(l)

t = ("a", "b", "c") # tuple. Note: tuples are ordered and unchangeable
print(t)

r = range(6) # range. Note: ranges are ordered and unchangeable
print(r)

# ---------------------------------------------------------

# TODO: Mapping Type:	dict

d = {"name" : "John", "age" : 36} # dict. Note: dictionaries are unordered and changeable
print(d)

# ---------------------------------------------------------

# TODO: Set Types:	set, frozenset

s = {"a", "b", "c"} # set. Note: sets are unordered and unindexed
print(s)

fs = frozenset({"a", "b", "c"}) # frozenset. Note: frozensets are unordered and unindexed

# ---------------------------------------------------------

# TODO: Boolean Type:	bool

b = True # bool
print(b)

# ---------------------------------------------------------

# TODO: Binary Types:	bytes, bytearray, memoryview

bt = b"Hello" # bytes. Note: bytes are immutable sequences of single bytes (integers in the range of 0 <= x < 256)
print(bt)

ba = bytearray(5) # bytearray. Note: bytearray objects are mutable sequences of single bytes (integers in the range of 0 <= x < 256)
print(ba)

mv = memoryview(bytes(5)) # memoryview. Note: memoryview objects allow Python code to access the internal data of an object that supports the buffer protocol without copying
print(mv)

# ---------------------------------------------------------

# TODO: None Type:	None

n = None # None. Note: None is not the same as 0, False, or an empty string. None is a data type of its own (NoneType)
print(n)

# ---------------------------------------------------------

# TODO: Type Conversion

# Convert from one type to another with the int(), float(), and complex() methods

# Convert from one type to another with the str() method

# Convert from one type to another with the list(), tuple(), and set() methods

# Convert from one type to another with the dict() method

# Convert from one type to another with the bool() method

# ---------------------------------------------------------