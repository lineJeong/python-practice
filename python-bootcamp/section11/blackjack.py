# 카드의 합이 21을 초과하면 짐
# J,Q,K == 10
# A == 1 or A == 11
# 딜러의 카드의 합이 17미만이면 다른 카드를 받음

from blackjack_art import logo

input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

print(logo)
print(f"Your cards: , current score: ",)
print(f"Computer's first card: ")
input("Type 'y' to get another card, type 'n' to pass: ")
print(f"Your final hand: , final score: ")
print(f"Computer's final hand: , final score: ")
print("You went over. You lose.")

input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
