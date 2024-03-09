import random
import os
from art import logo, vs
from data import data

def get_random_item():
    return random.choice(data)

def get_item_info(item):
    return f"{item['name']}, {item['description']}, from {item['country']}"

def compare_items(a_follwer, b_follwer):
    if a_follwer > b_follwer:
        return "A"
    elif a_follwer < b_follwer:
        return "B"

def play_game():
    score = 0
    is_game_over = False
    print(logo)

    item_b = get_random_item()

    while not is_game_over:
        item_a = item_b
        item_b = get_random_item()

        while item_a == item_b:
            item_b = get_random_item()

        print(f"Compare A: {get_item_info(item_a)}")
        print(vs)
        print(f"Against B: {get_item_info(item_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        os.system('clear')
        print(logo)
        
        if guess == compare_items(item_a['follower_count'], item_b['follower_count']):
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final Score: {score}")
            is_game_over = True

play_game()