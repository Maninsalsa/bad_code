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

Allows the user to convert letters and/or words in plain text into ASCII artform letters.
Each capital letter is assigned an ASCII art representation in key:value pair format.
The letters are written on a file

## Technical Design
The project consists of:
- ASCII library JSON file containing the art mappings
- Module with core functionality 
- Main script to coordinate the program flow

### Program Flow
1. Import required modules and ASCII library
2. Get user input string
3. Convert input to uppercase
4. Map each character to its ASCII art representation
5. Combine the ASCII art characters
6. Write the result onto a file in .txt format. 

### Components

**Main Script (main.py)**
- Imports required modules
- Gets user input
- Coordinates conversion process
- Displays output

**ASCII Library (ascii_library.json)**
- Stores ASCII art mappings
- Keys are capital letters
- Values are lists of strings forming characters

**ASCII Converter Module**
- Contains core conversion logic
- Handles character mapping
- Combines ASCII characters

### Requirements
- Dictionary mapping letters to ASCII art
- Support for capital letters A-Z
- Each ASCII character composed of 7 strings
- Input validation and error handling
- Output to console or text file

### Implementation Details

#### Core Classes
- `AsciiLetter`: Represents single ASCII character
- `AsciiWord`: Combines multiple ASCII letters

#### Key Functions  
- `convert_to_ascii(text)`: Main conversion function
- `validate_input(text)`: Input validation
- `combine_letters(letters)`: Combines ASCII characters

#### Error Handling
- Input validation
- Invalid character handling
- Custom exceptions for ASCII conversion errors

### Testing
- Unit tests for core functionality
- Input validation tests
- Edge case handling
- Integration tests
