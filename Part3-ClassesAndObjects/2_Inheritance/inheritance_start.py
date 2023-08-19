# Example of inheritance

# Publication is the base class
class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price

# Magazine inherits from Publication
# Book inherits from Publication
class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price) # Call the base class constructor
        self._author = author
        self._pages = pages
    
    # Properties are getters and setters
    @property
    def title(self):
        return self._title
    
    # Setter
    @title.setter
    def title(self, value):
        self._title = value

    @property
    def author(self):
        return self._author
    
    # Setter
    @author.setter
    def author(self, value):
        self._author = value

    @property
    def pages(self):
        return self._pages
    
    # Setter
    @pages.setter
    def pages(self, value):
        self._pages = value

    @property
    def price(self):
        return self._price
    
    # Setter
    @price.setter
    def price(self, value):
        self._price = value

# Create an object
b1 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# Get the title
print(b1.title)

# Set the title
b1.title = "The Catcher in the Rye 2"
print(b1.title)
print(b1.author)
print(b1.pages)
print(b1.price)