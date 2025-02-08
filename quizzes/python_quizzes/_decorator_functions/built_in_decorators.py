from functools import wraps, lru_cache, total_ordering
from typing import Any, Callable, TypeVar, cast
from abc import ABC, abstractmethod
from dataclasses import dataclass


# The `@` symbol is used for decorators in Python, and there are both built-in decorators and custom ones you can create:

# Built-in Decorators
class MyClass:
    @property               # ✅ Built-in: Makes method act like property
    def name(self):
        return self._name

    @classmethod           # ✅ Built-in: Method that works on class
    def class_method(cls):
        pass

    @staticmethod          # ✅ Built-in: Method that needs no class/instance
    def static_method():
        pass


# **Creating Custom Decorators:**
# Custom Decorator Function
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

# Using Custom Decorator
@my_decorator             # ✅ Custom: Your own decorator
def say_hello():
    print("Hello!")

# What happens behind scenes:
say_hello = my_decorator(say_hello)


# **Common Built-in Decorators:**
class Example:
    _name = "John"
    
    @property             # Getter
    def name(self):
        return self._name
    
    @name.setter         # Setter
    def name(self, value):
        self._name = value
    
    @classmethod        # Class method
    def from_string(cls, string):
        return cls()
    
    @staticmethod      # Static method
    def helper():
        return "I help"
        
    @abstractmethod    # From abc module
    def must_implement(self):
        pass


# **Creating More Complex Decorators:**
# Decorator with Parameters
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# Using Parameterized Decorator
@repeat(times=3)      # ✅ Custom decorator with parameters
def greet(name):
    print(f"Hello {name}")


# **Real-World Example:**
import time
import functools

# Custom Timing Decorator
def timer(func):
    @functools.wraps(func)  # Preserves function metadata
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.2f} seconds")
        return result
    return wrapper

# Using the Timer
@timer
def slow_function():
    time.sleep(1)
    return "Done!"

# Using Multiple Decorators
@timer
@classmethod
def class_operation(cls):
    time.sleep(1)


# Common Built-in Decorators:
# 1. `@property`
# 2. `@classmethod`
# 3. `@staticmethod`
# 4. `@abstractmethod`
# 5. `@functools.wraps`
# 6. `@contextlib.contextmanager`

