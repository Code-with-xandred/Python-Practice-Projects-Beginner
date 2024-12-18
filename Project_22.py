# 21. The Secret Auction Programme

def find_highest_bidder(biding_dictionary):
    winner = ""
    highest_bid = 0

    max(biding_dictionary)

    for bidder in biding_dictionary:
        bid_amount = biding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The Winner Is {winner} With a Bid Of ${highest_bid}")

bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What Is Your Name?: ")
    price = int(input("What Is Your Bid?: $"))
    bids[name] = price
    should_continue = input("Are There Any Other Bidders? Type 'Yes' Or 'No':-.\n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)

# -----------------------------------------------------------------------------------------