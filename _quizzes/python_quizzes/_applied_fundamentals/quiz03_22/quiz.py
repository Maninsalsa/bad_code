# Question 1: List Comprehensions
# What will the following list comprehension output?

# answer = "1. Outputs the exponents of the first 5 indexes"
# result = [x**2 for x in range(5)]
# print(f"{answer}\n{result}")

# # Question 2: Functions
# # What's wrong with this function definition?

# answer = """
# 2. the print(calculation complete) line should be before the return value. 
# since it's after, it doesn't execute. Also the function should be able to take more 
# than one number to calc average"""

# # def calculate_average(numbers):
# #     total=sum(numbers)
# #     return total/ len(numbers)
# #     print("Calculation complete")

# def calculate_average(*numbers) -> float:
#     total=sum(numbers)
#     print("Calculation complete")
#     return total/len(numbers)

# answer = calculate_average(10, 3, 4, 6, 68)
# print(answer)

# # Question 3: Conditional Statements
# # What will the following code output?

# answer = """the answer is A. Even though x satisfies the elif and else statements, the program is satisifed with the first conditional statement
# In order to have it print all, continue would have to be in the conditional statement execution"""
# x = 10
# if x > 5:
#     print("A")
# elif x > 8:
#     print("B")
# else:
#     print("C")

# # Question 4: List Comprehensions with Nested Conditions
# # What will this list comprehension produce?

# answer = """if x is even, append it to the new list, if it isn't multiply it by 2, starting at 1, up to 5"""

# result = [x if x % 2 == 0 else x*2 for x in range(1, 6)]
# print(result)

# # Question 5: Functions with default Parameters
# # What does this funcitno return when called as greet("Alice")?

# answer = """Hello, Alice"""

# def greet(name, greeting="Hello"):
#     return f"{greeting}, {name}"

# # Question 6: Nested Conditional Statements
# # What will this code output

# answer = "B"

# score = 85
# if score >= "90":
#     result= "A"
# else:
#     if score >= 80:
#         result = "B"
#     else:
#         if score >= 70:
#             result = "C"
#         else:
#             result = "F"

# print(result)

# Question 7: Advanced List Comprehension
# What does this nested list comprehension create?

answer = """creates a new matrix with 3 rows, where each row contains the 1st, 2nd, then\
            3rd elements of the og rows. This effectively transposes rows into columns and columns into rows"""


def print_matrix(matrix) -> list:
    # Find the maximum width needed
    width = max(len(str(elem)) for row in matrix for elem in row)
    
    for row in matrix:
        # Format each element to have consistent width
        print(' '.join(f"{elem:{width}}" for elem in row))

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
printed_matrix = print_matrix(matrix)
print("\n")


transposed = [[row[i] for row in matrix] for i in range(3)]
printed_transposed = print_matrix(transposed) 