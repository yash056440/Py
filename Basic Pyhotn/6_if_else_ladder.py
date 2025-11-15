'''
    write a program to findout person obesity level using BMI(body to mass index) technique.
    ---------------------------------------------------------------------
    formula to calculate BMI IS 
    bmi = weight(Kg ) / (height_in_meter * height_in_meter)
    obesity level 
        Underweight: BMI less than 18.5
        Normal: BMI between 18.5 to 24.9
        Overweight: BMI between 25.0  29.9
        Obese: BMI between 30.0  34.9
        Extremely Obese: BMI 35.0 and above
    input:
        weight, foot, inch 
    steps 
    1   accept input weight, foot, inch
    2   convert foot and inches into meter 
    3   calculate BMI 
    4   calculate & display person obesity level
'''
"""
Improved BMI calculator with correct conversion and classification.

Inputs: weight (kg), height (feet and inches)
Conversion: 1 inch = 0.0254 meters
Classification ranges (standard simplified):
    Underweight: BMI < 18.5
    Normal:      18.5 <= BMI < 25.0
    Overweight:  25.0 <= BMI < 30.0
    Obese:       30.0 <= BMI < 35.0
    Extremely Obese: BMI >= 35.0

This script validates inputs and prints BMI formatted to 2 decimals.
"""

def read_positive_float(prompt):
    val = float(input(prompt).strip())
    if val <= 0:
        raise ValueError("Value must be positive")
    return val


def read_nonnegative_int(prompt):
    val = int(input(prompt).strip())
    if val < 0:
        raise ValueError("Value must be non-negative")
    return val


def main():
    try:
        weight = read_positive_float("Enter your weight in kilograms (kg): ")
        print("Enter your height:")
        foot = read_nonnegative_int("  Feet: ")
        inch = read_nonnegative_int("  Inches: ")
    except ValueError as e:
        print("Invalid input:", e)
        return

    # convert total height to meters (1 inch = 0.0254 m)
    total_inches = (foot * 12) + inch
    meter = total_inches * 0.0254

    if meter <= 0:
        print("Invalid height: height must be greater than zero")
        return

    # calculate BMI
    bmi = weight / (meter * meter)

    # display BMI with 2 decimals
    print(f"BMI: {bmi:.2f}")

    # classification
    if bmi < 18.5:
        classification = "Underweight"
    elif bmi < 25.0:
        classification = "Normal"
    elif bmi < 30.0:
        classification = "Overweight"
    elif bmi < 35.0:
        classification = "Obese"
    else:
        classification = "Extremely Obese"

    print(f"Classification: {classification}")


if __name__ == "__main__":
    main()