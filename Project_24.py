# The Number Guessing Game With Function

import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too High.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too Low.")
        return turns - 1
    else:
        print(f"You Got It: The Answer Was {actual_answer}")


def set_difficulty():
    level = input("Choose a Difficulty, Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Welcome To The Number Guessing Game!")
    print("I'am Thinking Of a Number Between 1 And 100.")
    answer = random.randint(1, 100)
    print(f"Passt, The Correct Answer Is {answer}")

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You Have {turns} Attempts Remaining To Guess The Number.")
        guess = int(input("Make a Guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print(f"You've Run Out Of Guesses, You Lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()