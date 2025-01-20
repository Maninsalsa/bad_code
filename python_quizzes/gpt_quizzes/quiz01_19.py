# sum of even Numbers

"""
Question 1
# define a function that takes a list as a parameter:
    # create a container that captures all even numbers
    # use a forloop to iterate each number on the list:
        # modulo conditional to ID numbers with a 0 remainder:
            add to container
    return the sum of all numbers within the even number container

call the function and contain it's return value in a variable

print the answer in terminal
"""
# 1. Answer
def sum_of_even_numbers(numberlist: list) -> int:
    return [i for i in numberlist if i % 2 ==0]


"""
Question 2

define a function that takes (an iterable string, the target string) and returns an integer:

    return  iterablestring.lower().count(target string) methods to make all strings the same case, then count all instances of the target word
    
"""

# 2. Answer
def how_many_times(stringofwords: str, targetword: str) -> int:
    return stringofwords.lower().count(targetword)

"""
Question 3

'string reversed' is kind of ambigiuous so here's 2 answers

define a func that (input string) -> str:
    return reversed(input string) (instead of .reverse() since it's not a list)

or

define a func that (input string) -> str:
    define what a words are by splitting the 'words' by the space character using .split() which uses empty space as the delimiter and creates a list of strings.
    define reversed words that join the list of words into a string in reverse order
    return the reversed words

"""

def reverse_string(sentence: str) -> str:
    return reversed(sentence)
    #corrected should be return ' '.join(reversed(sentence) this is because reversed is an iterator, not a string. 

# or

def reverse_sentence(sentence: str) -> str:
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

"""
Question 4

define a function that iterates through all characters in a string and returns a boolean:
    split the string into words using .split()

    outer loop to iterate through each word:
        create a set for all seen characters
        inner loop to iterate through all characters in the string:
            if the current character is found again within any of the words:
                return False
    return True
"""

def all_unique(input_string: str) -> bool:
    list_of_words = input_string.split()
    
    for words in list_of_words:
        checked_characters = set() # use a set that automatically excludes duplicates
        for chars in words:
            if chars in checked_characters:
                return False
    return True

"""
Question 5

define a function, takes a list of ints and returns an int:
    # trying to build good habits here
    conditional to check if the list is empty:
        return None or raise an exception

    initialize the largest number variable and set it to 0:
    access each numnber in list:
        if the current number is > the largest number:
            set the largest number to the current number
    return the largest number
"""

def largest_number(list_of_numbers: list) -> int:
    if list_of_numbers == []:
        return None
    
    largest_number = 0
    for number in list_of_numbers:
        if number > largest_number:
            largest_number = number
    return largest_number        


"""
Bonus  #### No Points =[

define a function that takes *sorted_lists and returns a combined sorted list:
    take the two lists and create a new list that takes all the elements and sorts them

Define a function that takes two sorted lists:

    Create an empty list to store the merged result.

    Use two pointers, one for each list.
    While neither pointer has reached the end of its list:
        Compare the current elements at each pointer.
        Append the smaller element to the result list.
        Move the pointer for the smaller element forward.

    If one list still has elements, append them to the result.+

    Return the merged list.

"""

def merge_sorted_lists(list1: list, list2: list) -> list:
    """Merges two sorted lists into a single sorted list."""
    merged = [] #Create an empty list to store the merged result.
    i, j = 0, 0  # Pointers for list1 and list2

    # Merge elements until one of the lists is exhausted
    while i < len(list1) and j < len(list2): # While neither pointer has reached the end of its list:
        if list1[i] < list2[j]: # Compare the current elements at each pointer.
            merged.append(list1[i]) # Append the smaller element to the result list.
            i += 1 # Move the pointer for the smaller element forward.
        else: # If one list still has elements, append them to the result.+
            merged.append(list2[j])
            j += 1

    # Append any remaining elements from list1 or list2
    merged.extend(list1[i:])
    merged.extend(list2[j:])

    return merged

# Example Usage
list1 = [1, 3, 5]
list2 = [2, 4, 6]
result = merge_sorted_lists(list1, list2)
print(result)  # Output: [1, 2, 3, 4, 5, 6]