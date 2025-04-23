# """
# SLICING QUIZ

# The purpose of this quiz is to test your knowledge of slice operation syntax. some of
# the questions require modifying the given iterable, but the brute force solutions, must
# only be derived from utilizing slicing operations. disregard big O performance.

# BONUS complete the objectives pythonically
# """


# # """
# # QUESTION 1
# # Given the string: "Hello World!"
# # What slice operation would return just "Hello"?
# # """
# given_string = "Hello World!"
# print(f"Answer 1: {given_string[:5]}\n")

# # """
# # QUESTION 2
# # Given the string: "Python Programming"
# # Write a slice operation that returns every second character starting from index 1
# # Expected output: "yhnPormig" """

# # # length = 18
# given_string = "Python Programming" 
# # Your solution here
# answer_2 = given_string[1::2]
# print(f"Answer 2: {answer_2}\n")

# # """
# # QUESTION 3
# # Given the string: "Programming101"
# # Write a slice operation that returns the string in reverse order
# # Expected output: "101gnimmargorP"
# # """

# given_string = "Programming101"

# # for i, v in enumerate(given_string):
# #     print(i, v)
# # Your solution here
# answer_3 = given_string[-1::-1]
# print(f"Answer 3: {answer_3}\n")

# def convert_case(number, given_string:str) -> str:
#     converted_string = ""
#     if number == 0:
#         case = [i.upper() for i in given_string]

#     if number == 1:
#         case = [i.lower() for i in given_string]
    
#     return case
        

# # """
# # QUESTION 4
# # Given the string: "Python Is Awesome"
# # Write a slice operation that returns only the vowels (a,e,i,o,u)
# # Hint: First convert to lowercase, then use string methods and slicing
# # Expected output: "oiaeoae
# # """
# # 
# given_string = "Python Is Awesome"

# # Your solution here
# lower_cased_space = convert_case(1, given_string)
# lower_cased = list(filter(lambda x: x != ' ', lower_cased_space))
# string_4 = lower_cased[4:7:2] + lower_cased[8:12:2] + lower_cased[-3:-2:] + lower_cased[8:12:2]
# answer_4 = "".join(string_4)
# print(f"Answer 4: {answer_4}\n")

# # """
# # QUESTION 5
# # Given the list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # Write a slice operation that returns every third number
# # Expected output: [0, 3, 6, 9]
# # """
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # Your solution here
# answer_5 = numbers[::3]
# print(f"Answer 5: {answer_5}\n")

# # """
# # QUESTION 6
# # Given the string: "Hello Python"
# # Write a slice operation that returns the first 5 characters in reverse order
# # Expected output: "olleH" 
# # """

# given_string = "Hello Python"
# # Your solution here
# answer_6 = given_string[4::-1]
# print(f"Answer 6: {answer_6}\n")

# # """
# # QUESTION 7
# # Given the string: "PyThOnPrOgRaMmInG"
# # Write a slice operation that returns every uppercase letter
# # Hint: First create a new string with just uppercase letters, then slice
# # Expected output: "TORGRMG" 
# # """

# given_string = "PyThOnPrOgRaMmInG"
# # Your solution here
# upper_case = convert_case(0, given_string)
# upper_cased = upper_case[2:5:2] + upper_case[7:10:2] + upper_case[10::3]
# answer_7 = "".join(upper_cased)
# print(f"Answer 7: {answer_7}\n")

# """
# QUESTION 8
# Given two strings: "Python" and "Programming"
# Write slice operations to create the word "Pong" using only characters from these strings
# Hint: You'll need to use slicing on both strings
# Expected output: "Pong" 
# """

# string1 = "Python"
# string2 = "Programming"
# # Your solution here
# answer_8 = string1[::4] + string2[-2::]
# print(f"Answer 8: {answer_8}\n")

# """
# QUESTION 9
# Given the string: "0123456789"
# Write a slice operation that returns all numbers except the first and last two
# Expected output: "234567" 
# """

# given_string = "0123456789"
# # Your solution here
# answer_9 = given_string[2:8:]
# print(f"Answer 9: {answer_9}\n")

# """
# QUESTION 10
# Given the string: "Python Programming"
# Write slice operations to swap the words
# Expected output: "Programming Python" 
# """

# given_string = "Python Programming"
# # Your solution here
# answer_10 = given_string[7::] + given_string[6:7:1] + given_string[:6:]
# print(f"Answer 10: {answer_10}\n")

# """
# SLICING BEST PRACTICES 

# This section of the quiz pertains to big O performance. you will have to deduce whether
# or not the situation in the prompt calls for slicing. 
# """

# """
# QUESTION 11
# You need to reverse a string with 1 million characters. Which approach would be more efficient?

# a) string[::-1]
# b) ''.join(reversed(string))
# c) ''.join([string[i] for i in range(len(string)-1, -1, -1)])
# """
# # Your answer here (a, b, or c)
# """
# b. since all methods still create a new iterable, I'm assuming reversed(string) would be
# correct since most built-in functions use C under the hood
# """

# """
# QUESTION 12
# You need to extract the last 5 elements from a list of 10,000 items. 
# Which method would be more efficient?

# a) my_list[-5:]
# b) my_list[len(my_list)-5:]
# c) collections.deque(my_list, maxlen=5)

# Consider both time complexity and memory usage.
# """
# # Your answer here (a, b, or c)
# """
# c. since the list is contains a large number of iterables, collections.deque(). reason is
# .deque() is implemented in C, thread-safe, memory efficient with maxlen. 

# """

