# Description:
# This program is designed to calculate the final balance after a specified number of years, based on compound interest. It prompts the user for input values of principle amount, annual interest rate, and time in years, while ensuring that all inputs are non-negative. The program uses validation checks within while loops to continuously request valid inputs from the user. Once the inputs are validated, it calculates the final balance using the compound interest formula and prints the result.

# Key Steps:
# Variable Initialization:

# principle, rate, and time are initialized to 0 to store user input values.
# Input Principle Amount with Validation:

# The user is prompted to input the principle amount.
# If the input is a negative number, an error message is displayed, and the loop repeats until a valid (non-negative) value is entered.
# Input Annual Interest Rate with Validation:

# The user is asked to input the annual interest rate as a percentage.
# If a negative value is entered, the user is prompted to re-enter until a valid input is provided.
# Input Time in Years with Validation:

# The program prompts the user to input the time duration in years.
# A negative time value is invalid, so the loop continues until the user provides a non-negative value.

# The final balance after applying compound interest is displayed in INR (Indian Rupees), rounded to two decimal places.