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
import os
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display_list = []

# while len(display_list) < word_length:
#     display_list.append("_")

# for _ in chosen_word:
#     display_list += "_"

for _ in range(word_length):
    display_list += "_"

print(logo)
print(chosen_word)

end_of_game = False
lives = 6

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    os.system("clear")

    if guess in display_list:
        print(f"You've already guessed {guess}.")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display_list[position] = letter

    if guess not in chosen_word:
        print(f"{guess} is not in the word. You lose a life.")
        lives -= 1

    print(f"{' '.join(display_list)}")
    print(stages[lives])

    if "_" not in display_list:
        end_of_game = True
        print("You win.")
    
    if lives == 0:
        end_of_game = True
        print("You lose.")