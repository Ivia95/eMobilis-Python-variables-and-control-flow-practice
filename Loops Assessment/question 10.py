def tuples_to_dict(tuple_list):
    result_dict = {}  # Initialize an empty dictionary
    for key, value in tuple_list:
        result_dict[key] = value  # Add the key-value pair to the dictionary
    return result_dict  # Return the resulting dictionary

# Example list of tuples
tuple_list = [("apple", 5), ("banana", 3), ("cherry", 7)]

# Call the function and print the result
print(tuples_to_dict(tuple_list))
