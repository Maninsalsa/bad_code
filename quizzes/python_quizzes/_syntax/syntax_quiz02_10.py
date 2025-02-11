
# Python Syntax Quiz - Intermediate Level

# 1. **Decorator Syntax**
# What's wrong with this decorator implementation?

# def my_decorator():
#     def wrapper(func):
#         result = func()
#         return result.upper()
#     return wrapper

# @my_decorator
# def greet():
#     return "hello"

# answer_1
def my_decorator(func): # target function is passed through decorator, not wrapper
    def wrapper():
        answer = func() # initialize function
        return answer.upper() # modifies by calling .upper, but does not change the o.g. function
    return wrapper

@my_decorator # decorator syntax
def greet():
    return "hello"

print(greet())

# 2. **List Comprehension with Conditionals**
# Fix the syntax error in this list comprehension:

numbers = [1, 2, 3, 4, 5]
# evens = [x if x % 2 == 0 for x in numbers]

answer_2 = [x for x in numbers if x %2 ==0]

# 3. **Context Manager Syntax**
# What's missing in this context manager implementation?

# class FileManager:
#     def __init__(self, filename):
#         self.filename = filename
        
#     def __enter__(self):
#         self.file = open(self.filename, 'r')
#         return self.file

# answer ❌
class FileManager:

    def __init__(self, filename):
        self.filename = filename
    
    def __enter__(self):
        self.file = open(self.filename, 'r') # or 'w', depends on needs. sytntax ok
        return self.file
    
    def __exit(self, exc_type, exc_val, exc_tb):
        self.file.close() # each file entered must be closed when exiting context

"""
class DatabaseConnection:
    def __enter__(self):
        print("Opening connection")
        return self
        
    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Closing connection")
        
        if exc_type is ZeroDivisionError:
            print("Handled division by zero!")
            return True  # Suppress the exception
        
        return False  # Let other exceptions propagate

# Example usage
with DatabaseConnection() as db:
    # This will be caught and suppressed
    result = 1 / 0  # ZeroDivisionError
    
with DatabaseConnection() as db:
    # This will propagate
    x = undefined_variable  # NameError
"""
# 4. **Lambda Function Syntax**
# Correct the syntax error in this lambda function:

# multiply = lambda x, y: x * y if y > 0 else

answer_4 = lambda x,y: x * y if y > 0 else 0 # else statement must be explicit

# 5. **Generator Function Syntax**
# What's wrong with this generator function implementation?

# def fibonacci():
#     a, b = 0, 1
#     while True:
#         return a
#         a, b = b, a + b

# answer_5 ❌
def fibonacci(x,y):
    a, b = x, y
    while True:
        yield a # use yield instead of return
        a, b = b, a + b
        
print(fibonacci(2,3))

"""
Generator functions use yield to produce a sequence of values without storing them all in memory at once
"""