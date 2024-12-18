# 23. The Calculator Project 

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+":add,
    "-":substract,
    "*":multiply,
    "/":divide,
}

def calculator():
    should_accumulate = True
    num1 = float(input("What Is The First Number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick An Operation: ")
        num2 = float(input("What Is The Next Number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' To The Calculate With {answer}, or Type 'n' To Start a New Calculation.")


        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()

# ---------------------------------------------------------------------------------------------------------