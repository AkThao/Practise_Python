from random import randint


def make_random_list():
    random_list = [randint(1, 50) for i in range(randint(1, 100))]

    return random_list


def remove_duplicates(input_list):
    new_list = []
    for i in input_list:
        if i not in new_list:
            new_list.append(i)

    return new_list


def remove_duplicates_with_sets(input_list):
    new_list = list(set(input_list))

    return new_list


list_with_duplicates = make_random_list()
first_list_without_duplicates = remove_duplicates(list_with_duplicates)
second_list_without_duplicates = remove_duplicates_with_sets(list_with_duplicates)


print(list_with_duplicates)
print(first_list_without_duplicates)
print(second_list_without_duplicates)