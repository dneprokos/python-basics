# Examples of using classes and methods

# The class is a blueprint for creating objects
class Book:
    # Init is not a constructor, it is a method that is called when an object is created
    def __init__(self, title, author, pages, price):
        # Underscore is a convention for private variables. It is a convention, not a rule
        self._title = title
        self._author = author
        self._pages = pages
        self._price = price
    
    # Properties are getters and setters
    @property
    def title(self):
        return self._title
    
    # Setter
    @title.setter
    def title(self, value):
        self._title = value



# Create an object
b1 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# Get the title
print(b1.title)

# Set the title
b1.title = "The Catcher in the Rye 2"
print(b1.title)

