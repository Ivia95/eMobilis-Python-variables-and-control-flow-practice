def reverse_strings(strings):
    reversed_list = []  # Initialize an empty list to store reversed strings
    for s in strings:
        reversed_list.append(s[::-1])  # Reverse each string and add to the list
    return reversed_list  # Return the list of reversed strings

# Example input
strings = ["apple", "banana", "cherry"]

# Call the function and print the result
print(reverse_strings(strings))
