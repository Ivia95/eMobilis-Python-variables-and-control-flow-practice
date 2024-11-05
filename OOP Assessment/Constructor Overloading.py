class Rectangle:
    def __init__(self, length, width=None):
        if width is None:
            self.width = length
        else:
            self.width = width
        self.length = length

    def calculate_area(self):
        return self.length * self.width

# Creating a square
square = Rectangle(5)
print(f"Square area: {square.calculate_area()}")

# Creating a rectangle
rectangle = Rectangle(4, 6)
print(f"Rectangle area: {rectangle.calculate_area()}")
