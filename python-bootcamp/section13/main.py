############ DEBUGGING############
from random import randint

# # 1. Describe Problem


# def my_function():
#     for i in range(1, 20):  # 1~19
#         if i == 20:
#             print("You got it")


# my_function()


# # Fix


def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()


# # 2. Reproduce the Bug
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])


# # Fix
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])


# # 3. Play Computer
# year = int(input("What's your year of birth? "))
# if year > 1980 and year < 1994:
#     print("You are a millenial.")
# elif year > 1994:
#     print("You are a Gen Z.")


# # Fix
year = int(input("What's your year of birth? "))
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year >= 1994:
    print("You are a Gen Z.")
