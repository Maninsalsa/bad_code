
"""
This script calculates the BMI based on user input for weight in pounds 
and height in feet and inches. put in a function?
"""


# input for height
def bmiCalculator():

    # Input for weight
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
        # converted_height = None  # Set to None to handle errors if needed later
        # print(f"{weight_input}\n{height_input}\n{converted_height}")

    bmi = (weight * 703) / converted_height ** 2

    # print(bmi)
    return bmi

bmi_value = bmiCalculator()
print(f"\nYour BMI is {bmi_value}\n")

# Part 4: Output the BMI in both health categories to the user

def whoVerification(bmi_value):
    
    who_verify = ""

    # assign variables for WHO
    if bmi_value < 18.5:
        who_verify = "under weight"

    elif bmi_value < 25.0 and bmi_value >= 18.5:
        who_verify = "normal weight"

    elif bmi_value >= 25.0 and bmi_value < 30.0:
        who_verify = "over weight"
        
    else:
        who_verify = "obese"

    return who_verify
   # assign CDC variables
def cdcVerification(bmi_value):
    
    cdc_verify = ""

    # assign variables for WHO
    if bmi_value < 18.5:
        cdc_verify = "under weight"

    elif bmi_value < 24.9 and bmi_value >= 18.5:
        cdc_verify = "normal weight"

    elif bmi_value >= 25.0 and bmi_value < 29.9:
        cdc_verify = "over weight"
        
    else:
        cdc_verify = "obese"

    return cdc_verify

print(f"according to the WHO organization, you have {whoVerification(bmi_value)}")
print(f"according to the CDC, you have {cdcVerification(bmi_value)}\n")



"""
Program Prompt: BMI and Health Category Calculator

Objective

Create a program that:
	1.	Asks for the user’s weight (in pounds) and height (in inches).
	2.	Calculates the BMI using the formula:

BMI = \frac{weight \times 703}{height^2}

	3.	Categorizes the BMI according to health standards from two organizations:
	•	WHO (World Health Organization):
	•	Underweight: BMI < 18.5
	•	Normal weight: 18.5 <= BMI < 25
	•	Overweight: 25 <= BMI < 30
	•	Obese: BMI >= 30

	•	CDC (Centers for Disease Control):
	•	Underweight: BMI < 18.5
	•	Healthy weight: 18.5 <= BMI < 24.9
	•	Overweight: 25 <= BMI < 29.9
	•	Obesity: BMI >= 30

	4.	Outputs the calculated BMI and the health categories for both WHO and CDC.

Breakdown for Applying Your Framework

1. Understand the Problem and Break It Down into Parts

	•	Part 1: Ask the user for weight and height.
	•	Part 2: Calculate BMI using the provided formula.
	•	Part 3: Compare the BMI against the WHO and CDC standards.
	•	Part 4: Output the BMI and both health categories to the user.
"""

