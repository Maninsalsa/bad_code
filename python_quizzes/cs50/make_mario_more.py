# use the python language to simulate the make_mario_more exercise that was written in C

# def capture_number(prompt="Enter a whole, positive number: ") -> int:
#     while True:
#         try:
#             number = int(input(prompt).strip())
#             if number <= 0:
#                 print("Please try again...")
#                 continue
#             print(f"You entered: {number}!")
#             return number
#         except ValueError:
#             print("Please try again...")

# value = capture_number()

# def pyramid_printer(integer):
#     spaces = 0
#     bricks = 0

def print_row(user_input: int, row: int) -> None:
    # Print leading spaces
    print(" " * (user_input - row - 1), end="")
    
    # Print left hashes
    print("#" * row, end="")
    
    # Print gap between pyramids
    print("  ", end="")
    
    # Print right hashes
    print("#" * row, end="")
    
    # Print trailing spaces (optional in Python since we're using newline)
    print(" " * (user_input - row - 1))

def main() -> None:
    # Get valid height from user
    while True:
        try:
            n = int(input("height?: "))
            if n >= 1:
                break
            print("Please enter a positive number")
        except ValueError:
            print("Please enter a valid number")
    
    # Print each row of the pyramid
    for i in range(n):
        print_row(n, i)

if __name__ == "__main__":
    main()
    