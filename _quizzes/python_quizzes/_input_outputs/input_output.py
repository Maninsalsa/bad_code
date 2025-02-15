# Python Quiz: Iteration, Mutables, and Built-in Functions
# Difficulty: Incrementing from Easy to Advanced
# Total Questions: 20

# EASY
# Q1: What is the output type of dict.items() vs dict.keys()?

"""ANSWER
dict.items() and dict.keys() both produce view objects that represent elements in a dictionary. 
dict.items() returns the key value pairs as a tuple, if there are more than one key value pair, 
it will return a tuple with a list of tuples that are key value pairs. e.g. dict([(key, 
value), (key, value), etc]) for dict.keys(), it returns a view object tuple that has a
list of strings that represent the keys in a dictionary""" 

# Q2: What built-in function converts a string into individual characters while maintaining mutability?

"""ANSWER
the list() built-in function creates a list object which elements are the iterable within the input string. 
the function is built in C and is more memory efficient than using a loop to do the same."""

# Q3: What is returned by list.pop(0) vs list.pop()?

"""ANSWER
list.pop(0) modifies the list by removing an element from the input list and returns the specified element and retains it's datatype"""

# Q4: What happens when using .remove() on a list if the value appears multiple times?
"""ANSWER
.remove() takes the first instance of the element removed, and returns NONE, which is very different than using .pop()"""


# MEDIUM
# Q5: What is the output and why?
# x = [1, 2, 3]
# y = x.copy()
# y.extend([4, 5])
# x.append(6)
# print(x, y)

Q5 = ([1, 2, 3, 6], [1, 2, 3, 4, 5])

# Q6: How do the return types differ?
a = map(str, [1, 2, 3])
# b = [str(x) for x in [1, 2, 3]]
c = (*map(str, [1, 2, 3]),)

print(type(a))
print(type(c))

"""ANSWER
a is a map object which if iterated on will return a list of string versions of the numbers,
b returns a new list of strings, and c unpacks the map object and creates a tuple of string versions of the input list
"""

# Q7: What happens in memory when performing:
# dict1.update(dict2) vs dict3 = dict1 | dict2

# Q8: What is the difference between sorted(dict) vs dict.keys()?

# HARDER
# Q9: Explain the output:
# x = [1, 2, 3]
# y = (x, x)
# x.append(4)
# print(y)

# Q10: What happens in memory:
# x = [1, 2, 3]
# y = [x] * 3
# x.append(4)
# print(y)

# Q11: Compare the return types and mutability:
# x = "1,2,3".split(",")
# y = list("1,2,3")
# z = [*"1,2,3"]

# Q12: What is the output and why?
# d = {1: "one", 2: "two"}
# keys = d.keys()
# d[3] = "three"
# print(len(keys))

# ADVANCED
# Q13: Explain the memory implications:
# x = [1, 2, [3, 4]]
# y = x.copy()
# y[2][0] = 5
# print(x)

# Q14: What happens and why?
# x = {1: [1, 2], 2: [3, 4]}
# y = dict(x)
# y[1].append(3)
# print(x)

# Q15: Compare the iteration behavior:
# d = {1: "one", 2: "two"}
# x = iter(d)
# y = iter(d.items())
# z = iter(d.values())

# Q16: What is the output type and memory behavior?
# x = [1, 2, 3]
# y = filter(lambda n: n > 1, x)
# x.append(4)
# print(list(y))

# EXPERT
# Q17: Explain the difference in memory and performance:
# from itertools import chain
# x = [1, 2, 3]
# y = [4, 5, 6]
# a = list(chain(x, y))
# b = x + y
# c = [*x, *y]

# Q18: What happens in memory:
# class Custom:
#     def __iter__(self): return iter([1, 2, 3])
# x = Custom()
# a = list(x)
# b = list(x)
# print(a is b)

# Q19: Compare the behavior and efficiency:
# x = {1: "one", 2: "two"}
# a = {k: v for k, v in x.items()}
# b = dict(x.items())
# c = {**x}

# Q20: Explain the output and memory implications:
# from collections import defaultdict
# x = defaultdict(list)
# y = x.copy()
# y[1].append(2)
# print(x)


