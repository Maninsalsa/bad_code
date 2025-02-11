# **Python Whiteboarding Quiz - Beginner Level**

# Question 1: Basic Function Whiteboarding
# Write pseudocode to create a function that takes a list of numbers and returns their sum.
# Break down the steps needed:
# 1. Define the function name and parameter
# 2. Initialize a variable to store the sum
# 3. Iterate through the list
# 4. Add each number to sum
# 5. Return the final sum

"""
Answer:

name function create sum([list of nums]) -> number:
    container to hold sum of the list of numbers

    for each number in the list:
        add the number value to the container
    return the container

    OR

name function create sum([list of nums]) -> number:
    container to hold the sum of the list of numbers = sum([list of nums])
    return container

Coded:

def the sum(list) -> int:
    the_sum = sum(list)
    return the_sum
"""


# Question 2: Simple Class Design
# Write pseudocode for a basic Car class with the following requirements:
# - Should have attributes for make, model, and year
# - Should have a method to display car info
# Steps:
# 1. Define class name
# 2. Create __init__ method with parameters
# 3. Initialize instance variables
# 4. Create display_info method
# 5. Format and return car information string

"""
Answer:

class CarDesign:
    Car_details = {"car_name"} : {"car_make", "car_model","car_year"}}

    def __init__(self, make, model, year)
        self.make = make
        self.model = model
        self.year = year

    def display_info(self)
        print(self.make, self.model, self.year)




"""

# Question 3: Basic API Endpoint
# Write pseudocode for creating a simple REST API endpoint that returns user data:
# Steps:
# 1. Import necessary frameworks
# 2. Define route/endpoint
# 3. Create function to handle GET request
# 4. Get user data from database/source
# 5. Return JSON response
# 6. Add error handling

# Question 4: File Processing
# Write pseudocode for reading a text file and counting word frequency:
# Steps:
# 1. Open file with proper error handling
# 2. Initialize empty dictionary for word counts
# 3. Read file line by line
# 4. Split lines into words
# 5. Count word occurrences
# 6. Close file
# 7. Return word frequency dictionary

# Question 5: Data Structure Implementation
# Write pseudocode for implementing a basic stack data structure:
# Steps:
# 1. Create Stack class
# 2. Initialize empty list for storage
# 3. Implement push method
# 4. Implement pop method
# 5. Implement peek method
# 6. Add size check methods
# 7. Include error handling for empty stack

# For each question, provide:
# 1. The step-by-step pseudocode
# 2. Any potential edge cases to consider
# 3. Time/space complexity analysis
# 4. Alternative approaches if applicable

