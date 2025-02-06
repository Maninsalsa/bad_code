"""
SLICING QUIZ

The purpose of this quiz is to test your knowledge of slice operation syntax. some of
the questions require modifying the given iterable, but the brute force solutions, must
only be derived from utilizing slicing operations. disregard big O performance.

BONUS complete the objectives pythonically
"""


# """
# QUESTION 1
# Given the string: "Hello World!"
# What slice operation would return just "Hello"?
# """
given_string = "Hello World!"
print(f"Answer 1: {given_string[:5]}\n")

# """
# QUESTION 2
# Given the string: "Python Programming"
# Write a slice operation that returns every second character starting from index 1
# Expected output: "yhnPormig" """

# # length = 18
given_string = "Python Programming" 
# Your solution here
answer_2 = given_string[1::2]
print(f"Answer 2: {answer_2}\n")

# """
# QUESTION 3
# Given the string: "Programming101"
# Write a slice operation that returns the string in reverse order
# Expected output: "101gnimmargorP"
# """

given_string = "Programming101"

# for i, v in enumerate(given_string):
#     print(i, v)
# Your solution here
answer_3 = given_string[-1::-1]
print(f"Answer 3: {answer_3}\n")

def convert_case(number, given_string:str) -> str:
    converted_string = ""
    if number == 0:
        case = [i.upper() for i in given_string]

    if number == 1:
        case = [i.lower() for i in given_string]
    
    return case
        

# """
# QUESTION 4
# Given the string: "Python Is Awesome"
# Write a slice operation that returns only the vowels (a,e,i,o,u)
# Hint: First convert to lowercase, then use string methods and slicing
# Expected output: "oiaeoae
# """
# 
given_string = "Python Is Awesome"

# Your solution here
lower_cased_space = convert_case(1, given_string)
lower_cased = list(filter(lambda x: x != ' ', lower_cased_space))
string_4 = lower_cased[4:7:2] + lower_cased[8:12:2] + lower_cased[-3:-2:] + lower_cased[8:12:2]
answer_4 = "".join(string_4)
print(f"Answer 4: {answer_4}\n")

# """
# QUESTION 5
# Given the list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Write a slice operation that returns every third number
# Expected output: [0, 3, 6, 9]
# """
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Your solution here
answer_5 = numbers[::3]
print(f"Answer 5: {answer_5}\n")

# """
# QUESTION 6
# Given the string: "Hello Python"
# Write a slice operation that returns the first 5 characters in reverse order
# Expected output: "olleH" 
# """

given_string = "Hello Python"
# Your solution here
answer_6 = given_string[4::-1]
print(f"Answer 6: {answer_6}\n")

# """
# QUESTION 7
# Given the string: "PyThOnPrOgRaMmInG"
# Write a slice operation that returns every uppercase letter
# Hint: First create a new string with just uppercase letters, then slice
# Expected output: "TORGRMG" 
# """

given_string = "PyThOnPrOgRaMmInG"
# Your solution here
upper_case = convert_case(0, given_string)
upper_cased = upper_case[2:5:2] + upper_case[7:10:2] + upper_case[10::3]
answer_7 = "".join(upper_cased)
print(f"Answer 7: {answer_7}\n")

"""
QUESTION 8
Given two strings: "Python" and "Programming"
Write slice operations to create the word "Pong" using only characters from these strings
Hint: You'll need to use slicing on both strings
Expected output: "Pong" 
"""

string1 = "Python"
string2 = "Programming"
# Your solution here
answer_8 = string1[::4] + string2[-2::]
print(f"Answer 8: {answer_8}\n")

"""
QUESTION 9
Given the string: "0123456789"
Write a slice operation that returns all numbers except the first and last two
Expected output: "234567" 
"""

given_string = "0123456789"
# Your solution here
answer_9 = given_string[2:8:]
print(f"Answer 9: {answer_9}\n")

"""
QUESTION 10
Given the string: "Python Programming"
Write slice operations to swap the words
Expected output: "Programming Python" 
"""

given_string = "Python Programming"
# Your solution here
answer_10 = given_string[7::] + given_string[6:7:1] + given_string[:6:]
print(f"Answer 10: {answer_10}\n")

"""
SLICING BEST PRACTICES 

This section of the quiz pertains to big O performance. you will have to deduce whether
or not the situation in the prompt calls for slicing. 
"""

"""
QUESTION 11
You need to reverse a string with 1 million characters. Which approach would be more efficient?

a) string[::-1]
b) ''.join(reversed(string))
c) ''.join([string[i] for i in range(len(string)-1, -1, -1)])
"""
# Your answer here (a, b, or c)
"""
b. since all methods still create a new iterable, I'm assuming reversed(string) would be
correct since most built-in functions use C under the hood
"""

"""
QUESTION 12
You need to extract the last 5 elements from a list of 10,000 items. 
Which method would be more efficient?

a) my_list[-5:]
b) my_list[len(my_list)-5:]
c) collections.deque(my_list, maxlen=5)

Consider both time complexity and memory usage.
"""
# Your answer here (a, b, or c)
"""
c. since the list is contains a large number of iterables, collections.deque(). reason is
.deque() is implemented in C, thread-safe, memory efficient with maxlen. 

"""

"""
QUESTION 13
Given a large list, you need to remove the first element repeatedly.
Which approach should you use?

a) my_list = my_list[1:]
b) my_list.pop(0)
c) from collections import deque; d = deque(my_list); d.popleft()
"""
# Your answer here (a, b, or c)
"""c, .deque() is best when changes are repeatedly being made to either end of an iterable"""

"""
QUESTION 14
You need to check if a sequence ends with a specific pattern.
Which method is more efficient?

a) sequence[-len(pattern):] == pattern
b) sequence.endswith(pattern)  # for strings
c) all(sequence[i] == pattern[i] for i in range(-len(pattern), 0))
"""
# Your answer here (a, b, or c)
answer_14 = None

"""
QUESTION 15
You have a string with 100,000 characters and need every 100th character.
Which approach is more memory efficient?

a) string[::100]
b) ''.join(string[i] for i in range(0, len(string), 100))
c) [string[i] for i in range(0, len(string), 100)]
"""
# Your answer here (a, b, or c)
answer_15 = None