# Example of palindrome challenge using scope blocks

# TODO: Create a palidrome function takes a string and returns True if it is a palindrome
def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]

# TODO: Call the function and print out the result
print(is_palindrome("Hello"))   # False
print(is_palindrome("level"))   # True