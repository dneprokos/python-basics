# Example of abstract classes in Python

# Abstract classes are classes that contain one or more abstract methods. An abstract method is a method that is declared, but contains no implementation. Abstract classes cannot be instantiated, and require subclasses to provide implementations for the abstract methods.
from abc import ABC, abstractmethod # ABC = Abstract Base Class (ABC) module from Python's standard library


class GraphicShape(ABC): # ABC = Abstract Base Class (ABC) module from Python's standard library
    def __init__(self):
        super().__init__()
    
    @abstractmethod # This decorator indicates that this method is abstract
    def calcArea(self):
        # This is an abstract method
        pass

class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius
    
    def calcArea(self):
        return 3.14 * (self.radius ** 2)
    
class Square(GraphicShape):
    def __init__(self, side):
        self.side = side
    
    def calcArea(self):
        return self.side * self.side

# g = GraphicShape() # This will throw an error because you cannot instantiate an abstract class
c = Circle(10)
print(c.calcArea())

s = Square(12)
print(s.calcArea())