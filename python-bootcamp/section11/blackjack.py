# 카드의 합이 21을 초과하면 짐
# J,Q,K == 10
# A == 1 or A == 11
# 딜러의 카드의 합이 17미만이면 다른 카드를 받음

import random
import os
from blackjack_art import logo


def get_random_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        ace_index = cards.index(11)
        cards[ace_index] = 1
    return sum(cards)


def compare_score(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose."

    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Computer has a Blackjack. You lose."
    elif user_score == 0:
        return "You have a Blackjack. You win."
    elif user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Computer went over. You win."
    elif user_score > computer_score:
        return "You win."
    else:
        return "You lose."


def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    while len(user_cards) < 2 and len(computer_cards) < 2:
        user_cards.append(get_random_card())
        computer_cards.append(get_random_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}",)
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score >= 21:
            is_game_over = True
        else:
            if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
                user_cards.append(get_random_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(get_random_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(
        f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_score(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('clear')
    play_game()
