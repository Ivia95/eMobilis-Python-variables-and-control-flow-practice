def ask_until_exit():
    while True:
        user_input = input("Enter a word (type 'exit' to quit): ")
        if user_input.lower() == 'exit':  # Check if the input is 'exit'
            break  # Exit the loop
        print(user_input)  # Print the entered word

# Call the function to start the process
ask_until_exit()
