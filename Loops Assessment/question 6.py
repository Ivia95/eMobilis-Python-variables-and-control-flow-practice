def find_largest_number(numbers):
    largest = numbers[0]  # Initialize the largest number with the first element of the tuple
    for number in numbers:
        if number > largest:  # Update the largest number if current number is greater
            largest = number
    return largest  # Return the largest number found

# Example tuple
numbers = (10, 20, 30, 40, 50)

# Call the function and print the result
print(find_largest_number(numbers))
