# **Python Decorator Functions Quiz - Beginner Level**

# What is the primary purpose of a decorator function in Python?

# Choose the most accurate answer:
# a) To add visual elements to the code
# b) To modify or enhance the behavior of another function without directly changing its source code
# c) To create new variables within a function
# d) To import external libraries
# Answer: b ✅


# Which of the following is the correct syntax for applying a decorator to a function?

# A)
# @decorator
# def my_function():
#     pass

# B)
# @decorator()
# def my_function():
#     pass

# C)
# decorator@
# def my_function():
#     pass

# D)
# def my_function():
#     @decorator
#     pass

# Answer: A ✅

# What will be the output of this code?

def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def greet():
    return "hello world"

print(greet())
# Answer: The wrapper takes the function and assigns the function call to a variable and applies the .upper() method to it and returns the result


# Write a decorator function called `timer` that will measure and print the execution time of any function it decorates. Use the following template:

import time

def timer(func):
    # Your code here
    start_time = time.time()
    func
    end_time = time.time()

# Example usage:
@timer
def slow_function():
    time.sleep(1)
    return "Done!"
# Answer: 

# def timer(func):
#     # Your code here
#     start_time = time.time()
#     func
#     end_time = time.time()

# Create a decorator called `retry` that will retry a function up to 3 times if it raises an exception. Here's the template:

def retry(func):
    # Your code here 
    # tries = 0
    # if func == ValueError and tries < 3:
    #     func
    #     tries +1
    def wrapper(*args, **kwargs): # ✅
        for attempt in range(3):
            try:
                return func(*args, **kwargs)
            except ValueError as e:
                if attempt == 2:  # Last attempt
                    raise e
                print(f"Attempt {attempt + 1} failed, retrying...")
        return None
    return wrapper 
    
# Example usage:
@retry
def might_fail():
    import random
    if random.random() < 0.7:  # 70% chance to fail
        raise ValueError("Random failure!")
    return "Success!"
# Answer: 

# def retry(func):
#     # Your code here
#     tries = 0
#     if func == ValueError and tries < 3:
#         func
#         tries +1

# **Answer Format:**
# Please provide:
# 1. Your chosen answer for questions 1-2
# 2. The expected output for question 3
# 3. Your implementation for questions 4-5

# Remember to explain your reasoning for each answer. Good luck! 🍀

# Would you like to start with any particular question, or shall we go through them in order?
