# 11. Slot Machine Programme

import random
def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("-------------------------")
    print(" | ".join(row))
    print("-------------------------")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    else:
        return 0

def main():
    balance = 100
    print("-------------------------")
    print("Welcome To Python Slots ")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("-------------------------")

    while balance > 0:
        print(f"Current Balance: ${balance}")

        bet = input("Place your Bet Amount: ")

        if not bet.isdigit():
            print("Please Enter a Valid Amount")
            continue
        bet = int(bet)

        if bet > balance:
            print("Insufficient Funds")
            continue

        if bet <= 0:
            print("Bet Must Be Must Be Greater Than 0")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You Want ${payout}")
        else:
            print("Sorry Lost This Round")
        
        balance += payout

        play_again = input("Do You Want To Spin Again? (Y/N): ").upper()
        if play_again != "Y":
            break
    print("-------------------------")
    print(f"Game Over! Your Final Balance Is ${balance}")
    print("-------------------------")

if __name__ == '__main__':
    main()

