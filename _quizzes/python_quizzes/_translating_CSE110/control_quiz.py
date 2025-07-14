
# # ========== CONDITIONAL STATEMENTS QUIZ ==========

# # 1. What will be printed?
# x = 7
# if x < 10:
#     print("Q1:", "A" if x < 10 else "B")

# # 2. What is the output?
# y = 4
# if y % 2 == 0:
#     print("Q2:", "Even")
# else:
#     print("Q2:", "Odd")

# # 3. What grade will be printed?
# score = 72
# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# else:
#     grade = "D or F"
# print("Q3:", grade)

# # ========== FOR LOOPS QUIZ ==========

# # 1. What will this print?
# print("Q4:", end=" ")
# for i in range(3):
#     print(i, end=" ")
# print()

# # 2. What is the sum?
# total = 0
# for n in [1, 2, 3]:
#     total += n
# print("Q5:", total)

# # 3. What will be printed?
# for char in "hi":
#     print(f"Q6: {char}")

# # ========== WHILE LOOPS QUIZ ==========

# # 1. What will this print?
# count = 0
# while count < 2:
#     print("Q7:", count)
#     count += 1

# # 2. What is the final value of z?
# z = 5
# while z > 0:
#     z -= 2
# print("Q8:", z)

# # 3. What will be printed?
# n = 3
# while n:
#     print("Q9:", n)
#     n -= 1

# # ========== LIST COMPREHENSIONS QUIZ ==========

# # 1. What is the result?
# lst = [x * 2 for x in range(3)]
# print("Q10:", lst)

# # 2. What is the output?
# evens = [n for n in range(6) if n % 2 == 0]
# print("Q11:", evens)

# # 3. What will be printed?
# squares = [i**2 for i in [1, 2, 3]]
# print("Q12:", squares)

# # ========== DICTIONARY COMPREHENSIONS QUIZ ==========

# # 1. What is the result?
# d = {x: x**2 for x in range(2)}
# print("Q13:", d)

# # 2. What is the output?
# letters = {c: ord(c) for c in 'ab'}
# print("Q14:", letters)

# # 3. What will be printed?
# nums = {n: n+1 for n in [2, 4]}
# print("Q15:", nums)

# # ========== MATCH-CASE (PYTHON 3.10+) QUIZ ==========

# # 1. What will be printed?
# def match_q16(val):
#     match val:
#         case 1:
#             return "one"
#         case 2:
#             return "two"
#         case _:
#             return "other"
# print("Q16:", match_q16(2))

# # 2. What is the output?
# def match_q17(val):
#     match val:
#         case "a":
#             return "A"
#         case "b":
#             return "B"
#         case _:
#             return "?"
# print("Q17:", match_q17("c"))

# # 3. What will be printed?
# def match_q18(val):
#     match val:
#         case int() if val > 0:
#             return "positive"
#         case int() if val < 0:
#             return "negative"
#         case _:
#             return "zero or not int"
# print("Q18:", match_q18(-5))

# # ========== DICTIONARY AS SWITCH-CASE QUIZ ==========

# # 1. What is the result?
# days = {1: "Mon", 2: "Tue", 3: "Wed"}
# print("Q19:", days.get(2, "Unknown"))

# # 2. What will be printed?
# actions = {0: "stop", 1: "go"}
# print("Q20:", actions.get(3, "wait"))

# # 3. What is the output?
# nums = {10: "ten", 20: "twenty"}
# print("Q21:", nums.get(10))


# ========== QUIZ SYNTAX: HOW DO YOU WRITE... ==========

# How do you write a basic if statement in Python?
print("How do you write a basic if statement in Python?\n")

x = int(input("Type something, anything: "))
y = int(input("Type one more thing: "))

if x == y:
    print("Equal")
elif x < y:
    print("shmaller")
elif x > y:
    print("bigger")
else:
    print("nope, sorry, no peaches")

print()

# question: How do you write a basic if statement that checks if x is greater than 5 and prints "x is big?"
print("How do you write a basic if statement that checks if x is greater than 5 and prints \"x is big?\"\n")

