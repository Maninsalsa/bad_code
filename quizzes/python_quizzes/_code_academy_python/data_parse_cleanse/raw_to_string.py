raw_data = """
    Hello, world!   This is a test. 
    Some lines have extra spaces.     
    Others, have punctuation! 
    And some have inconsistent spacing. 
    \n
    Let's see how well the script can clean this up.    
    """

def strip_and_filter(strings):
    """Strip whitespace and filter out empty strings from a list."""
    return [s.strip() for s in strings if s.strip()]

def strip_specific_indices(strings, indices=None):
    """Strip whitespace from specific indices in a list."""
    if indices is None:
        return strings
    
    stripped_list = strings.copy()
    for index in indices:
        if 0 <= index < len(stripped_list):
            stripped_list[index] = stripped_list[index].strip()
    return stripped_list

def interactive_edit(strings):
    """Interactively edit a list of strings by stripping whitespace."""
    edited_list = strip_and_filter(strings)
    
    while True:
        for i, item in enumerate(edited_list):
            print(f"{i}: {item}")
        
        indices_to_edit = input("Enter indices to edit (comma-separated) or 'done' to finish: ")
        if indices_to_edit.lower() == 'done':
            break
            
        try:
            indices = [int(i.strip()) for i in indices_to_edit.split(',')]
            edit_elements = [edited_list.pop(idx) for idx in sorted(indices, reverse=True) 
                           if 0 <= idx < len(edited_list)]
            
            while True:
                print("\nCurrent elements:")
                for i, elem in enumerate(edit_elements):
                    print(f"{i}: {elem}")
                
                strip_again = input("\nStrip these elements again? (y/n): ").lower()
                if strip_again != 'y':
                    break
                    
                edit_elements = strip_specific_indices(edit_elements)
            
            insert_idx = int(input("Enter index where to insert edited elements: "))
            for element in edit_elements:
                edited_list.insert(insert_idx, element)
                insert_idx += 1
                
        except ValueError:
            print("Invalid input. Please enter valid indices.")
            continue
            
    return edited_list

def joiner(lst, indices=None):
    """Join list elements into a string, with optional specific delimiters at given indices."""
    delimiters = {
        "space": " ",
        "newline": "\n", 
        "comma": ",",
        "period": ".",
        "semicolon": ";",
        "colon": ":",
        "hyphen": "-",
        "underscore": "_",
        "pipe": "|",
        "slash": "/"
    }

    if not indices:
        return ' '.join(lst)  # Use space as the default delimiter

    result = []
    for i, item in enumerate(lst):
        result.append(item)
        if i in indices:
            delimiter_type = indices[i]
            delimiter = delimiters.get(delimiter_type, '')
            result.append(delimiter)
            
    return ''.join(result)

def main(raw_data):
    """Process raw data through cleaning, optional editing, and joining steps."""

    # Convert raw_data to a list of strings
    raw_data_lines = raw_data.splitlines()

    # Step 1: Strip and filter the list
    cleaned_lines = strip_and_filter(raw_data_lines)
    
    # Step 2: Optionally interactively edit the list
    edited_lines = interactive_edit(cleaned_lines)
    
    # Step 3: Join the list into a single string
    # Join with a space by default
    final_string = joiner(edited_lines, indices=None)
    
    # Output the final result
    print("Final cleaned and formatted string:")
    print(final_string)

if __name__ == "__main__":
    main(raw_data)