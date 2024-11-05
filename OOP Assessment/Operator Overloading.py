class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Create two Vector objects
vector1 = Vector(2, 3)
vector2 = Vector(5, 7)

# Add the two vectors
result = vector1 + vector2

# Print the result
print(result)  # Output: Vector(7, 10)
