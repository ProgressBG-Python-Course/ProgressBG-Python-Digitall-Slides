# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:

Define a function named `get_numeric_input()` that:

1. Prompts the user to enter a valid number.
2. Continuously prompts until a valid number (integer or floating-point) is entered.
3. Returns the valid number as a `float`.

The function must handle potential errors, such as:

- KeyboardInterrupt - gracefully exit, if user press 'Ctrl+C'
- Empty input - pressing Enter without typing anything.
- Invalid input - non-numeric characters.
- Any other unexpected errors that might occur during input.

"""

### Your code here


# Example usage:
# try:
#     valid_number = get_numeric_input()
#     print("You entered:", valid_number)
# except KeyboardInterrupt:
#     print("\nProgram exited by user.")


### EXPECTED OUTPUT:

# Please enter a number: 23
# You entered: 23.0

# Please enter a number:
# Invalid input: Input cannot be empty.

# Please enter a number: o
# Invalid input: could not convert string to float: 'o'

# Please enter a number: ^C
# Program exited by user.


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:

Write a program that prompts the user to enter their name. Ensure the entered name:

1. Contains only letters.
    - tip: you can use the string.isalpha() method
2. Starts with an uppercase letter.
    - tip: you can use the string.isupper() method
3. Is at least 2 characters long.

The function must raise InvalidUserName exception if user name is not valid.

"""

### Your code here

# Example usage:
# try:
#     username = get_valid_username()
#     print(f"Hello, {username}!")
# except KeyboardInterrupt:
#     print("\nProgram exited by user.")

# EXPECTED OUTPUT:
# Please enter your name: ada123
# Error: Name must contain only letters.
# Please enter your name: ada
# Error: Name must start with an uppercase letter.
# Please enter your name: A
# Error: Name must be at least 2 characters long.
# Please enter your name: Ada
# Hello, Ada!
