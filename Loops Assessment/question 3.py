def sum_of_list(nums):
    total = 0  # Initialize total to 0
    for num in nums:
        total += num  # Add each number in the list to the total
    return total  # Return the total sum

# Given list
nums = [1, 2, 3, 4, 5]

# Call the function and print the result
print(sum_of_list(nums))
