from random import randrange as rando

# Target = 9
nums = [2,7,11,15]

def two_sum(list):
    target = 0
    compatible_indexes = []
    for index, value in enumerate(list):
        if target != 9:
            target += value
            compatible_indexes.append(index)
        else:
            return f"Output : {compatible_indexes} // nums[{compatible_indexes[0]}] + nums[{compatible_indexes[1]}] = {list[compatible_indexes[0]]} + {list[compatible_indexes[1]]} = {target}"
        

answer = two_sum(nums)
# Output: [0, 1]  // nums[0] + nums[1] = 2 + 7 = 9
print(answer) 

# Improved design

def two_sum(nums, target):
    # Dictionary to store the value and its index
    seen = {}
    for index, value in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - value
        if complement in seen:
            # Found the pair
            return [seen[complement], index]  # Return indices of the pair
        # Store the current value and its index
        seen[value] = index
    return None  # If no solution exists

# alternate version with matrix generator



def rando_list_gen(number: int = rando(1,100)) -> list:
    randomly_generated = []
    print("\n=== Generating Random List ===")
    print(f"Generating {number} random numbers...")
    for _ in range(number):
        randomly_generated.append(rando(1,100))
    print(f"Generated list: {randomly_generated}")
    return randomly_generated

# first = rando_list_gen(5)
# answer = two_sum()
# print(answer)

def two_sum() -> str:
    print("\n=== Two Sum Problem ===")
    # generate a random number
    target = rando(1,100)
    random_list = rando_list_gen()
    print(f"\nTarget to hit: {target}")
    print(f"Initial random list: {random_list}")
 
    iteration = 1
    while True:
        print(f"\n--- Iteration {iteration} ---")
        print("Checking all combinations...")
        # Check all combinations of numbers in current list
        for i in range(len(random_list)):
            for j in range(i + 1, len(random_list)):
                print(f"Checking index {i}:{random_list[i]} + index {j}:{random_list[j]}")
                if random_list[i] + random_list[j] == target:
                    return f"\nSolution found!\nIndices {i} and {j} with value {random_list[i]} and {random_list[j]} = target number: {target}"
        
        # If no match found, generate more numbers and add to list
        print("\nNo matches found in current list...")
        new_numbers = rando_list_gen()
        random_list.extend(new_numbers)
        print(f"Added new numbers to the list")
        print(f"Updated list: {random_list}")
        iteration += 1

def two_sum_fixed(nums: list, target: int) -> str:
    """
    Find two numbers in the list that add up to target
    Returns a formatted string showing the solution, or None if no solution exists
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return f"Output: [{i}, {j}]  // nums[{i}] + nums[{j}] = {nums[i]} + {nums[j]} = {target}"
    return None