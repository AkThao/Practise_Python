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

remaining_word = ["_ "] * word_len
guessed_letters = []
while "_ " in remaining_word:
    user_guess = input("Guess a letter:\n").upper()
    if user_guess in guessed_letters:
        print("\nYou have already guessed that letter, try again.\n")
        continue
    guessed_letters.append(user_guess)
    result = check_user_guess(user_guess, random_word, remaining_word)
    if result == False:
        print("\nIncorrect\n")
        continue
    else:
        remaining_word = result
        print("\n" + "".join(remaining_word) + "\n")

print("\nYou win!\n")