# """
# QUESTION 13
# Given a large list, you need to remove the first element repeatedly.
# Which approach should you use?

# a) my_list = my_list[1:]
# b) my_list.pop(0)
# c) from collections import deque; d = deque(my_list); d.popleft()
# """
# # Your answer here (a, b, or c)
# """c, .deque() is best when changes are repeatedly being made to either end of an iterable"""

# """
# QUESTION 14
# You need to check if a sequence ends with a specific pattern.
# Which method is more efficient?

# a) sequence[-len(pattern):] == pattern
# b) sequence.endswith(pattern)  # for strings
# c) all(sequence[i] == pattern[i] for i in range(-len(pattern), 0))
# """
# # Your answer here (a, b, or c)
# answer_14 = None

# """
# QUESTION 15
# You have a string with 100,000 characters and need every 100th character.
# Which approach is more memory efficient?

# a) string[::100]
# b) ''.join(string[i] for i in range(0, len(string), 100))
# c) [string[i] for i in range(0, len(string), 100)]
# """
# # Your answer here (a, b, or c)
# answer_15 = None


"""
SLICING QUIZ EXTENSION 04 - 19 -25

"""
# QUESTION 16
# Given the nested list: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Write a slice operation that returns only the middle elements [2, 5, 8]
# Hint: You'll need to combine multiple slice operations
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Your solution here
middle_elements = [sublist[1] for sublist in nested_list]
# Alternative solution:
# middle_elements = [nested_list[i][1] for i in range(len(nested_list))]

# Using slicing:
middle_elements_slice = [nested_list[i][1:2][0] for i in range(len(nested_list))]
# Or more purely with slicing:
middle_elements_pure_slice = [row[1:2][0] for row in nested_list[0:3]]
# End of Selection





# # QUESTION 17
# # Given the string: "A,B,C;D,E,F;G,H,I"
# # Use slicing to get every third character that follows a comma
# # Expected output: "CEI"
# complex_string = "A,B,C;D,E,F;G,H,I"
# # Your solution here

# # QUESTION 18
# # Given two strings: "12345" and "ABCDE"
# # Write slice operations to create an interleaved string where every other character alternates
# # Expected output: "1A2B3C4D5E"
# num_string = "12345"
# alpha_string = "ABCDE"
# # Your solution here

# # QUESTION 19
# # Given the string: "PyThOn@#$PrOgRaMmInG123"
# # Write slice operations to extract only the letters, maintaining their original case
# # Expected output: "PyThOnPrOgRaMmInG"
# mixed_string = "PyThOn@#$PrOgRaMmInG123"
# # Your solution here

# # QUESTION 20
# # Given the palindrome string: "Step on no pets"
# # Write a slice operation that checks if it's a palindrome (ignoring spaces and case)
# # Hint: Use string methods first, then slicing
# palindrome = "Step on no pets"
# # Your solution here

# """
# ADVANCED SLICING CONCEPTS
# These questions focus on more complex slicing scenarios and performance considerations
# """

# # QUESTION 21
# # Given a matrix represented as nested lists:
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# # Write slice operations to get the diagonal elements [1, 6, 11]
# # Your solution here

# # QUESTION 22
# # You have a large string containing DNA sequences: "ATCGATCGATCG"
# # Write a slice operation to get overlapping sequences of length 3
# # Expected output: ["ATC", "TCG", "CGA", "GAT", "ATC", "TCG", "CGA", "GAT", "ATC", "TCG"]
# dna_sequence = "ATCGATCGATCG"
# # Your solution here

# """
# PERFORMANCE CONSIDERATIONS
# Answer these questions about slicing performance and best practices
# """

# # QUESTION 23
# # When working with a very large sequence (millions of elements), which slicing operation
# # would be more memory efficient for getting alternate elements?
# #
# # a) sequence[::2]
# # b) list(itertools.islice(sequence, 0, None, 2))
# # c) [sequence[i] for i in range(0, len(sequence), 2)]
# # 
# # Explain your reasoning

# # QUESTION 24
# # In a scenario where you need to process a large file line by line in reverse order,
# # which approach would be more efficient?
# #
# # a) lines = file.readlines()[::-1]
# # b) lines = reversed(file.readlines())
# # c) from collections import deque; lines = deque(file, maxlen=1000)
# #
# # Consider both memory usage and processing speed

# # QUESTION 25
# # Given a string with a million characters, you need to extract specific ranges repeatedly.
# # Which data structure would be most efficient?
# #
# # a) Keep as string and use string slicing
# # b) Convert to list and use list slicing
# # c) Use memoryview on bytes object
# # d) Use array.array
# #
# # Consider both access speed and memory usage

# """
# ANSWERS:

# [Hidden for now - would you like to attempt the questions first?]
# """


# # The extension maintains the original quiz's progression from basic to advanced concepts while adding:

# # 1. More complex slicing scenarios (nested lists, pattern matching)
# # 2. Real-world applications (DNA sequence processing)
# # 3. Performance-focused questions
# # 4. Matrix operations using slicing
# # 5. Memory efficiency considerations

# # Would you like to try solving these questions first, or would you like to see the answers and explanations?

# # Each question builds on the concepts from the original quiz while introducing new challenges:
# # - Questions 16-20 focus on practical applications
# # - Questions 21-22 deal with more complex data structures
# # - Questions 23-25 address performance considerations

# # The questions are designed to be engaging while testing deeper understanding of Python slicing operations and their practical applications. They maintain the same difficulty progression as the original quiz while introducing new concepts and scenarios.
