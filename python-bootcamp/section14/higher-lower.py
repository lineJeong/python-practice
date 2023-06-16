# 1. Breakdown the problem
# 2. Start with the easiest
# 3. Turn the problem into comments
# 4. Write code -> Run code -> Fix code

import random
import os
from art import logo, vs
from data import data

# data 랜덤 추출


def pick_random_item():
    return random.choice(data)


def get_item_info(item):
    return f"{item['name']}, {item['description']}, from {item['country']}"

# A, B의 팔로워 수 비교
# 유저의 선택에 따라 결과 분기
# 유저가 더 많은 팔로워를 맞췄으면, score+1하고 정답(A or B)는 유지하고 새로운 랜덤 아이템과 비교
# 정답이 B면, 다음 판에서는 A에 올라가 있어야 함
# 정답을 맞추지 못하면 종료


def check_guess(guess, a_follower, b_follower):
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"


def play_game():
    print(logo)

    score = 0
    is_game_over = False

    item_a = pick_random_item()
    item_b = pick_random_item()

    while not is_game_over:
        item_a = item_b
        item_b = pick_random_item()

        while item_a == item_b:
            item_a = pick_random_item()

        # print(f"You're right! Current score: {}") # 최소 1개 이상 맞췄을 때부터 띄워줌

        print(
            f"Compare A: {get_item_info(item_a)}")
        print(vs)
        print(
            f"Compare B: {get_item_info(item_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        is_correct = check_guess(
            guess, item_a["follower_count"], item_b["follower_count"])

        os.system('clear')
        print(logo)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            is_game_over = True
            print(f"Sorry, that's wrong. Final score: {score}")


play_game()
