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