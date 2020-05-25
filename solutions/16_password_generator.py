from random import randint, choice

# Use HTML ASCII codes from 33 to 126 inclusive (characters ! to ~)

strength = int(input("How strong would you like your password to be? [1 = weak, 2 = medium, 3 = strong]?\n"))


def generate_password(strength):
    word_list = open("word_list.txt", "r")
    words = word_list.readlines()
    word_list.close()

    if strength == 1:
        password = choice(words).replace("\n", "")
    elif strength == 2:
        password = []
        for i in range(10):
            password.append(chr(randint(33, 127)))
        password = "".join(password)
    elif strength == 3:
        password = choice(words) + "-" + choice(words) + "-" + choice(words)
        password = password.replace("\n", "")

    return password


password = generate_password(strength)
print(f"\nThe password is:\n{password}")