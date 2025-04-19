def count_vowels(string: str):
    vowels = ['a','e','i','o','u']
    return [vowel for vowel in string if vowel in vowels]

def fizzBuzz():

    number_range = list(range(1, 101))

    fizz_buzz_or_fizzBuzz = []

    for num in number_range:
        if not num % 3:
            fizz_buzz_or_fizzBuzz.append("fizz")
        elif not num % 5:
            fizz_buzz_or_fizzBuzz.append("buzz")
        elif not num % 3 and not num % 5: 
            fizz_buzz_or_fizzBuzz.append("fizzbuzz")
        else:
            fizz_buzz_or_fizzBuzz.append(num)
    return print(fizz_buzz_or_fizzBuzz)


answer12 = fizzBuzz()

"""Thanks for your answers! Let me go through them and provide some feedback:

1. ✓ Question 1: C is correct! You understood the type conversion.
2. ✓ Question 2: C is correct - good job understanding the order of operations.
3. ✓ Question 3: B is correct - you correctly identified the condition that applies.
4. ✓ Question 4: Your answer 6 matches with option B, which is correct.
5. ❌ Question 5: There's a misunderstanding here. Using `discount=True` when calling a function is valid Python syntax when the parameter has a default value. The correct answer is C (45.0).
6. ✓ Question 6: A is correct - good job tracking the list operations.
7. ✓ Question 7: D is correct - you understood the dictionary's `get()` method.
8. ✓ Question 8: You're right that A and B are identical ("pytING"). The correct answer is A.
9. ❌ Question 9: The answer should be B ("Division error, Done"). The code raises a ZeroDivisionError, so "Success" is never printed.
10. ✓ Question 10: A is correct - that's the proper way to open a file for reading.

For the implementation questions:

**Question 11 (Count Vowels):**
Your function returns a list of vowels rather than the count of vowels. Here's a small correction:


def count_vowels(string: str):
    vowels = ['a','e','i','o','u']
    return len([vowel for vowel in string.lower() if vowel in vowels])


The key improvements are:
1. Adding `.lower()` to make it case-insensitive
2. Using `len()` to count the vowels instead of returning the list
3. The function should return an integer, not a list

**Question 12 (FizzBuzz):**
There's a logical issue in your implementation. The "fizzbuzz" condition (divisible by both 3 and 5) needs to be checked first, otherwise, numbers like 15 will only match the first condition (divisible by 3). Also, your conditional logic isn't quite right:


def fizzBuzz():
    fizz_buzz_or_fizzBuzz = []
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:  # Check for both first
            fizz_buzz_or_fizzBuzz.append("fizzbuzz")
        elif num % 3 == 0:  # Then check for divisible by 3
            fizz_buzz_or_fizzBuzz.append("fizz")
        elif num % 5 == 0:  # Then check for divisible by 5
            fizz_buzz_or_fizzBuzz.append("buzz")
        else:
            fizz_buzz_or_fizzBuzz.append(num)
    return fizz_buzz_or_fizzBuzz  # Just return the list (don't print inside the function)

# To see the results
result = fizzBuzz()
print(result)


Your overall score is 7/12 - you've got a good understanding of Python basics but there are a few areas to review:
1. Function calling with keyword arguments
2. Exception handling flow
3. Function return values vs. printing
4. Logical order of conditionals"""

# Python Quiz: Targeted Practice

## Instructions
# - This quiz focuses on function arguments, exception handling, return values, and logical conditionals
# - Try to solve each question before checking the answers
# - For code questions, write out your solution first



### Question 1: Function Arguments
# What will be the output of the following code?


def greeting(name, message="Hello"):
    return f"{message}, {name}!"

print(greeting("Alice"))
print(greeting("Bob", message="Hi"))
print(greeting(message="Welcome", name="Charlie"))