x = int(input("pick a number: "))
if x > 5:
    print("x is big?")

print()


# How do you write an if-else statement in Python?
print("How do you write an if-else statement in Python?\n")

x = "Spain"
y = "Maine"

if x > y:
    print(1)
else:
    print(0)

print()


# question: How do you write an if-else statement that prints "even" if x is even, otherwise "odd"?
print("How do you write an if-else statement that prints \"even\" if x is even, otherwise \"odd\"?\n")
x = int(input("Pick an int: "))

if x % 2 == 0:
    print("even")
else:
    print("odd")

print()


# How do you write an if-elif-else chain in Python?
print("How do you write an if-elif-else chain in Python?\n")
# for time reasons, I just copied paste my first answer, as I took it too far
x = int(input("Type something, anything: "))
y = int(input("Type one more thing: "))

if x == y:
    print("Equal")
elif x < y:
    print("shmaller")
elif x > y:
    print("bigger")
else:
    print("nope, sorry, no peaches")

print()

# question: How do you write an if-elif-else chain that prints "A" if score >= 90, "B" if score >= 80, otherwise "C"?
print('question: How do you write an if-elif-else chain that prints "A" if score >= 90, "B" if score >= 80, otherwise "C"?\n')

score = int(input("What's the score?: "))
if score >= 90:
    print("A")
elif score >=80:
    print("B")
else:
    print("C")

print()


# How do you write a for loop over a range in Python?
print("How do you write a for loop over a range in Python?\n")

answer = [num for num in range(0, 11)]
print(answer)

for num in range(0, 11):
    print(num, end=" ") 

print()

# question: How do you write a for loop that prints numbers 0 to 4?
print("How do you write a for loop that prints numbers 0 to 4?\n")

loop_0_through_4 = [num for num in range(0,5)]
print(loop_0_through_4)

print()

# How do you write a for loop over a list in Python?
print("How do you write a for loop that prints each fruit in a list called fruits?\n")

# question: How do you write a for loop that prints each fruit in a list called fruits?
fruits = ["apple", "banana", "cherry", "orange", "grape", "kiwi", "mango", "pear", "peach", "plum"]

def fruit_printer(fruits: list) -> str:
    for fruit in fruits:
        print(fruit)

printed_fruit = fruit_printer(fruits)


print()

# How do you write a for loop with index in Python?
print("How do you write a for loop that prints the index and value for each fruit in fruits?\n")

my_list = range(1, 11)

for index,value in enumerate(my_list):
    print(index, value)



# question: How do you write a for loop that prints the index and value for each fruit 
for index, value in fruits:
    print(index, value)

print()

# How do you write a for loop over a dictionary in Python?
print("How do you write a for loop that prints each key and value in a dictionary called person?\n")

# No, this is not correct syntax.
# The variable 'person' is being assigned a set of dictionaries, which is invalid because dictionaries are unhashable types and cannot be elements of a set.
# Also, to iterate over key-value pairs in a dictionary, 'person' should be a dictionary, not a set or list of dictionaries.
# Here is the correct syntax for a dictionary and iterating over its key-value pairs:

person = {
    "name": "Billy",
    "age": 25,
    "city": "New York"
}

for key, value in person.items():
    print(key, value)


print()

# How do you write a while loop in Python?
# question: How do you write a while loop that prints count from 0 to 2?
print("How do you write a while loop that prints count from 0 to 2?\n")

num = 0
while num < 3:
    print(num)
    # Python does not support the ++ syntax (e.g., num++). Use += 1 instead.
    num += 1

print()

# How do you write a basic list comprehension in Python?
print("How do you write a list comprehension that makes a list of squares from 0 to 5?\n")

comprehension = [square**2 for square in range(0,6)]

print()

# How do you write a list comprehension with a condition in Python?
# question: How do you write a list comprehension that makes a list of even squares from 0 to 9?
print("How do you write a list comprehension that makes a list of even squares from 0 to 9?\n")

squares = range(0,10)

even_squares = [square**2 for square in squares if square % 2 == 0]

print()

