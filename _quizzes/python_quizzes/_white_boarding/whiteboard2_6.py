"""
**Grading Criteria:**
- Completeness of component identification
- Logical flow of operations
- Consideration of edge cases
- Scalability considerations
- Clear separation of concerns

For each problem, provide:
1. System components/data structures needed
2. Step-by-step breakdown of operations
3. Edge cases to consider
4. Potential bottlenecks
5. Error handling considerations

"""


# DIFFICULTY BEGINNER

"""
1. **To-Do List Manager**
Problem: Design a simple to-do list that allows users to:

user adds string through terminal or UI 

Mark tasks as complete
Delete tasks
View all tasks
View only incomplete tasks

Break down the components and operations needed.
"""
#Directories
    # file directory
        # dictionary for complete/incomplete lists
        # dictionary for deleted lists
    # src
        # holds the list object main script that executes all 
        # holds the module with the list components

# Components
    # Data Sctructures
        # Inside file directory
            # dictonary to store created to-do list files
            # dictionary to store deleted files

        # list object -> file
            # creates empty to do list instances that can overwrite stored lists
            # or writes new list files

                # Instance variables
                    # tasks -> 2D list [[name string, status string], etc] for task name and completion status
                    # deleted tasks -> 2D list that cointains all popped task variables from the tasks list
                    # task variable -> [name string, status string]

                    # validation variable -> string
                        # value boolean == true for complete, false for incomplete
                        # has images that signify unfilled(False), pressed(when clicked), and filled(True). 
                        # returns the string complete or incomplete depending on boolean value. 

                # Instance methods

                    # Add tasks
                        # get user string input and adds it to the tasks list
                    # Mark tasks
                        # if else operations that change the boolean state of the value variable to false or true depending on current state
                    # Delete tasks
                        # pops task from tasks list and stores return values into deleted tasks. 
                    # View all tasks
                        # prints the 2D list sorted as complete and incomplete tasks in LIFO order
                    # View only incomplete tasks
                        # prints all tasks whose status is incomplete in LIFO order
                    # write lists
                        # creates a list file that represents the most current version of the list
                        # creates a list file that represents the tasks which were deleted and writes them to the deleted dictionary
                        # if the list already exists, it rewrites the file with the instances data
                        # if the list doesn't exists, it appends a new file into the dictionary. 

        # Edge Cases
            # an empty list is started
            # create a view for deleted items allow capability to restore them 
"""
2. **Basic Calculator**


Problem: Create a calculator that can:
- Add, subtract, multiply, divide
- Clear the current calculation
- Display current result
- Handle decimal numbers
- Show error for division by zero

Map out the necessary parts and operations.

"""
 # Directories
    # calculator module

        # contains calculator class:
            # constructor method(self)
                # class variables:

                # string input
                # stored value
                # 
                

    # main.py
        # imports os
        # imports sys
        # import tty
        # import termios
        # imports calculator module and initializes the Calculator object into a variable called calc

        # main then exectues a while true loop for continuous updates until operation is exited by user by pressing the esq button
        # in the while true loop


 # Data Structures

    # Dictionary for entry history for the last 20 entrees
        # in main.py should be fine
    
        





 # While True loop to keep updating the accepting inputs open:

 
"""
3. **Password Validator**
Problem: Design a system that checks if a password is valid by:
- Checking minimum length (8 characters)
- Requiring at least one uppercase letter
- Requiring at least one number
- Requiring at least one special character
- Returning specific error messages for failed criteria

Outline the validation steps and feedback system.
"""

# def is_password_valid(str) -> str:
    # Each condition should be flagged

    # minimum length is >= 8
    # at least one upper case? set to False
    # has one number? set to False
    # Has one symbol? set to False

    # Iterate over the string once and update the boolean values first
    # Booleans first because length of list(booleans) < password length guaranteed

  
    # the minimum amount of needed characters
        # if char.upper():
        #     set at least one upper case to True
        # if char.isdigit():
        #     set the one number flag to True
        # if not char.isalnum(): # combo .isalnum() with not
        #     set symbols flag to True

        # after each char is evaluated, exit early and proceed to all flags check

        # if length, and all booleans are true:
            # return True
        # else: 
            # return False
        

# methods, functions, combos:
    # .isallnum(), "not" operator 
        # .isallnum() checks that the iterable only contains numbers and letters, using not will confirm symbols
    # any()



"""
4. **Temperature Converter**
Problem: Create a temperature conversion tool that:
- Converts between Celsius and Fahrenheit
- Handles negative numbers
- Rounds to one decimal place
- Shows both temperatures simultaneously
- Validates input as numbers only

Break down the conversion logic and display requirements.
"""

"""
5. **Basic Contact List**
Problem: Design a simple contact manager that can:
- Add new contacts (name, phone, email)
- Display all contacts
- Search for a contact by name
- Delete contacts
- Prevent duplicate entries

Outline the structure and operations needed.
"""


# Difficulty: Progressive (Junior → Senior)

"""
1. **Shopping Cart Total Calculator**
Problem: Design a system that calculates the total price of items in a shopping cart, including:
- Multiple quantities of items
- Different discount types (percentage off, buy-one-get-one)
- Tax calculation
- Shipping costs based on total weight
- Coupon code application

Break this down into implementable steps and data structures needed.
"""

"""
2. **File Directory Tree Visualizer**
Problem: Create a command-line tool that displays a directory structure as a tree, with:
- Configurable depth levels
- File size information
- Option to show/hide hidden files
- Filter by file extension
- Count of files in each directory

Outline the component structure and processing steps.
"""
"""
3. **Tic-Tac-Toe Game State Manager**
Problem: Design the backend logic for a Tic-Tac-Toe game that handles:
- Player moves
- Win condition checking
- Draw condition checking
- Game history tracking
- Ability to undo moves

Break down the game logic and state management requirements.
"""
"""
4. **Task Scheduler**
Problem: Create a priority-based task scheduler that manages:
- Tasks with different priority levels
- Time-based execution
- Recurring tasks
- Task dependencies (Task B can't start until Task A completes)
- Resource allocation

Outline the system components and scheduling logic.
"""
"""
5. **Chat Room Message Handler**
Problem: Design a message handling system for a chat room that supports:
- Message broadcasting
- Private messages
- User presence tracking
- Message history
- Rate limiting for spam prevention
- Emoji/URL parsing

Break down the message flow and required components.
"""
