# ASCII Art Generator

## Project Overview
This project helps practice several key Python concepts:

- Dictionary key/value access
- Use of classes
- Module imports and file handling 
- Separation of concerns
- Iterator usage with built-in methods
- Common string methods (.get(), .upper(), .join())
- List comprehensions
- Unit testing
- Documentation

Allows the user to convert their plain text of individual letters and/or words into their ASCII artform versions. 
Each capital letter is assigned an ascii art in key:value pair format.

## Technical Design
directory includes:
- one json file for the ascii library
- one module to store functions
- one main script to organize it all together

**Main**
    the library and module are imported

    main asks the user for a string, which is stored in a variable 'string_captured'
    'string_captured' takes the input string from the user and converts it to uppercase
    
    'ascii_printer' passes 'string_captured' and converts the values 
    The variable "ascii_art" initiates a variable to capture the ascii art associated with the matching key
    the chars in the string passed is iterated over and adds the ascii art values for all matching key and char pairs. 

### Requirements
- Dictionary containing ASCII art letters
- Capital letters as keys
- Values are lists of 7 strings forming ASCII art characters
- the user inputs any string, whether it's a single letter or a word, and the program will print what they write on a .txt document

### Key Questions
1. Python Fundamentals Quiz (Easy):
   - What string method would you use to convert "hello" to "HELLO"?
   - How do you access a value from a dictionary given its key?
   - What is the purpose of .get() vs direct key access?

2. ASCII Art Functions (Medium): 
   - Write a function that takes a single letter and returns its ASCII art representation
   - How would you validate that input is a valid letter?
   - What data structure would you use to store multi-line ASCII characters?

3. String Processing (Medium):
   - Design a function that combines multiple ASCII letters into a word
   - How would you handle invalid characters in the input?
   - What's the most efficient way to join multiple strings vertically?

4. Error Handling (Hard):
   - Implement comprehensive input validation with appropriate error messages
   - Add unit tests to verify letter case handling
   - Create a custom exception class for ASCII art errors

### Implementation Approach

main.py accesses the json file ascii_library.json. 
it encorporates classes from the asci_art_letter.py to create word and letter instances. 

#### Core classes and Functions

def_ascii_word()
def_ascii_letter()

