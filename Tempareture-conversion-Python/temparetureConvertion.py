unit = input("Is this a temperature in Fahrenheit or Celsius? (C/F): ")
temp = float(input("Please enter the temperature: "))

if unit.upper() == "C":
    converted_temp = (temp * 9/5) + 32
    print(f"{temp}°C is equal to {converted_temp}°F")
elif unit.upper() == "F":
    converted_temp = (temp - 32) * 5/9
    print(f"{temp}°F is equal to {round(converted_temp, 2)}°C")
else:
    print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
