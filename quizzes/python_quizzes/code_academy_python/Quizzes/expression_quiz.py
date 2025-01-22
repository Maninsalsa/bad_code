import random

def gen_random_list(l_length, min, max):
    length = l_length
    min_value = min
    max_value = max

    random_list = []

    for i in range(length): 
        value = [random.randint(min_value, max_value)]
        random_list += value
    return random_list

print(gen_random_list(10, 1, 100))

"""
Reverse Access:
You have a list lst and you want to access elements from the end to the start as you iterate forward through another list. What equation would you use?
"""
random_numbers = [82, 79, 22, 9, 27, 46, 40, 96, 7, 31]

def access_reverse_list(list):
    # create an expression that represents the end of the list
    # the end of the list index == the len(list)
    # remember indexes start at 0 unless specified so the last index is always len(list) - 1
    # to iterate through the list, len(list) - 1 - i
    reverse_list = []
    for index in range(len(list) - 1, - 1, -1):
        reverse_list.append(list[index])
    return reverse_list
print(f"o.g. list: {random_numbers}\nreverse list : {access_reverse_list(random_numbers)}")

"""
Middle-Out Access:
You have a list lst and you want to access elements starting from the middle and moving outward in both directions. How would you calculate the indices?
"""

print(type(sum([1,2,3])))
"""
Skip Every Other Element:
"""
"""
You want to access every other element in a list lst starting from the end. What equation would you use to calculate the indices?
"""
"""
Access in Pairs:
"""
"""
You have a list lst and you want to access elements in pairs, starting from the end. How would you calculate the indices for each pair?
"""
"""
Zigzag Pattern:
You want to access elements in a zigzag pattern: start from the end, then the start, then the second-to-last, then the second, and so on. How would you calculate the indices?
Feel free to attempt these, and let me know when you're ready for the answers!
"""