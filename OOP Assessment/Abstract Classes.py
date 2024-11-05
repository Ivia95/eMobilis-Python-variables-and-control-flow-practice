from abc import ABC, abstractmethod
import math

# Define the abstract base class Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Define the Circle subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Define the Square subclass
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

# Create instances of Circle and Square
my_circle = Circle(5)
my_square = Square(4)

# Call the area() method on each instance
print(f"Area of the circle: {my_circle.area()}")  # Output: Area of the circle: 78.53981633974483
print(f"Area of the square: {my_square.area()}")  # Output: Area of the square: 16
