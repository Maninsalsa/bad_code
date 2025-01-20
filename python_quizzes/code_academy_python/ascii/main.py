#import the array and block printer function from ascii_library file
from ascii_library import ascii_art_letters, block_printer

# Example usage to print 'HELLO'
if __name__ == "__main__":
    word = input("Enter a word: ").upper()
    block_printer(word)
    # this was the error
    # block_printer = list(word)
    # I was reassigning block_printer into a list insteawd of calling it with the word I want to print.


