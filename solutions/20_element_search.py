from random import randint


def create_ordered_list():
    random_list = [randint(1, 100) for i in range(randint(1, 100))]
    random_list.sort()

    return random_list


def search_for_element(ordered_list, num):
    return num in ordered_list


def binary_search_for_element(ordered_list, num):
    while len(ordered_list) > 0:
        midpoint = len(ordered_list) // 2
        middle_element = ordered_list[midpoint]
        if num == middle_element: # num is in ordered_list, stop binary search
            return True
        elif num < middle_element: # num is in first half, ignore second half
            ordered_list = ordered_list[:midpoint]
        elif num > middle_element: # num is in second half, ignore first half
            ordered_list = ordered_list[midpoint + 1:]
    return False


ordered_list = create_ordered_list()
print(ordered_list)
for i in range(100):
    user_num = int(input("Enter a number between 1 and 100:\n"))
    print(search_for_element(ordered_list, user_num))
    print(binary_search_for_element(ordered_list, user_num))