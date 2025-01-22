# ASCII letters made out of their letters.upper()
ascii_art_letters = {
    'A': [
        "  A   ",
        " A A  ",
        "A   A ",
        "AAAAA ",
        "A   A ",
        "A   A ",
        "A   A "
    ],
    'B': [
        "BBBB  ",
        "B   B ",
        "B   B ",
        "BBBB  ",
        "B   B ",
        "B   B ",
        "BBBB  "
    ],
    'C': [
        " CCC  ",
        "C   C ",
        "C     ",
        "C     ",
        "C     ",
        "C   C ",
        " CCC  "
    ],
    'D': [
        "DDDD  ",
        "D   D ",
        "D   D ",
        "D   D ",
        "D   D ",
        "D   D ",
        "DDDD  "
    ],
    'E': [
        "EEEEE ",
        "E     ",
        "E     ",
        "EEE   ",
        "E     ",
        "E     ",
        "EEEEE "
    ],
    'F': [
        "FFFFF ",
        "F     ",
        "F     ",
        "FFF   ",
        "F     ",
        "F     ",
        "F     "
    ],
    'G': [
        " GGG  ",
        "G   G ",
        "G     ",
        "G  GG ",
        "G   G ",
        "G   G ",
        " GGG  "
    ],
    'H': [
        "H   H ",
        "H   H ",
        "H   H ",
        "HHHHH ",
        "H   H ",
        "H   H ",
        "H   H "
    ],
    'I': [
        " III  ",
        "  I   ",
        "  I   ",
        "  I   ",
        "  I   ",
        "  I   ",
        " III  "
    ],
    'J': [
        "JJJJJ ",
        "    J ",
        "    J ",
        "    J ",
        "J   J ",
        "J   J ",
        " JJJ  "
    ],
    'K': [
        "K   K ",
        "K  K  ",
        "K K   ",
        "KK    ",
        "K K   ",
        "K  K  ",
        "K   K "
    ],
    'L': [
        "L     ",
        "L     ",
        "L     ",
        "L     ",
        "L     ",
        "L     ",
        "LLLLL "
    ],
    'M': [
        "M   M ",
        "MM MM ",
        "MM MM ",
        "M M M ",
        "M   M ",
        "M   M ",
        "M   M "
    ],
    'N': [
        "N   N ",
        "NN  N ",
        "NN  N ",
        "N N N ",
        "N  NN ",
        "N  NN ",
        "N   N "
    ],
    'O': [
        " OOO  ",
        "O   O ",
        "O   O ",
        "O   O ",
        "O   O ",
        "O   O ",
        " OOO  "
    ],
    'P': [
        "PPPP  ",
        "P   P ",
        "P   P ",
        "PPPP  ",
        "P     ",
        "P     ",
        "P     "
    ],
    'Q': [
        " QQQ  ",
        "Q   Q ",
        "Q   Q ",
        "Q   Q ",
        "Q  Q  ",
        "Q   Q ",
        " QQQ Q"
    ],
    'R': [
        "RRRR  ",
        "R   R ",
        "R   R ",
        "RRRR  ",
        "R R   ",
        "R  R  ",
        "R   R "
    ],
    'S': [
        " SSS  ",
        "S   S ",
        "S     ",
        " SSS  ",
        "    S ",
        "S   S ",
        " SSS  "
    ],
    'T': [
        "TTTTT ",
        "  T   ",
        "  T   ",
        "  T   ",
        "  T   ",
        "  T   ",
        "  T   "
    ],
    'U': [
        "U   U ",
        "U   U ",
        "U   U ",
        "U   U ",
        "U   U ",
        "U   U ",
        " UUU  "
    ],
    'V': [
        "V   V ",
        "V   V ",
        "V   V ",
        "V   V ",
        " V V  ",
        " V V  ",
        "  V   "
    ],
    'W': [
        "W   W ",
        "W   W ",
        "W   W ",
        "W W W ",
        "W W W ",
        "W W W ",
        " W W  "
    ],
    'X': [
        "X   X ",
        "X   X ",
        " X X  ",
        "  X   ",
        " X X  ",
        "X   X ",
        "X   X "
    ],
    'Y': [
        "Y   Y ",
        "Y   Y ",
        " Y Y  ",
        "  Y   ",
        "  Y   ",
        "  Y   ",
        "  Y   "
    ],
    'Z': [
        "ZZZZZ ",
        "    Z ",
        "   Z  ",
        "  Z   ",
        " Z    ",
        "Z     ",
        "ZZZZZ "
    ]
}

# make a function that prints these block letters by row
def block_printer(word): 
    for i in range(7):
        print(" ".join(ascii_art_letters[letter][i] for letter in word))