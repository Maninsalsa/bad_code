"""
pa_adv2_decorator_functions.py

Beginner:
In an agentic application built with a Python/Django backend, optimizing expensive
computations or API calls is crucial for performance. A common approach to achieve
this is using a decorator for caching results.

Your task is to create a Python decorator function to cache the results of another
function. The decorator should:

-Store cached results in a dictionary in memory.
-Use the function arguments to create a unique key for each result.
-Return the cached result if available, or compute and cache the result if not.
-Provide a beginner-friendly implementation for the decorator and demonstrate its
 use with a simple function.
"""

# Decorator = A Function that extends the behavior of another function
#             w/o modifying the base function
#             Pass the base function as an argument to the Decorator

# Step 2 # add a decorator function:
def add_sprinkles(func):
    def wrapper(): 
        # a wrapper function ensures the extended behavior is only applied when
        # the base function is called with the decorator function
        # not just when the decorator function is called via @<decorator>.
        print("*You add sprinkles🎊")
        func()
    return wrapper

# Step 1 create the base function
@add_sprinkles # This is syntactic sugar for: get_ice_cream = add_sprinkles(get_ice_cream)
def get_ice_cream():
    print("Here is your ice cream 🍨")

get_ice_cream()


"""
Advanced:
Question: Design a Python decorator function to implement memoization (caching) for
optimizing expensive computations or API calls in an agentic application built with
a Python/Django backend. The solution should include considerations for:

Handling variable arguments for the decorated function.
Using Django's caching framework for storage, with fallback support for local memory
caching.
Expiration of cached results after a configurable time period to maintain up-to-date
results.
Provide a code implementation and briefly explain how this would integrate into the
context of the backend development for an agentic application.
"""