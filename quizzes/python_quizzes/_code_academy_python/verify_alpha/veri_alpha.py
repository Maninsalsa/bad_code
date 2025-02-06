alpha_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:

# Using the list approach would be an exception if the order of information is important. 
# unique_letters list approach
# def unique_english_letters(string):
#     unique_letters = []
#     for letter in string:
#         if letter in alpha_list and letter not in unique_letters:
#             unique_letters.append(letter)
#     return len(unique_letters)

# # alpha_list iteration approach (least efficient)
# def unique_english_letters(string):
#     uniques = 0
#     for letter in alpha_list:
#         if letter in string:
#             uniques += 1
#     return uniques

# using a set to ensure uniqueness *most efficient
def unique_english_letters(string):
    # Use a set to store only unique letters
    return len({letter for letter in string if letter in alpha_list})

print(unique_english_letters("mississippi"))
print(unique_english_letters("Apple"))

# takes input word and counts the amount of times x appears in the word.
# def count_char_x(word, x):
#     count = 0
#     for letter in word:
#         if letter == x:
#             count += 1
#     return count

# the most efficient approach:

def count_char_x(word, x):
    return word.count(x)

print(count_char_x("mississippi", "s"))
print(count_char_x("mississippi", "m"))

# using count can also count substrings from the reference string
def count_multi_char_x(word, x):
    return word.count(x)

