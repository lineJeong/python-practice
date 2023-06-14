import random
from art import logo


def make_an_answer():
    return random.choice(list(range(1, 101)))


def choose_a_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5


def get_guess_result(guess, answer):
    if (guess == answer):
        print(f"You got it! The answer was {guess}.")

    if (guess < answer):
        print("Too low.")
    elif (guess > answer):
        print("Too high.")


def check_guess_again(attemps):
    if attemps <= 0:
        print("You've run out of guesses, you lose.")
    else:
        print("Guess again.")


def calc_attemps(attempts):
    return attempts - 1


def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")

    answer = make_an_answer()
    print(f"Pssst, the correct answer is {answer}")

    attempts = choose_a_difficulty()

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        get_guess_result(guess, answer)
        attempts = calc_attemps(attempts)

        if answer == guess:
            return
        else:
            check_guess_again(attempts)


play_game()
