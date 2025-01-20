# Write a function that takes a 2D matrix (list of lists) as input and returns a list of its elements in spiral order.
# expected_output = [1, 2, 3, 6, 9, 8, 7, 4, 5]

# Input

input_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def return_spiral_list(matrix: list) -> list:
    spiral_order = []
    # first spiral piece
    spiral_order = [value for value in matrix[0]]
    # modular definition of the next piece
    # iterate through the last column starting at the second index (matrix[1])
    # Set index to last column (2) since we want the rightmost values
    column_index = 2
    # Get all values from the last column, starting from second row (matrix[1:])
    # This creates a list of values [6,9] from the rightmost column
    column = [row[column_index] for row in matrix[1:]]
    # Add each value from the column list to our spiral_order result
    for value in column:
        spiral_order.append(value)
    last_index = (len(matrix) - 1)
    for value in reverse_sublist[:-1]:
        spiral_order.app
    return spiral_order

# second spiral piece = 
    # print the last value of each sub_list from top to bottom
# third spiral piece = 
    # print all elements of the last sublist from the left of the last element in that list
    # in reverse order


sample = return_spiral_list(input_matrix)
print(sample)

# fundies_01_11._25.py