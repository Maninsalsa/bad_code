import os

class Calculator:
    def __init__(self):
        self.current_input = ""
        self.stored_number = None
        self.current_operator = None
        self.history = []

    def handle_operator(self, operator):
        if self.current_input:
            if self.stored_number is None:
                self.stored_number = float(self.current_input)
            else:
                self.calculate()
            self.current_operator = operator
            self.current_input = ""

    def calculate(self):
        if self.stored_number and self.current_input and self.current_operator:
            num1 = self.stored_number
            num2 = float(self.current_input)
            
            operations = {
                '+': lambda x, y: x + y,
                '-': lambda x, y: x - y,
                '*': lambda x, y: x * y,
                '/': lambda x, y: x / y if y != 0 else 'Error'
            }
            
            result = operations[self.current_operator](num1, num2)
            self.history.append(f"{num1} {self.current_operator} {num2} = {result}")
            self.stored_number = result
            return result

    def display_screen(self):
        os.system('clear')  # Mac uses 'clear' instead of 'cls'
        print("Calculator (press 'q' to quit)")
        print("=" * 30)
        
        # Show history
        for entry in self.history[-3:]:
            print(entry)
        print("=" * 30)
        
        # Show current calculation
        if self.stored_number is not None:
            print(f"{self.stored_number} {self.current_operator} {self.current_input}")
        else:
            print(self.current_input or "0")