# How do you write a dictionary comprehension in Python?
# question: How do you write a dictionary comprehension that maps x to x squared for x in range(6)?
print("How do you write a dictionary comprehension that maps x to x squared for x in range(6)?\n")

# A dictionary comprehension in Python allows you to create a new dictionary by specifying an expression for the keys and values, followed by a for clause, and optionally an if clause for filtering.

# The general syntax is:
# {key_expression: value_expression for item in iterable [if condition]}
# For example, {x: x**2 for x in range(6) if x % 2 == 0} creates a dictionary mapping each even x to its square for x from 0 to 5.


dict_comp = {x: x**2 for x in range(6)}
print(dict_comp)


print()

# How do you write a set comprehension in Python?# question: How do you write a set comprehension that gets the length of each fruit in 
print("How do you write a set comprehension that gets the length of each fruit in fruits?\n")

fruits = ['apple', 'banana', 'cherry', 'date']
lengths = {len(fruit) for fruit in fruits}
print(lengths)


print()

# How do you write a generator expression in Python?
print("How do you write a generator expression that yields x squared for x in range(6)?\n")

# A generator expression in Python is similar to a list comprehension, but it uses parentheses () instead of square brackets [].
# It creates an iterator that yields items one by one, which is memory efficient for large data.

# Syntax:
# (expression for item in iterable [if condition])

# Example use case: Summing the squares of numbers from 0 to 5 without creating an intermediate list.
gen_expr = (x**2 for x in range(6))

# To use the generator, you can iterate over it or use functions like sum():
print("Sum of squares from 0 to 5:", sum(gen_expr))

# If you want to see the values, you can convert it to a list:
gen_expr = (x**2 for x in range(6))  # recreate generator since it was exhausted
print("Squares from 0 to 5:", list(gen_expr))


print()

# How do you write a tuple comprehension in Python?
print("How do you write a tuple comprehension that gets the length of each fruit in fruits?\n")

# # Note: There is no direct 'tuple comprehension' in Python.
# # If you use parentheses with a comprehension, you get a generator expression, not a 
# tuple.
# # To create a tuple from a comprehension, you can use the tuple() constructor on a 
# generator expression.
# No, it's not because tuples are immutable. 
# The reason is that in Python, using parentheses with a comprehension creates a generator expression, not a tuple.
# To get a tuple, you need to pass the generator expression to the tuple() constructor.

fruits = ['apple', 'banana', 'cherry', 'date']
lengths_tuple = tuple(len(fruit) for fruit in fruits)
print(lengths_tuple)

print()


# How do you write a switch-case in Python (using match-case)?
print("How do you write a match-case statement that returns \"one\" for 1, \"two\" for 2, and \"other\" otherwise?\n")

# Skeleton for match-case (Python 3.10+)
value = 4
match value:
    case 1:
        # your code for case 1
        print("one")
    case 2:
        # your code for case 2
        print("two")
    case _:
        # your code for default case
        print("other")

# In a switch-case statement (or match-case in Python), the main keywords are:
# - 'match': This keyword starts the switch-like statement and is followed by the value you want to compare.
# - 'case': Each 'case' keyword introduces a possible value or pattern to match against the value given to 'match'.
# - '_': The underscore is used as a "catch-all" or default case, similar to 'default' in other languages.
# In Python, the structure looks like:
# match value_to_check:
#     case possible_value1:
#         # code to run if value_to_check == possible_value1
#     case possible_value2:
#         # code to run if value_to_check == possible_value2
#     case _:
#         # code to run if no other case matches (default)

print()

# How do you write a switch-case in Python (using a dictionary)?
print("How do you write a function that returns the day of the week for numbers 1-7 using a dictionary?\n")

# Yes, this is an example of using a dictionary to mimic switch-case behavior in Python.
# The function maps numbers 1-7 to days of the week, similar to how a switch-case would work in other languages.

def get_day_of_week(n):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    # The .get() method acts like the 'default' case in switch-case.
    return days.get(n, "Invalid day")

# Example usage:
for i in range(0, 9):
    print(f"{i}: {get_day_of_week(i)}")


print()

