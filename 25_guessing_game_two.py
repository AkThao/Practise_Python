def make_guess(old_guess, direction, minimum, maximum):
    if old_guess == None:
        guess = 50
    elif direction == 'h':
        maximum = old_guess - 1
        guess = (minimum + maximum) // 2
    elif direction == 'l':
        minimum = old_guess + 1
        guess = (minimum + maximum) // 2

    return guess, minimum, maximum


def check_if_correct(guess):
    result = input(f"\nIs {guess} correct [y/n]?\n").lower()

    if result == 'n':
        direction = input("\nToo high [h] or too low [l]?\n").lower()
        return False, direction
    elif result == 'y':
        print("\nYay!")
        print(f"It took {guesses} guesses")
        return True, 0

user_num = int(input("\nEnter a number between 0 and 100:\n"))
old_guess = None
direction = 0
minimum = 0
maximum = 100
guesses = 0


while 1:
    (guess, new_min, new_max) = make_guess(old_guess, direction, minimum, maximum)
    guesses += 1
    old_guess = guess
    minimum = new_min
    maximum = new_max
    (result, direction) = check_if_correct(guess)
    if result:
        break
    else:
        continue