from random import choice

with open("sowpods.txt", 'r') as read_file:
    word_list = read_file.readlines()

random_word = choice(word_list).strip()
print(random_word)