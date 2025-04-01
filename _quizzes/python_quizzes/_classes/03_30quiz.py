# Q1 What is the purpose of this class? 

class Dog:
    def __init__(self, name):
        self.name = name

dog = Dog("Buddy")

"""Answer The class contains a constructor method that allows it to take a string as a parameter."""

# Q2 What's the difference between total_count and count in this code?

class Counter:
    total_count = 0  # Class variable
    
    def __init__(self):
        self.count = 0  # Instance variable

"""Answer
total count is a class variable, which will remain exactly the same throughout all instances of this class. The count variable, although has the same properties as it's other instance copies, is unique to the instance in value.
"""

# Q3 Method types What's the difference between the fahrenheit and from_fahrenheit methods? How would you call each one?

class Temperature:
    # Constructor -takes parameter and assignes it to celsius
    def __init__(self, celsius):
        self._celsius = celsius
    
    # Property decorator method
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
    # Class method decorator
    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return cls(celsius)

temp = Temperature(25)

"""Answer
Property Decorator Acts like a getter method. Accessed like an attribute (no parentheses needed). Computes fahrenheit on-demand from celsius Usage: temp.fahrenheit. Class method
"""

# Q4

# Q5

# Q6

# Q7

# Q8

# Q9

# Q10