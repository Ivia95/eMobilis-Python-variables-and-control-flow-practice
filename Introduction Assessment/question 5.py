# Ask the user for their age
age = int(input("Enter your age: "))

# Determine the age category
if age < 18:
    category = "a minor"
elif 18 <= age <= 65:
    category = "an adult"
else:
    category = "a senior"

# Print the result
print(f"You are {category}.")
