weight = input("Please enter your weight: ")
unit = input("Please enter the unit (K for kilograms, L for pounds): ")

if unit.upper() == 'K':
    weight = float(weight) * 2.20462
    unit = "lbs."
    print(f"Your weight is: {round(weight, 1)} {unit}")
elif unit.upper() == 'L':
    weight = float(weight) / 2.20462
    unit = "kgs."
    print(f"Your weight is: {round(weight, 1)} {unit}")
else:
    print("Invalid unit. Please enter 'K' for kilograms or 'L' for pounds.")
