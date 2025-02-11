from calculator import Calculator
from getch import getch



def main():
    calc = Calculator()
    
    while True:
        calc.display_screen()
        char = getch()
        
        if char.lower() == 'q':
            break
        elif char.isdigit():
            calc.current_input += char
        elif char in "+-*/":
            calc.handle_operator(char)
        elif char in ['\r', '\n']:  # Enter key
            if calc.current_input and calc.stored_number and calc.current_operator:
                calc.calculate()
                calc.current_input = ""
        elif char == 'c':  # Clear
            calc.current_input = ""
            calc.stored_number = None
            calc.current_operator = None

if __name__ == "__main__":
    main()