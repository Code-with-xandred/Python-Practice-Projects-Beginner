#4. Python Compund Interset Calculator

principle = 0
rate = 0
time = 0

while principle <0:
    principle = float(input("Enter The Principle amount: "))
    if principle <0:
        print("Principle Can't Be Less Than Or Equal To Zero")

while rate <0:
    rate = float(input("Enter The interest rate: "))
    if rate <0:
        print(" interest rate Can't Be Less Than Or Equal To Zero")
    
while time <0:
    time = int(input("Enter The time in years: "))
    if time <0:
        print("Time Can't Be Less Than Or Equal To Zero")

total = principle * pow(1 + rate / 100, time)
print(f"Balance after {time} years/s: ${total:.2f}")

# ________________________________________________________________________________________________

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter The Principle amount: "))
    if principle < 0:
        print("Principle Can't Be Less Than Zero")
    else:
        break

while True:
    rate = float(input("Enter The Interest Rate: "))
    if rate < 0:
        print("Principle Can't Be Less Than Zero")
    else:
        break

while True:
    time = int(input("Enter The Time In Years: "))
    if time < 0:
        print("Time Can't be Less Than Zero")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} years/s: ${total:.2f}")