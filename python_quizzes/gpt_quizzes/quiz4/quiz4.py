# Part 1.

def add_category(*categories):
    product_categories = [category for category in categories]
    return product_categories

categories_today = add_category("Electronics", "Furniture", "Toys")

# Part 2. 

def add_tuple(product_name, quantity_sold, sale_date):
    return (product_name, quantity_sold, sale_date)

added_tuple = add_tuple("Laptop", 5, "2025-01-04")


print(categories_today)
print(added_tuple)
