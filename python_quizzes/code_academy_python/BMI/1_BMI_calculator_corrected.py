"""
This script calculates the BMI based on user input for weight in pounds
and height in feet and inches. It categorizes the BMI according to health
standards from the World Health Organization (WHO) and the Centers for Disease
Control and Prevention (CDC).
"""

# Function to calculate BMI
def bmi_calculator():
    """
    Calculates BMI based on user-provided weight and height.
    Returns the BMI as a float.
    """
    # Input for weight in pounds
    weight = float(input("What is your weight in lbs?: "))

    # Input for height in feet and inches with error handling
    try:
        height_input = input("What is your height? (format: feet inches): ")
        
        # Convert input string to two integers for feet and inches
        feet, inches = map(int, height_input.split())
        
        # Calculate total height in inches
        converted_height = float(feet * 12) + float(inches)
        
    except ValueError:
        # Handle invalid input format
        print("Please enter height as feet inches, e.g., '5 10'")
        return None  # Exit function if input format is incorrect
    
    # Calculate BMI using the formula for the Imperial system
    bmi = (weight * 703) / (converted_height ** 2)
    return bmi

# Calculate BMI
bmi_value = bmi_calculator()
if bmi_value is not None:
    print(f"\nYour BMI is {bmi_value:.2f}\n")

    # Function to categorize BMI based on WHO standards
    def who_verification(bmi_value):
        """
        Determines the BMI category according to WHO standards.
        Returns a string describing the weight category.
        """
        if bmi_value < 18.5:
            return "underweight"
        elif 18.5 <= bmi_value < 25.0:
            return "normal weight"
        elif 25.0 <= bmi_value < 30.0:
            return "overweight"
        else:
            return "obese"

    # Function to categorize BMI based on CDC standards
    def cdc_verification(bmi_value):
        """
        Determines the BMI category according to CDC standards.
        Returns a string describing the weight category.
        """
        if bmi_value < 18.5:
            return "underweight"
        elif 18.5 <= bmi_value < 24.9:
            return "normal weight"
        elif 25.0 <= bmi_value < 29.9:
            return "overweight"
        else:
            return "obese"

    # Output health categories according to WHO and CDC
    print(f"According to the WHO, you are categorized as: {who_verification(bmi_value)}")
    print(f"According to the CDC, you are categorized as: {cdc_verification(bmi_value)}\n")
else:
    print("No BMI calculated due to input error.")