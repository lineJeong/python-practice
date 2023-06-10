from auction_art import logo
import os

print(logo)
print("Welcome to the secret auction program.")

bids = {} # {"first": 10, "second": 5}
bidding_continue = True


def get_winner(bidding_record):
    winner = ""
    highest_bid = 0
    for name in bidding_record:
        current_bid = bidding_record[name]
        if highest_bid < current_bid:
            winner = name
            highest_bid = current_bid

    print(f"The winner is {winner} with a bid of ${highest_bid}")


while bidding_continue == True:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))

    bids[name] = price

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if other_bidders == "no":
        bidding_continue = False
        get_winner(bidding_record=bids)
    else:
        os.system('clear')  # mac에서 python console 지우기
