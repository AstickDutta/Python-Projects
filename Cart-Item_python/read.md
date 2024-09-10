Explanation of the Code:
# Variables:

# foods = []: Initializes an empty list to store the names of the food items the user enters.
# prices = []: Initializes an empty list to store the prices of the food items.
# total = 0: This variable is used to store the cumulative total price of all the items.
# While Loop:

# The loop runs continuously to allow the user to enter food items and their prices until the user decides to quit by entering 'q'.
# Inside the loop:
# food = input(f"Please enter the food to buy (q for quit): "): The program prompts the user to enter a food item. If the user types 'q', the loop breaks and the program moves on to display the cart.
# price = float(input(f"Please enter the price of {food}: ")): If the user enters a valid food item, the program asks for its price and converts the input into a floating-point number using float().
# The entered food and price are added to the foods and prices lists respectively using foods.append(food) and prices.append(price).
# Displaying the Cart:

# After the user quits the loop, the program prints a separator "----------Cart---------------" to indicate the start of the cart display.
# for food in foods: print(food): Loops through the foods list and prints each food item added to the cart.
# Total Calculation:

# total = sum(prices): The total price is calculated by summing up all the values in the prices list using Python's built-in sum() function.
# print(f"Your total price is: INR {total:.2f}"): The total price is printed in a formatted way. The :.2f ensures that the total price is rounded to 2 decimal places.
