def ascii_printer(word: str) -> str:
    ascii_art = []
    
    # iterate through string argument
    for char in word:
        if char == ascii_art_letters[char]:
            ascii_art.append(ascii_art_letters[char])
    return ascii_art

# give me the syntax and built0in functions of generic versions of iterating through values of a dictionary:

# access key 
for key in my_dict:
    print(key)
# or
for key in my_dict.keys():
    print(key)

# access value
for value in my_dict.values():
    print(value)

# access key : value
for key, value in my_dict.items():
    print(f"{key}: {value}")

# access a an index within a value in a dictionary
value = my_dict["key"][index]  # If value is a sequence
# or
value = my_dict.get("key")[index]  # Safer way with .get()

# access individual characters in a string
my_string = "Hello"
for char in my_string:
    print(char)

# access characters with index
for i in range(len(my_string)):
    print(my_string[i])

# access with enumerate for both index and character
for i, char in enumerate(my_string):
    print(f"Index {i}: {char}")

# string slicing
substring = my_string[start:end:step]  # e.g. my_string[0:3] gets first 3 chars
# or
first_char = my_string[0]      # get first character
last_char = my_string[-1]      # get last character
every_other = my_string[::2]   # get every other character
