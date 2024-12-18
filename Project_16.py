# 16. Tip Calculator

print("Welcome To The Tip Calculator!")
Bill = float(input("What Was The Total Bill? $:- "))
Tip = int(input("What Percentage Tip Would You Like To Give? 10 12 15:- "))
People = int(input("How Many People To Split The Bill?:- "))

Tip_As_Percentage = Tip / 100
Total_Tip_Amount = Bill * Tip_As_Percentage
Total_Bill = Bill + Total_Tip_Amount
Bill_Per_Person = Total_Bill / People
Final_Amount = round(Bill_Per_Person, 2)
print(f"Each Person Should Pay: ${Final_Amount}")
