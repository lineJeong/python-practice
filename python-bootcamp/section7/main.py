# 랜덤 단어 생성
# 단어 길이만큼의 빈칸 생성
# 유저가 글자를 추측해서 입력
    # 맞을 때 
        # 빈칸을 해당 글자로 채움
        # 빈칸이 전부 채워졌다면 종료(win), 아니라면 유저 추측으로 다시 돌아감
    # 틀릴 때
        # 행맨을 1회 그림
        # 행맨이 완성됐다면 종료(lose), 아니라면 유저 추측으로 다시 돌아감

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

blank_list = []

while len(blank_list) < len(chosen_word):
    blank_list.append("_")

print(chosen_word)
print(blank_list)

guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")