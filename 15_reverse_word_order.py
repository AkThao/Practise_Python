user_string = input("Enter a sentence:\n")


def reverse_words(input_str):
    list_of_words = input_str.split()
    reversed_list_of_words = list_of_words[::-1]

    return " ".join(reversed_list_of_words)

reversed_string = reverse_words(user_string)
print(f"\nSentence with words reversed:\n{reversed_string}")