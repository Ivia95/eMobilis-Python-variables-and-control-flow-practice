# Ask the user for a score
score = int(input("Enter a score (0-100): "))

# Determine the grade
if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
else:
    grade = 'F'

# Print the grade
print("The grade is:", grade)
