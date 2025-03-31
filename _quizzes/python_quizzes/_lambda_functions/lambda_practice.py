grade_list = [3.5, 3.7, 2.6, 95, 87]

# Create a lambda function that converts grades
# If grade < 5, assume it's a 4.0 scale (multiply by 25)
# Otherwise, keep it as is (already on 100 scale)
convert_grade = lambda grade: grade * 25 if grade < 5 else grade

# Use map() to apply the lambda function to all grades
convert_list = list(map(convert_grade, grade_list))

print(f"Original grade_list: {grade_list}\nConverted grade list:{convert_list}")