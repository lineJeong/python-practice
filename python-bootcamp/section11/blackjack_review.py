import random
import os
from blackjack_art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    # 11(ace) + 10
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare_score(player_score, computer_score):
    if player_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose"
    elif player_score == 0:
        return "You win"
    elif player_score > 21:
        return "You lose"
    elif computer_score > 21:
        return "You win"
    elif player_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():

    print(logo)

    player_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    while not is_game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        # Error: blackjack일 때 play_score = 0
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        

        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            player_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if player_should_deal == 'y':
                player_cards.append(deal_card())
            else:
                is_game_over = True
    
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_score(player_score, computer_score))

    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        os.system('clear')
        play_game()


play_game()