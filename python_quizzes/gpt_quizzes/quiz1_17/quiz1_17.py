"""
Write a Python class ShoppingCart that allows a user to:
	1.	Add items to the cart with their names and prices.
	2.	Remove items from the cart by their names.
	3.	Calculate the total price of all items in the cart.
	4.	List all the items currently in the cart.
"""

sample_items = {
    "apple": 1.00,       # $1.00 per apple
    "banana": 0.50,      # $0.50 per banana
    "chocolate": 2.00,   # $2.00 per chocolate bar
    "milk": 3.50,        # $3.50 per bottle of milk
    "bread": 2.50        # $2.50 per loaf of bread
}

class ShoppingCart:

    def __init__(self):
        self.items = []
        self.item_price = 0
        self.total_price = float(0.0)

    def add_item(self, item_name: str, price: float):
        # adds an item from a dictionary or file into the cart object
        
    def remove_item(self, name: str):
        # removes an item from the 
        pass

