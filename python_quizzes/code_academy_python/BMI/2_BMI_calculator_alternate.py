"""
This script calculates the BMI based on user input for weight in pounds
and height in feet and inches. It categorizes the BMI according to health
standards from the World Health Organization (WHO) and the Centers for Disease
Control and Prevention (CDC).
"""

# Health standard thresholds for BMI categories
WHO_THRESHOLDS = {
    "underweight": (None, 18.5),
    "normal weight": (18.5, 25.0),
    "overweight": (25.0, 30.0),
    "obese": (30.0, None)
}

CDC_THRESHOLDS = {
    "underweight": (None, 18.5),
    "normal weight": (18.5, 24.9),
    "overweight": (25.0, 29.9),
    "obese": (30.0, None)
}

def get_weight():
    """Prompts user for weight and returns it as a float."""
    while True:
        try:
            return float(input("What is your weight in lbs?: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value for weight.")

def get_height():
    """Prompts user for height in feet and inches, returns total inches."""
    while True:
        try:
            height_input = input("What is your height? (format: feet inches): ")
            feet, inches = map(int, height_input.split())
            return feet * 12 + inches  # Total height in inches
        except ValueError:
            print("Invalid format. Please enter height as feet inches (e.g., '5 10').")

def calculate_bmi(weight, height_in_inches):
    """Calculates BMI based on weight in pounds and height in inches."""
    return (weight * 703) / (height_in_inches ** 2)

def categorize_bmi(bmi, thresholds):
    """
    Categorizes BMI based on provided thresholds.
    `thresholds` should be a dictionary where keys are category names
    and values are (min, max) tuples for BMI ranges.
    """
    for category, (min_bmi, max_bmi) in thresholds.items():
        if (min_bmi is None or bmi >= min_bmi) and (max_bmi is None or bmi < max_bmi):
            return category
    return "Unknown category"  # Fallback, should not occur with proper thresholds

# Main program flow
weight = get_weight()
height_in_inches = get_height()
bmi_value = calculate_bmi(weight, height_in_inches)

print(f"\nYour BMI is {bmi_value:.2f}")

# Display BMI categories according to WHO and CDC
print(f"According to the WHO, you are categorized as: {categorize_bmi(bmi_value, WHO_THRESHOLDS)}")
print(f"According to the CDC, you are categorized as: {categorize_bmi(bmi_value, CDC_THRESHOLDS)}\n")