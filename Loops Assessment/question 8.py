def keys_greater_than_n(input_dict, n):
    result = []  # Initialize an empty list to store keys
    for key, value in input_dict.items():
        if value > n:  # Check if the value is greater than n
            result.append(key)  # Add the key to the result list if condition is met
    return result  # Return the list of keys

# Example dictionary and integer
input_dict = {'a': 5, 'b': 12, 'c': 3}
n = 4

# Call the function and print the result
print(keys_greater_than_n(input_dict, n))
