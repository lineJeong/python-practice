from auction_art import logo
import os

print(logo)
print("Welcome to the secret auction program.")

bidding_list = [] # [{"name": "first", "bid": 10}, {"name": "second", "bid": 5}]
bidding_continue = True


def make_bidding_list(name, bid, bidding_list):
    bidder = {
        "name": name,
        "bid": bid
    }
    bidding_list.append(bidder)


def get_winner(bidding_list):
    highest_bid = 0
    winner = ""
    for bidder in bidding_list:
        current_name = bidder["name"]
        current_bid = bidder["bid"]
        if highest_bid < current_bid:
            highest_bid = current_bid
            winner = current_name
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while bidding_continue == True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    make_bidding_list(name, bid, bidding_list)

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if other_bidders == "no":
        bidding_continue = False
        get_winner(bidding_list)
    else:
        os.system('clear')  # mac에서 python console 지우기
