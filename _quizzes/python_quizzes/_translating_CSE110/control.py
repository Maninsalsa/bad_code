
# ========== CONDITIONAL STATEMENTS ==========

# Basic if statement
x = 10
if x > 5:
    print("x is greater than 5")

# if-else statement
if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")

# if-elif-else chain
score = 87
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D or F")

# ========== FOR LOOPS ==========

# Looping over a range of numbers
for i in range(5):
    print(f"i is {i}")

# Looping over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Looping with index (using enumerate)
for idx, fruit in enumerate(fruits):
    print(f"Fruit #{idx}: {fruit}")

# Looping over a dictionary
person = {"name": "Alice", "age": 30}
for key, value in person.items():
    print(f"{key}: {value}")

# ========== WHILE LOOPS ==========

count = 0
while count < 3:
    print(f"count is {count}")
    count += 1

# Infinite loop (be careful!)
# while True:
#     print("This will run forever unless you break out of it.")

# ========== LIST COMPREHENSIONS ==========

# Basic list comprehension
squares = [x * x for x in range(6)]
print("Squares:", squares)

# List comprehension with condition
even_squares = [x * x for x in range(10) if x % 2 == 0]
print("Even squares:", even_squares)

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6]]
flattened = [num for row in matrix for num in row]
print("Flattened:", flattened)

# ========== OTHER COMPREHENSIONS ==========

# Dictionary comprehension
squares_dict = {x: x * x for x in range(6)}
print("Squares dict:", squares_dict)

# Set comprehension
unique_lengths = {len(fruit) for fruit in fruits}
print("Unique fruit name lengths:", unique_lengths)

# Generator expression (creates a generator, not a list)
squares_gen = (x * x for x in range(6))
print("Squares from generator:", list(squares_gen))

# ========== SWITCH CASE ==========

# Python does not have a traditional switch-case statement.
# Instead, use match-case (Python 3.10+) or dictionaries.

# Using match-case (Python 3.10+)
def number_to_string(n):
    match n:
        case 1:
            return "one"
        case 2:
            return "two"
        case 3:
            return "three"
        case _:
            return "something else"

print(number_to_string(2))

# Using dictionary as a switch-case alternative
def day_of_week(n):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return days.get(n, "Invalid day")

print(day_of_week(5))