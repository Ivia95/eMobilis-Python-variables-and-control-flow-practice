def has_pair_with_sum(numbers, target_sum):
    seen = set()  # Initialize an empty set to store numbers we've seen
    for number in numbers:
        complement = target_sum - number
        if complement in seen:  # Check if the complement of the current number is in the seen set
            return True  # Return True if the pair is found
        seen.add(number)  # Add the current number to the set
    return False  # Return False if no such pair is found

# Example input
numbers = [10, 15, 3, 7]
target_sum = 17

# Call the function and print the result
print(has_pair_with_sum(numbers, target_sum))
