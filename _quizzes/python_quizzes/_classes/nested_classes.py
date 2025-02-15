# nested classes

class Outer:
    outer_var = "I'm in the outer class"
    
    def __init__(self):
        self.outer_instance_var = "I'm an outer instance variable"
    
    # This is a nested class
    class Inner:
        inner_var = "I'm in the inner class"
        
        def __init__(self):
            self.inner_instance_var = "I'm an inner instance variable"
            
        def inner_method(self):
            return "Inner method called"
    
    def create_inner(self):
        # Create an instance of Inner class
        return self.Inner()

# Usage examples:
# 1. Creating an Inner class instance through Outer
outer = Outer()
inner = outer.Inner()
print(inner.inner_method())  # "Inner method called"

# 2. Creating Inner class directly
inner2 = Outer.Inner()
print(inner2.inner_var)  # "I'm in the inner class"

"""
Key points about nested classes:
Scope and Access:
The inner class can be accessed through the outer class
The inner class doesn't automatically have access to the outer class's instance attributes
The inner class can access the outer class's class variables
"""



"""
Nested class comparison vs the use of other containers

"""

# Approach 1: Using nested State class
class TrafficLight:
    class State:
        RED = "red"
        YELLOW = "yellow"
        GREEN = "green"
    
    def __init__(self):
        self.current_state = self.State.RED

# Approach 2: Using class variables
class TrafficLight:
    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"
    
    def __init__(self):
        self.current_state = self.RED


# Benefits of using the nested State class:

# 1. **Namespace Organization**:
#    - States are grouped under `State.`, making it clear these values are related
#    - Prevents name collisions (imagine if you needed RED for something else)
#    - Usage is more explicit: `TrafficLight.State.RED` vs `TrafficLight.RED`

# 2. **Better Code Completion**:
#    - When typing `TrafficLight.State.`, your IDE will only show state-related options
#    - Helps with discoverability of related constants

# 3. **Encapsulation**:
#    - Keeps state-related logic contained within the State class
#    - Prevents direct modification of state values from outside
#    - Allows adding state-specific methods (e.g., validation, transitions)
#    - Makes it easier to maintain and modify state-related code
#    - Provides a clear boundary between traffic light logic and its states

# Example:

class TrafficLight:
    class State:
        RED = "red"
        YELLOW = "yellow"
        GREEN = "green"
        
        @classmethod
        def all_states(cls):
            return [cls.RED, cls.YELLOW, cls.GREEN]
        
        @classmethod
        def is_valid_state(cls, state):
            return state in cls.all_states()
   
# Usage
print(TrafficLight.State.is_valid_state("red"))  # True
print(TrafficLight.State.is_valid_state("blue")) # False


# 4. **Type Hinting**:
#    - Enables static type checking for state values
#    - Provides better IDE support and code completion
#    - Makes code more self-documenting and explicit
#    - Helps catch type-related errors early
#    - Works well with Literal type for fixed set of values
#    - Improves code maintainability and readability

from typing import Literal

class TrafficLight:
    class State:
        RED = "red"
        YELLOW = "yellow"
        GREEN = "green"
        
        StateType = Literal["red", "yellow", "green"]

    def __init__(self) -> None:
        self.current_state: self.State.StateType = self.State.RED


"""
However, if your use case is very simple and you don't need these benefits, using class
variables directly might be more straightforward. It's about choosing the right level of
complexity for your needs.

"""

"""Let's compare using a dictionary approach with the previous methods:"""

# Approach 1: Dictionary as a class variable
class TrafficLight:
    STATES = {
        'RED': 'red',
        'YELLOW': 'yellow',
        'GREEN': 'green'
    }
    
    def __init__(self):
        self.current_state = self.STATES['RED']

# Approach 2: Nested State class (from previous example)
class TrafficLight:
    class State:
        RED = "red"
        YELLOW = "yellow"
        GREEN = "green"
    
    def __init__(self):
        self.current_state = self.State.RED


# Key differences:

# 1. **Syntax and Access**:
# Dictionary approach
light = TrafficLight()
light.current_state = TrafficLight.STATES['RED']    # Requires string key

# State class approach
light = TrafficLight()
light.current_state = TrafficLight.State.RED        # Direct attribute access


# 2. **Mutability**:
# Dictionaries are mutable
TrafficLight.STATES['RED'] = 'crimson'      # Can be modified
TrafficLight.STATES['PURPLE'] = 'purple'    # Can add new keys

# Class attributes are more protected
TrafficLight.State.RED = 'crimson'          # Can be modified but less common
TrafficLight.State.PURPLE = 'purple'        # Requires class modification


# 3. **Type Safety and IDE Support**:

# Dictionary - less IDE support
def change_state(self):
    if self.current_state == self.STATES['RED']:    # No autocomplete on 'RED'
        self.current_state = self.STATES['GREEN']   # Possible typos in keys

# State class - better IDE support
def change_state(self):
    if self.current_state == self.State.RED:        # IDE autocompletes
        self.current_state = self.State.GREEN       # IDE catches typos


# 4. **Validation and Methods**:

# Dictionary approach requires extra work for validation
class TrafficLight:
    STATES = {
        'RED': 'red',
        'YELLOW': 'yellow',
        'GREEN': 'green'
    }
    
    @classmethod
    def is_valid_state(cls, state):
        return state in cls.STATES.values()

# State class makes it more natural
class TrafficLight:
    class State:
        RED = "red"
        YELLOW = "yellow"
        GREEN = "green"
        
        @classmethod
        def is_valid_state(cls):
            return [cls.RED, cls.YELLOW, cls.GREEN]


# The dictionary approach might be better when:
# - You need to dynamically add/remove states
# - You're working with data that naturally maps to key-value pairs
# - You need to iterate over states frequently
# - You're loading states from a configuration file

# The State class approach might be better when:
# - You want better IDE support and type checking
# - Your states are fixed and won't change
# - You want to add methods or additional functionality to the states
# - You want to prevent accidental modifications to the states

"""In most simple cases, the State class approach is cleaner and safer, but dictionaries
can be more flexible when you need that flexibility.
"""

"""
Lesson of the day:

when choosing containers for data inside your class consider:
are they just constant simple values needed in each instance? -> variable

do the variables that have potential to be used in nested class methods or will be used for validation? -> nested classes

will the values of the containers constantly change and flexibility is needed, and does your class call for key value pair organizations -> dict
"""