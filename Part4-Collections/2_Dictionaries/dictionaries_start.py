# Example of dictionaries in Python

# Dictionaries are used to store data values in key:value pairs.

# TODO: Create a new dictionary
fileDesc = {} # Empty dictionary

nums = {1: "one", 2: "two", 3: "three"} # Dictionary with values

# TODO: Add some items to the dictionary
fileDesc["pdf"] = "Portable Document Format" # Add a new key:value pair
fileDesc["txt"] = "Text File" # Add a new key:value pair
fileDesc["docx"] = "Microsoft Word Document" # Add a new key:value pair
print(fileDesc) # {'pdf': 'Portable Document Format', 'txt': 'Text File', 'docx': 'Microsoft Word Document'}

# TODO: Get the items count
print(f"Items count: {len(fileDesc)}") # Items count: 3

# TODO: Adding an existing key will change its value
fileDesc["txt"] = "Text File Format" # Change the value of the key
print(fileDesc) # {'pdf': 'Portable Document Format', 'txt': 'Text File Format', 'docx': 'Microsoft Word Document'}

# TODO: Check if the key exists
print("txt" in fileDesc) # True. Returns True if the key exists in the dictionary. Otherwise, returns False
print("jpg" in fileDesc) # False. Returns True if the key exists in the dictionary. Otherwise, returns False

# TODO: Check if the value exists
print("Text File Format" in fileDesc.values()) # True. Returns True if the value exists in the dictionary. Otherwise, returns False

# TODO: Remove a single item from the dictionary
fileDesc.pop("txt") # Remove the key:value pair from the dictionary
print(fileDesc) # {'pdf': 'Portable Document Format', 'docx': 'Microsoft Word Document'}

# TODO: Clear the dictionary
fileDesc.clear() # Empty the dictionary
print(fileDesc) # {}