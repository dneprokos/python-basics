# Example of using string functions

thesstring = "Only those who dare to fail greatly can ever achieve greatly."
alpha1 = "abcde"
alpha2 = "ABCDE"

# TODO: len() - returns the length of the string
print(len(thesstring)) # 62

# TODO: substring - returns a substring of the string
print(thesstring[0:4]) # Only
print(thesstring[5:9]) # those
print(thesstring[10:13]) # who

# TODO: concatenate - returns a concatenated string
print(alpha1 + alpha2) # abcdeABCDE

# TODO: interpolation - use the format() method to interpolate formatted arguments into the string
print("The first five letters of the alphabet are: {}{}".format(alpha1, alpha2)) # The first five letters of the alphabet are: abcdeABCDE

# TODO: in - returns True if a substring is found in the string
print("abc" in alpha1) # True

# TODO: not in - returns True if a substring is not found in the string
print("xyz" not in alpha1) # True

# TODO: case conversion - returns a string converted to lowercase or uppercase
print(thesstring.lower()) # only those who dare to fail greatly can ever achieve greatly.
print(thesstring.upper()) # ONLY THOSE WHO DARE TO FAIL GREATLY CAN EVER ACHIEVE GREATLY.

# TODO: strip - returns a string with whitespace removed from the start and end
print("   Hello World   ".strip()) # Hello World

# TODO: replace - returns a string with all occurrences of one substring replaced with another
print(thesstring.replace("greatly", "spectacularly")) # Only those who dare to fail spectacularly can ever achieve spectacularly.

# TODO: split - returns a list of substrings separated by the given delimiter
print(thesstring.split(" ")) # ['Only', 'those', 'who', 'dare', 'to', 'fail', 'greatly', 'can', 'ever', 'achieve', 'greatly.']

# TODO: join - returns a string that is all strings within our set (in this case a list) concatenated
print(" ".join(thesstring.split(" "))) # Only those who dare to fail greatly can ever achieve greatly.

# TODO: startswith() - returns True if the string starts with the given substring
print(thesstring.startswith("Only")) # True
print(thesstring.startswith("only")) # False

# TODO: endswith() - returns True if the string ends with the given substring
print(thesstring.endswith("greatly.")) # True
print(thesstring.endswith("greatly")) # False

# TODO: find() - returns the index of the first occurrence of a substring within the string
print(thesstring.find("greatly")) # 44

