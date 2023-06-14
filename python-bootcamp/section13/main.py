############ DEBUGGING############

# # Describe Problem
def my_function():
    for i in range(1, 20):  # 1~19
        if i == 20:
            print("You got it")


my_function()


# # Fix
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()
