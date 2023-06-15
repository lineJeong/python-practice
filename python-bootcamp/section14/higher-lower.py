# 1. Breakdown the problem
# 2. Start with the easiest
# 3. Turn the problem into comments
# 4. Write code -> Run code -> Fix code

from random import randint
from art import logo, vs
from data import data

# data 랜덤 추출


def pick_item():
    random_idex = randint(0, len(data) - 1)
    return data[random_idex]

# A, B의 팔로워 수 비교
# 유저의 선택에 따라 결과 분기
# 유저가 더 많은 팔로워를 맞췄으면, score+1하고 정답(A or B)는 유지하고 새로운 랜덤 아이템과 비교
# 정답이 B면, 다음 판에서는 A에 올라가 있어야 함
# 정답을 맞추지 못하면 종료


def play_game():
    print(logo)

    item_A = pick_item()
    item_B = pick_item()

    # print(f"You're right! Current score: {}") # 최소 1개 이상 맞췄을 때부터 띄워줌
    print(
        f"Compare A: {item_A['name']}, {item_A['description']}, from {item_A['country']}")
    print(vs)
    print(
        f"Compare B: {item_B['name']}, {item_B['description']}, from {item_B['country']}")
    # input("who has more followers? Type 'A' of 'B': ")


play_game()
