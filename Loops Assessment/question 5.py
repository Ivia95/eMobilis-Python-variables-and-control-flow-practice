def print_even_keys(input_dict):
    for key, value in input_dict.items():
        if value % 2 == 0:  # Check if the value is even
            print(key)  # Print the key if the value is even

# Example dictionary
input_dict = {'a': 2, 'b': 3, 'c': 4}

# Call the function with the example dictionary
print_even_keys(input_dict)

