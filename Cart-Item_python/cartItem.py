foods = []
prices = []
total = 0

while True:
    food = input(f"Please enter the food to buy (q for quit): ")
    if food.lower() == 'q':
        break
    price = float(input(f"Please enter the price of {food}: "))
    foods.append(food)
    prices.append(price)

print("----------Cart---------------")

for food in foods:
    print(food)

total = sum(prices)
print(f"Your total price is: INR {total:.2f}")