# bmi_calculator.py

def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Sample usage
weight = 70  # kg
height = 1.75  # meters
print("Your BMI is:", calculate_bmi(weight, height))
