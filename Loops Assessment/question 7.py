def remove_duplicates(input_list):
    unique_list = []  # Initialize an empty list to store unique elements
    for item in input_list:
        if item not in unique_list:  # Check if the item is already in the unique list
            unique_list.append(item)  # Add the item to the unique list if it's not already there
    return unique_list  # Return the list with duplicates removed

# Example input list
input_list = [1, 2, 2, 3, 4, 4, 5]

# Call the function and print the result
print(remove_duplicates(input_list))
