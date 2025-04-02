"""Functions that take in functions as arguements are called decorator functions/ wrapper functions. They add functionality to the original function, while maintaing the original's functionality. They are a great way to maintain the og function, which may need to be called in it's orginal form in other parts of the script, but adds 'icing' on the cake, if you will, in other specific examples."""

# Q1
def greet():
    return "Hello!"

def uppercase_wrapper(func):
    def wrapper():
        return func().upper()
    return wrapper

no_wrapper = greet()
print(f"Before wrapper is applied:{no_wrapper}")

greet = uppercase_wrapper(greet)
result = greet()
print(f"After wrapper is applied: {result}")

"""Answer
The output is "HELLO!" uppercase_wrapper() takes greet() as an argument, and applies the .upper() method to the return value of greet(). While this can be achieved by assigning greet() to a variable and calling the .upper() method to it, this example shows the functionality of wrapper functions in a simple way. 
"""

# Q2 What's wrong with this wrapper implementation?

def log_function(func):
    print(f"Calling {func.__name__}")
    return func()

check = log_function()

"""Answer
.__name__ isn't a built in method and hasn't been defined
"""

"""Correct answer:
The decorator structure was not correctly implemented. the .__name__ is a valid built-in method, but the decorator needs to return a wrapper function that calls the original function when executed. In this example, the logging only happens when python interprets the defined function, not every time the wrapper is called.
"""

# Incorrect implementation
def log_function(func):
    print(f"Calling {func.__name__}")  # This happens ONCE when decorator is applied
    return func()  # Returns the result of calling the function

@log_function
def greet(name):
    return f"Hello, {name}!"

# The logging happens when Python reads this decorator
# After this point, calling greet() won't trigger any logging

# Correct implementation
def log_function(func):
    def wrapper(*args, **kwargs): # these parameters
        print(f"Calling {func.__name__}")  # This happens EVERY time wrapper is called
        return func(*args, **kwargs)
    return wrapper

@log_function
def greet(name):
    return f"Hello, {name}!"

# Manual decoration syntax
def greet(name):
    return f"Hello,{name}"
greet = log_function(greet)


# Now when we call greet():
greet("Alice")  # Prints "Calling greet" then returns "Hello, Alice!"
greet("Bob")    # Prints "Calling greet" then returns "Hello, Bob!"

"""
# Syntax explanation

# Function 1: The decorator function (outer function)
def log_function(func):                    # Takes the target function as parameter
    # Function 2: The wrapper function (inner function)
    def wrapper(*args, **kwargs):          # Takes any arguments meant for target
        print(f"Calling {func.__name__}")  # Add new functionality
        return func(*args, **kwargs)       # Call target function
    return wrapper                         # Decorator returns the wrapper function

# Function 3: The target function (function being wrapped)
@log_function
def greet(name):                          # This is the function we want to modify
    return f"Hello, {name}!
"""

# Q3 How would you fix this wrapper to preserve the og function's metadata?

def debug(func):
    def wrapper():
        print(f"Calling {func.__name__}")
        return func()
    return wrapper

@debug
def greet():
    """Says hello"""
    return "Hello!"
