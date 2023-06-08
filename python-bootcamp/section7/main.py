# 랜덤 단어 생성
# 단어 길이만큼의 빈칸 생성
# 유저가 글자를 추측해서 입력
    # 맞을 때 
        # 빈칸을 해당 글자로 채움
        # 빈칸이 전부 채워졌다면 종료(win), 아니라면 유저 추측으로 다시 돌아감
    # 틀릴 때
        # 행맨을 1회 그림
        # 행맨이 완성됐다면 종료(lose), 아니라면 유저 추측으로 다시 돌아감


#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random

chosen_word = random.choice(word_list)
print(chosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.