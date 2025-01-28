#import the array and block printer function from ascii_library file
import json
import ascii_printer as ap

try:
    with open('ascii_library.json', 'r') as file:
        ascii_library = json.load(file)
except FileNotFoundError:
    print("Error: ASCII library file not found")
    exit(1)
except json.JSONDecodeError:
    print("Error: Invalid JSON format in ASCII library file")
    exit(1)

word = input("Enter a word: ").upper()
ascii_fied = ascii_printer(word)
print(ascii_fied)


"""
Question the requirements: Breakdown

pseudocode
ask ai, stack_overflow, docs what builtin methods will find the values you're looking for
write tests, write code
"""

alphabet = []
ascii_art = []

for index, value in enumerate(ascii_art_letters):
    print(index, value)

    

print(alphabet)
print(ascii_art)

# letter_A = ascii_art_letters.get('Z')
# for line in letter_A:
#     print(line)

#cd quizzes/python_quizzes/code_academy_python/ascii


# Example usage to print 'HELLO'
if __name__ == "__main__":
    main()