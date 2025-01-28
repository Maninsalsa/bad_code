def block_printer(word: str) -> str:
    ascii_art = []
    
    # iterate through string argument
    for char in word:
        if char == ascii_art_letters[char]:
            ascii_art.append(ascii_art_letters[char])
    return ascii_art