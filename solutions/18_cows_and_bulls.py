from random import randint


def create_random_num():
    random_num = []
    while len(random_num) != 4:
        random_digit = randint(1, 9)
        if random_digit not in random_num:
            random_num.append(random_digit)

    return random_num


random_num = create_random_num()
print(random_num)

guesses = 7

def check_cows_bulls(guess):
    cows = 0
    bulls = 0
    for i in range(len(guess)):
        if guess[i] == random_num[i]: # +1 bull for correct number and correct position
            bulls += 1
        elif guess[i] != random_num[i] and guess[i] in random_num: # +1 cow for correct number but wrong position
            cows += 1

    return (cows, bulls)


if __name__ == "__main__":
    while (guesses > 0):
        print(f"\n{guesses} guesses remaining.")
        user_guess = input("Guess a 4-digit number:\n")
        user_digits = [int(d) for d in user_guess]
        cows_bulls = check_cows_bulls(user_digits)
        print(f"{cows_bulls[0]} cows, {cows_bulls[1]} bulls.\n")
        if cows_bulls[1] == 4: # if 4 bulls, all digits are correct and in correct positions
            print("Congratulations, you win!\n")
            break
        guesses -= 1
    print(f"You took {7 - guesses + 1} guesses.\n")