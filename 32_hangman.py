from random import choice

with open("sowpods.txt", 'r') as read_file:
    word_list = read_file.readlines()


random_word = choice(word_list).strip()
#print("\n" + random_word + "\n")

word_len = len(random_word)


def check_user_guess(input_letter, random_word, remaining_word):
    if input_letter not in random_word:
        return False
    else:
        for i in range(word_len):
            if input_letter == random_word[i]:
                remaining_word[i] = input_letter + " "
        return remaining_word


def check_if_won(remaining_word):
    if "_ " not in remaining_word:
        return True
    return False


def display_hangman(guesses):
    if guesses == 5:
        print("""
                 /
                /
               /
              /""")
    elif guesses == 4:
        print("""
                 / \\
                /   \\
               /     \\
              /       \\""")
    elif guesses == 3:
        print("""
                  |
                  |
                  |
                  |
                 / \\
                /   \\
               /     \\
              /       \\""")
    elif guesses == 2:
        print("""
              ____|
                  |
                  |
                  |
                  |
                 / \\
                /   \\
               /     \\
              /       \\""")
    elif guesses == 1:
        print("""
              ____|____
                  |
                  |
                  |
                  |
                 / \\
                /   \\
               /     \\
              /       \\""")
    elif guesses == 0:
        print("""
    ___________
    |   /     |
    |  /      |
    | /      ---
    |/      |   |
    |        ---
    |     ____|____
    |         |
    |         |
    |         |
    |         |
    |        / \\
    |       /   \\
    |      /     \\
    |     /       \\
    |
    |__________________""")



remaining_word = ["_ "] * word_len
guessed_letters = []
guesses = 6
while guesses > 0:
    user_guess = input("\nGuess a letter:\n").upper()

    if user_guess in guessed_letters:
        print("\nYou have already guessed that letter, try again.\n")
        continue

    guessed_letters.append(user_guess)
    result = check_user_guess(user_guess, random_word, remaining_word)
    if result == False:
        print("\nIncorrect")
        guesses -= 1
        display_hangman(guesses)
        continue
    else:
        remaining_word = result
        print("\n" + "".join(remaining_word) + "\n")
        if check_if_won(remaining_word):
            print("\nYou win!\n")
            break


if guesses == 0:
    print("\nOut of guesses.\nYou lose.\n")
    print(f"The word was {random_word}.\n")