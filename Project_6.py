#6.Shopping Cart Programme

foods = []
prices = []
total = 0

while True:
    food = input("Enter a Food To Buy (q To Quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter The Price Of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("------ YOUR CART -----")
for food in foods:
    print(food, end=" ")

for price in prices:
    total += price


print()
print(f"Your Total Is: ${total}")

# ___________________________________________________________________________________


