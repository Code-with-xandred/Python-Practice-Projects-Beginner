# 17. Pizza Order Practice

print("Welcome To Python Pizza Deliveries!")
Size = input("What Size Pizza Do You Want? S, M Or L:- ")
Pepperoni = input("Do You Want Pepproni On Your Pizza? Y Or N:- ")
Extra_Cheese = input("Do You Want Extra Cheese? Y Or N:- ")

Bill = 0
if Size == "S":
    Bill += 15
elif Size == "M":
    Bill += 20
elif Size == "L":
    Bill += 25
else:
    print("You Typed The Wrong Inputs.")
# -------------------------------------------------------------

if Pepperoni == "Y":
    if Size == "S":
        Bill += 2
    else:
        Bill += 3

# -----------------------------------------------------------------

if Extra_Cheese == "Y":
    Bill += 1

print(f"Your Final Bill Is: ${Bill}.")

