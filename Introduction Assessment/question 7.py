# Ask the user for the lengths of the three sides
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Determine the type of triangle
if side1 == side2 == side3:
    triangle_type = "Equilateral"
elif side1 == side2 or side2 == side3 or side1 == side3:
    triangle_type = "Isosceles"
else:
    triangle_type = "Scalene"

# Print the result
print(f"The triangle is {triangle_type}.")