# A) Error, the function calls are invalid  
# B) "Hello, Alice!", "Hi, Bob!", "Welcome, Charlie!"  
# C) "Hello, Alice!", "Hi, Bob!", Error in the third call  
# D) "Hello, Alice!", Error in the second call  



### Question 2: Keyword Arguments
# Which of the following function calls will result in an error?


def calculate(a, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    else:
        return a / b


# A) `calculate(5, 3)`  
# B) `calculate(5, operation="multiply", b=3)`  
# C) `calculate(a=5, b=3, operation="divide")`  
# D) `calculate(5, 3, "subtract", operation="multiply")`  



### Question 3: Default Arguments
# What's wrong with the following function definition?


def append_to_list(item, my_list=[]):
    my_list.append(item)
    return my_list


# A) Nothing, the function is correctly defined  
# B) The default argument is a mutable object, which can lead to unexpected behavior  
# C) Default arguments can't be used for parameters that aren't at the end  
# D) Return statements can't return parameters  



### Question 4: Exception Handling
# What will be the output of the following code?


try:
    print("Step 1")
    x = 1 / 0
    print("Step 2")
except ZeroDivisionError:
    print("Step 3")
else:
    print("Step 4")
finally:
    print("Step 5")


# A) Step 1, Step 2, Step 5  
# B) Step 1, Step 3, Step 4, Step 5  
# C) Step 1, Step 3, Step 5  
# D) Step 1, Step 5  



### Question 5: Exception Flow
# In the following code, what is printed?


def divide(a, b):
    try:
        result = a / b
        print("Division successful")
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    finally:
        print("Division operation completed")

print(divide(10, 2))


# A) Division successful, Division operation completed, 5.0  
# B) Division successful, 5.0, Division operation completed  
# C) Division successful, Division operation completed, None  
# D) 5.0, Division successful, Division operation completed  



### Question 6: Nested Exception Handling
# What will be the output of the following code?


try:
    try:
        print("Inner try")
        result = 10 / 0
    except TypeError:
        print("Inner except")
    finally:
        print("Inner finally")
except ZeroDivisionError:
    print("Outer except")
finally:
    print("Outer finally")


# A) Inner try, Inner except, Inner finally, Outer finally  
# B) Inner try, Inner finally, Outer except, Outer finally  
# C) Inner try, Inner except, Inner finally, Outer except, Outer finally  
# D) Inner try, Outer except, Inner finally, Outer finally  



### Question 7: Return Values
# What will be the value of `x` after the following code executes?


def process_list(items):
    if not items:
        return
    result = []
    for item in items:
        if item > 0:
            result.append(item * 2)
    return result

x = process_list([1, -2, 3, -4, 5])


# A) [2, 6, 10]  
# B) [2, -4, 6, -8, 10]  
# C) [1, -2, 3, -4, 5]  
# D) None  



### Question 8: Function Return Behavior
# What does the following function return when called with `get_status(200)`?


def get_status(code):
    if code == 200:
        print("OK")
    elif code == 404:
        print("Not Found")
        return code
    else:
        print("Unknown")
        return code


# A) 200  
# B) "OK"  
# C) None  
# D) The function raises an error  



### Question 9: Logical Conditionals
# What will the following code print?


def check_number(num):
    if num % 2 == 0 and num % 3 == 0:
        print("Divisible by both 2 and 3")
    elif num % 2 == 0:
        print("Divisible by 2")
    elif num % 3 == 0:
        print("Divisible by 3")
    else:
        print("Not divisible by 2 or 3")

check_number(6)


# A) Divisible by 2  
# B) Divisible by 3  
# C) Divisible by both 2 and 3  
# D) Not divisible by 2 or 3  



### Question 10: Logical Operator Precedence
# What will be the output of the following code?
# 

x = 5
y = 10
z = 15

if x < y and y < z or x > z:
    print("Condition 1")
else:
    print("Condition 2")


# A) Condition 1  
# B) Condition 2  
# C) Error  
# D) No output  



### Question 11: Code Implementation
# Write a function called `safe_divide` that takes two parameters, `a` and `b`, and returns the result of `a / b`. However, if `b` is zero, the function should return the string "Cannot divide by zero". Do not use try-except in your solution.



### Question 12: Code Implementation
# Write a function called `process_data` that takes a list of numbers and performs the following operations:
# 1. If the list is empty, return an empty dictionary
# 2. If the list contains negative numbers, remove them
# 3. Return a dictionary with the following keys:
#    - "sum": the sum of the remaining numbers
#    - "average": the average of the remaining numbers (return 0 if no numbers remain)
#    - "count": the count of the remaining numbers

# Example: 

# process_data([1, -2, 3, -4, 5]) should return {"sum": 9, "average": 3.0, "count": 3}




## Solutions

### Question 1: B
# All three function calls are valid. In the first call, the default message "Hello" is used. In the second call, the keyword argument `message="Hi"` overrides the default. In the third call, the order of arguments doesn't matter when using keyword arguments.

# ### Question 2: D
# # Option D will cause an error because it passes the positional argument "subtract" for the `operation` parameter and then tries to pass a keyword argument for the same parameter.

### Question 3: B
# The issue is that default arguments are evaluated only once when the function is defined, not each time the function is called. Since lists are mutable, the same list will be modified across multiple calls to the function. This is a common Python gotcha.

### Question 4: C
# The output will be:
# 1. "Step 1" - first print statement runs
# 2. Then `x = 1 / 0` raises a ZeroDivisionError
# 3. "Step 3" - the except block runs
# 4. "Step 5" - the finally block always runs
# The else block only runs if no exception is raised, so "Step 4" is not printed.

### Question 5: A
# The function successfully divides 10 by 2, so it prints "Division successful". Then the finally block runs, printing "Division operation completed". Finally, the function returns 5.0, which is printed by the outer print statement.

### Question 6: B
# 1. "Inner try" - from the inner try block
# 2. The inner block raises a ZeroDivisionError, but the inner except only catches TypeError
# 3. "Inner finally" - the inner finally block always runs
# 4. The ZeroDivisionError propagates to the outer try block, where it's caught
# 5. "Outer except" - the outer except block runs
# 6. "Outer finally" - the outer finally block always runs

### Question 7: A
# The function filters out negative numbers and doubles the positive ones:
# - [1, -2, 3, -4, 5] → [1, 3, 5] (after filtering) → [2, 6, 10] (after doubling)

### Question 8: C
# When `code` is 200, the function prints "OK" but doesn't explicitly return anything. In Python, when a function doesn't have a return statement, it implicitly returns `None`.

### Question 9: C
# The number 6 is divisible by both 2 and 3. The first condition `num % 2 == 0 and num % 3 == 0` is true, so "Divisible by both 2 and 3" is printed.

### Question 10: A
# The condition `x < y and y < z or x > z` is evaluated as `(x < y and y < z) or x > z`. Since 5 < 10 and 10 < 15, the first part is true, so the whole condition is true regardless of whether x > z. Therefore, "Condition 1" is printed.

### Question 11: Solution

def safe_divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


### Question 12: Solution

def process_data(numbers):
    if not numbers:
        return {}
    
    # Remove negative numbers
    positive_numbers = [num for num in numbers if num >= 0]
    
    # If no positive numbers remain
    if not positive_numbers:
        return {"sum": 0, "average": 0, "count": 0}
    
    # Calculate results
    total = sum(positive_numbers)
    count = len(positive_numbers)
    average = total / count
    
    return {
        "sum": total,
        "average": average,
        "count": count
    }


## Score Interpretation
# - 10-12 correct: Excellent! You've mastered these concepts
# - 8-9 correct: Good understanding, but review a few details
# - 6-7 correct: Decent grasp, focus on the areas you missed
# - Below 6: These concepts need more practice