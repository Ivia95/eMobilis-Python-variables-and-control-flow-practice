# Ask the user for a number
number = int(input("Enter a number (1-7): "))

# Determine the corresponding day of the week
if number == 1:
    day = "Monday"
elif number == 2:
    day = "Tuesday"
elif number == 3:
    day = "Wednesday"
elif number == 4:
    day = "Thursday"
elif number == 5:
    day = "Friday"
elif number == 6:
    day = "Saturday"
elif number == 7:
    day = "Sunday"
else:
    day = "Invalid input."

# Print the result
print(f"The corresponding day is: {day}")
