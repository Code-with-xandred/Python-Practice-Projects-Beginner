#13.Python Resturent Programme


menu = {
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'Coffee':80
}

print("Welcome To The Python Resturent")
print("Pizza: Rs40\nPasta: Rs50\nBurger: Rs60\nSalad: Rs70\nCoffee: Rs80")

order_total = 0

item_1 = input("Enter The Name Of Item You Want To Order:- ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your Item {item_1} Has Been Added To Your Order")

else:
    print(f"Orderd Item {item_1} Is Not Avaialable Yet!")

another_order = input("Do You Want To Add Another Item? (Yes/No): ")
if another_order == "Yes":
    item_2 = input("Enter The Name Of Second Item:- ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} Has Been Added To Order")
    else:
        print(f"Orderd Item {item_2} Is Not Avaialable!")

print(f"The Total Amount Of Items To Pay Is {order_total}")