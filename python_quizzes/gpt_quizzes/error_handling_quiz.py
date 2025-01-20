# brute force error handling

# while True:
#     input_number = input("Please enter a number...")
#     if input_number.isnumeric():
#         number = input_number
#         print(f"You enetered: {number}!")
#         break # break makes using an else statement unecessary. 
#     else: # However, the inclusion can improve readability
#         print('Please try again')

# put it in a function

def get_number() -> int:
    while True:
        ask_for_number = input("Enter a number...")
        if ask_for_number.isnumeric():
            number = int(ask_for_number)
            print(f"You entered: {number}!")
            return number
        print('please try again...')

# pythonic error handling
def pythonic_number() -> int:
    while True:
        try:
            number = int(input("Enter a number: "))
            print(f"You entered: {number}!")
            break
        except ValueError:
            print('Please try again...')


# even more pythonic and takes into account edge cases. 
def get_valid_number(prompt="Enter a positive number: ", allow_floats=False) -> float:
    """
    Prompt the user for a positive number and validate the input.

    Args:
        prompt (str): The message to display when asking for input.
        allow_floats (bool): Whether to allow floating-point numbers.

    Returns:
        int or float: A valid positive number entered by the user.
    """
    while True:
        try:
            # use of .strip ensures if the input has a number, but has white space, the space is ignored
            user_input = input(prompt).strip() 
            # Allow float or int based on `allow_floats`
            number = float(user_input) if allow_floats else int(user_input)
            if number <= 0:
                print("Please enter a positive number.")
                continue
            print(f"You entered: {number}!")
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Examples:
num = get_valid_number()
float_num = get_valid_number("Enter a float number: ", allow_floats=True)