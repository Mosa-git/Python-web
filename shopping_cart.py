
# Create a shopping cart programme that will continuously ask the user for a food product and the price of that product
# Have an exit clause if the user wishes to stop adding more things on their cart
# At the end show the food items an the total cost to the user

foods = []
prices = []

while True:
    food = input("Enter a food to buy or press q to quit: ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of the {food}: R"))
        foods.append(food)
        prices.append(price)
        
print("----- YOUR CART -----")
  
for food, price in zip(foods, prices):
    print(f"{food}: R{price}")

total = 0
for price in prices:
    total += price

print(f"Your total is: R{total}")