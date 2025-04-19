import random


"""# Python syntax guide"""

# iterable generator 

# iterable = [
#     random.choice([
#         random.randint(-100, 100),  # integers
#         random.random() * 200 - 100,  # floats
#         random.choice([True, False]),  # booleans
#         random.choice(["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]),  # strings
#         (random.randint(1, 10), random.randint(1, 10)),  # tuples
#         [random.randint(1, 10) for _ in range(random.randint(1, 3))],  # small lists
#         {random.randint(1, 20) for _ in range(random.randint(1, 3))},  # small sets
#         {str(random.randint(1, 5)): random.randint(1, 100) for _ in range(random.randint(1, 2))}  # small dicts
#     ]) for _ in range(100)
# ]

# print(iterable)

iterable = [76, (2, 8), -57.90853794441144, 'cherry', [10, 10, 2], (3, 6), False, [9, 7], 19.089937386420132, -16, {'5': 3, '4': 86}, 76.84767522838348, 'cherry', {'2': 53, '5': 76}, (8, 3), (4, 7), {3}, (6, 1), 'banana', 'cherry', -19, {2}, {10}, {12}, False, True, {'5': 11, '3': 41}, 'banana', (6, 1), {10, 7}, 94.65329077765492, {'3': 12, '5': 92}, {19, 11, 13}, False, -24.288578530878354, (2, 10), 67.52905094442056, 'elderberry', {'3': 97}, [4], True, (3, 8), 69.73181866331149, True, 'fig', 'cherry', 'fig', True, 40.45761123919766, False, 'banana', {'5': 36, '2': 10}, {10}, 'apple', -12.18224227706608, 10, 33.3109974606252, 67.85249763154957, False, {1, 20, 7}, 63, True, {'5': 97}, -1.5147188314651032, {'5': 72, '4': 26}, (3, 6), {1, 6}, {'1': 79, '2': 93}, {2, 5, 15}, {11, 12}, True, (8, 3), 4.7309107949734255, -70.15720567475769, (2, 2), 82, [4], (7, 4), 'apple', {2, 14}, {12, 15}, [5], {10}, (8, 5), -5, 73, (10, 7), (2, 4), {19}, -32, [3], {9}, [6, 3, 9], 'grape', {17, 19, 7}, True, [10], {'5': 19}, {'3': 32, '5': 74}, 21.81193674547812]


"""Make a function that sorts all elements in iterable into separate lists of alike data types. the function should only have to iterate"""

def log_append(lst, item, list_name):
    # This is a helper function that prints 
    lst.append(item)
    print(f"Added {item} to {list_name}")
    return lst

def sort_by_type(iterable):
    # Initialize containers for each data type
    integers = []
    floats = []
    booleans = []
    strings = []
    tuples = []
    lists = []
    sets = []
    dicts = []
    other = []  # For unexpected types
    
    # Check if input is actually iterable
    try:
        iter(iterable)
    except TypeError:
        raise TypeError("Input must be an iterable")
    
    # Iterate through the iterable only once and categorize each element
    for item in iterable:
        try:
            # Special handling for booleans since they are a subclass of int
            if isinstance(item, bool):
                log_append(booleans, item, "booleans")
            elif isinstance(item, int):
                log_append(integers, item, "integers")
            elif isinstance(item, float):
                log_append(floats, item, "floats")
            elif isinstance(item, str):
                log_append(strings, item, "strings")
            elif isinstance(item, tuple):
                log_append(tuples, item, "tuples")
            elif isinstance(item, list):
                log_append(lists, item, "lists")
            elif isinstance(item, set):
                log_append(sets, item, "sets")
            elif isinstance(item, dict):
                log_append(dicts, item, "dicts")
            else:
                # Handle any other data types
                log_append(other, item, "other")
        except Exception as e:
            # In case of any unexpected errors during type checking
            print(f"Error processing item: {e}")
            log_append(other, item, "other")
    
    # Return a dictionary containing all categorized lists
    return {
        'INTEGERS': integers,
        'FLOATS': floats,
        'BOOLEANS': booleans,
        'STRINGS': strings,
        'TUPLES': tuples,
        'LISTS': lists,
        'SETS': sets,
        'DICTS': dicts,
        'OTHER': other
    }

answer = sort_by_type(iterable)

print(f"\nHere is the dictionary of your sorted data types:\n{answer}")