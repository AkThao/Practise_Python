from random import randint
import sys


def check_guess(user_input, random_gen_num):
    if user_input == random_gen_num:
        return "\nCorrect!\n"
    elif user_input < random_gen_num:
        return "\nToo low\n"
    else:
        return "\nToo high\n"


guesses = 0

while(1):
    random_num = randint(1, 9)
    user_guess = input("Guess the number (between 1 and 9) or type 'exit' to exit\n")
    guesses += 1

    if user_guess.lower() == "exit":
        print(f"Answer was {random_num}")
        sys.exit()
    else:
        user_guess = int(user_guess)
        result = check_guess(user_guess, random_num)
        print(result)
        if result == "\nCorrect!\n":
            print(f"{guesses} attempts")
            sys.exit()