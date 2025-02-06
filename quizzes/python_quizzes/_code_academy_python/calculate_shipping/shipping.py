import random

# Generate and round weight based on user input
weight = round(float(input("Package weight (lbs)?: ")), 2)

def calc_shipping(package_weight):
    """
    Calculates the shipping cost based on package weight.
    
    Args:
        package_weight (float): The weight of the package in pounds.
        
    Returns:
        tuple: A tuple containing the total cost (float) and the price per pound (float).
    """
    price_perlb = 0
    match package_weight:
        case package_weight if package_weight <= 2.0:
            price_perlb = 4.50
        case package_weight if 2.0 < package_weight <= 6.0:
            price_perlb = 9.00
        case package_weight if 6.0 < package_weight <= 10.0:
            price_perlb = 12.00
        case package_weight if package_weight > 10.0:
            price_perlb = 14.25
    
    total_cost = round(package_weight * price_perlb, 2)
    return total_cost, price_perlb

def main():
    """
    Main program flow to calculate and print the shipping cost.
    """
    total_cost, price_perlb = calc_shipping(weight)
    print(f"Package weight: {weight} lbs")
    print(f"Price per pound: ${price_perlb}")
    print(f"Your total shipping cost: ${total_cost}")

# Execute the main function
if __name__ == "__main__":
    main()