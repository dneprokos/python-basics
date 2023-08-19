# Example of interfaces in Python

from abc import ABC, abstractmethod # ABC = Abstract Base Class (ABC) module from Python's standard library

# An interface is a class that contains only abstract methods. The methods are defined without any implementation. Interfaces form a contract between the class and the outside world, and this contract is enforced at build time by the compiler. If your class claims to implement an interface, all methods defined by that interface must appear in its source code before the class will successfully compile.
class jsonify(ABC): # ABC = Abstract Base Class (ABC) module from Python's standard library
    @abstractmethod # This decorator indicates that this method is abstract
    def toJson(self):
        pass

class GraphicShape(ABC): # ABC = Abstract Base Class (ABC) module from Python's standard library
    def __init__(self):
        super().__init__()
    
    @abstractmethod # This decorator indicates that this method is abstract
    def calcArea(self):
        # This is an abstract method
        pass

# This class implement the jsonify interface
class Circle(GraphicShape, jsonify):
    def __init__(self, radius):
        self.radius = radius
    
    def calcArea(self):
        return 3.14 * (self.radius ** 2)
    
    # This method is required by the jsonify interface
    def toJson(self):
        return f"{{\"circle\" : {str(self.calcArea())}}}"

# This class implement the jsonify interface
class Square(GraphicShape, jsonify):
    def __init__(self, side):
        self.side = side
    
    def calcArea(self):
        return self.side * self.side
    
    # This method is required by the jsonify interface
    def toJson(self):
        return f"{{\"square\" : {str(self.calcArea())}}}"

# g = GraphicShape() # This will throw an error because you cannot instantiate an abstract class
c = Circle(10)
print(c.calcArea())
print(c.toJson())

s = Square(12)
print(s.calcArea())
print(s.toJson())