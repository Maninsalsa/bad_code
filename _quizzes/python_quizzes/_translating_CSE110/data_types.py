name = input("What's your name? ")
print(f"hello {name}")

# primitive data types 

# Integers
my_integer = 43
negative_integer = -34
zero_int = 0

# floats
my_float = 43.1

# Strings
my_string = "Wow, python is so clean"

# booleans different from java in that it's upper case
my_bool = True


# ======= COLLECTION DATA TYPES (no type hints) =======
# List: ordered, mutable, allows duplicates; can hold any data types
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed_list = [1, "hello", 3.14, True]  # heterogeneous

# Tuple: ordered, immutable, allows duplicates; can hold any data types
coordinates = (10, 20)
person = ("Alice", 30, False)
single_element_tuple = (42,)
example_tuple = (42, "banana", False)  # heterogeneous

# Set: unordered, mutable, unique items; all items must be hashable
unique_numbers = {1, 2, 3, 2, 1}
unique_fruits = {"apple", "banana", "cherry"}
example_set = {1, 2.0, "three"}  # heterogeneous

# Frozenset: unordered, immutable, unique items; all items must be hashable
frozen_numbers = frozenset([1, 2, 3, 2, 1])
frozen_fruits = frozenset(["apple", "banana", "cherry"])
example_frozenset = frozenset([1, "apple", 3.14])  # heterogeneous

# Dict: key-value pairs, mutable, keys unique & hashable; values and keys can be any type
person_info = {"name": "Bob", "age": 25, "is_student": True}
fruit_colors = {"apple": "red", "banana": "yellow", "cherry": "red"}
example_dict = {"name": "Alice", 1: [1, 2, 3], 3.14: True}  # mixed key/value types

# ======= USE CASES =======
# - List: sequence where order and mutability matter
# - Tuple: fixed group of related data, immutable
# - Set/Frozenset: unique items, set operations, frozenset is immutable
# - Dict: fast lookup by unique keys, mapping relationships


# ======= TYPE HINTING ========

my_ints: list[int] = [34, 0, 76, -57]
my_floats: list[float] = [1.00, 94.542349587, -23.123]
my_strings: list[str] = ["apple", "banana", "cherry", "Python"]
my_booleans: list[bool] = [True, False, True]

# Examples of when type hints are most helpful

# - dict[str, str | int]: a dictionary where the keys are strings, and the values can be either strings or integers.
user_data: dict[str, str | int] = {"name": name, "age": 25}

# - list[int | float]: a list where each element can be either an integer or a float.
mixed_numbers: list[int | float] = [1, 2.5, 3, 4.7]

# ========== COLLECTION DATA TYPES ==========

# 1. LIST - Ordered, mutable, allows duplicates
# - list[type]: elements can be of specified type
scores: list[int] = [85, 92, 78, 85]  # duplicates allowed
names: list[str] = ["Alice", "Bob", "Charlie"]
nested_list: list[list[int]] = [[1, 2], [3, 4], [5, 6]]

# 2. TUPLE - Ordered, immutable, allows duplicates
# - tuple[type, ...]: fixed types for each position
coordinates: tuple[int, int] = (10, 20)  # exactly 2 ints
person_info: tuple[str, int, bool] = ("Alice", 25, True)  # mixed types
flexible_tuple: tuple[int, ...] = (1, 2, 3, 4, 5)  # any number of ints

# 3. SET - Unordered, mutable, no duplicates
# - set[type]: unique elements of specified type
unique_numbers: set[int] = {1, 2, 3, 4, 5}  # duplicates automatically removed
unique_words: set[str] = {"apple", "banana", "cherry"}
empty_set: set[str] = set()  # empty set (not {} which is dict)

# 4. FROZENSET - Unordered, immutable, no duplicates
# - frozenset[type]: immutable version of set
frozen_numbers: frozenset[int] = frozenset([1, 2, 3, 4, 5])
frozen_words: frozenset[str] = frozenset(["apple", "banana", "cherry"])

# 5. DICT - Key-value pairs, mutable, keys must be unique
# - dict[key_type, value_type]: specify types for keys and values
student_grades: dict[str, int] = {"Alice": 95, "Bob": 87, "Charlie": 92}
settings: dict[str, str | int | bool] = {"debug": True, "timeout": 30, "host": "localhost"}
nested_dict: dict[str, dict[str, int]] = {"user1": {"score": 100, "level": 5}}

# 6. ADVANCED COLLECTIONS (from collections module)
from collections import deque, defaultdict, Counter

# - deque[type]: double-ended queue, efficient at both ends
queue_numbers: deque[int] = deque([1, 2, 3, 4, 5])
queue_names: deque[str] = deque(["first", "second", "third"])

# - defaultdict[type]: dict with default values
word_count: defaultdict[int] = defaultdict(int)  # defaults to 0
grouped_data: defaultdict[list[str]] = defaultdict(list)  # defaults to empty list

# - Counter[type]: count occurrences
letter_counts: Counter[str] = Counter("hello world")
number_counts: Counter[int] = Counter([1, 2, 2, 3, 3, 3])

# ========== COMPLEX COMBINATIONS ==========

# Mixed collection types
game_data: dict[str, list[tuple[str, int]]] = {
    "player1": [("sword", 10), ("shield", 5)],
    "player2": [("bow", 15), ("arrow", 50)]
}

# Multiple union types
flexible_data: list[str | int | float | bool] = ["hello", 42, 3.14, True]

# Optional types (can be None)
maybe_scores: list[int | None] = [85, None, 92, None, 78]
optional_user: dict[str, str | int | None] = {"name": "Alice", "age": 25, "email": None}



# ======== FUNCTIONS ========

def average(numbers: list[float]) -> float:
    """Return the average of a list of numbers. Returns 0.0 if the list is empty."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def add_student_grade(grades: dict[str, int], name: str, grade: int) -> None:
    """Add or update a student's grade in the grades dictionary."""
    grades[name] = grade

def get_unique_words(words: list[str]) -> set[str]:
    """Return a set of unique words from a list."""
    return set(words)

def safe_get(dictionary: dict, key, default=None):
    """Safely get a value from a dictionary, returning default if key is missing."""
    return dictionary.get(key, default)

# ======== CLASSES ========

class Student:
    def __init__(self, name: str, grades: list[int] | None = None):
        self.name = name
        self.grades = grades if grades is not None else []

    def add_grade(self, grade: int) -> None:
        self.grades.append(grade)

    def average(self) -> float:
        return average(self.grades)

    def __repr__(self):
        return f"Student(name={self.name!r}, grades={self.grades!r})"

class Inventory:
    def __init__(self):
        self.items: dict[str, int] = {}

    def add_item(self, item: str, quantity: int = 1) -> None:
        self.items[item] = self.items.get(item, 0) + quantity

    def remove_item(self, item: str, quantity: int = 1) -> bool:
        if self.items.get(item, 0) >= quantity:
            self.items[item] -= quantity
            if self.items[item] == 0:
                del self.items[item]
            return True
        return False

    def total_items(self) -> int:
        return sum(self.items.values())

    def __repr__(self):
        return f"Inventory(items={self.items!r})"

# ======== METHODS (within classes above) ========

