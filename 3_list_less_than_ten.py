a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def get_list():
    user_a = []
    for i in range(10):
        user_a.append(int(input(f"Enter a number {[i + 1]}:\n")))

    return user_a


def print_less_than_ten(user_list):
    print("\nNumbers less than 10:")
    for num in user_list:
        if num < 10: print(num)


def print_less_than_ten_in_one_list(user_list):
    print("\nNumbers less than ten:")
    new_list = [num for num in user_list if num < 10]

    print(new_list)


def print_less_than_a_number(user_list):
    number = int(input("\nEnter a number:"))

    new_list = list(filter(lambda x: x < number, user_list))

    print(f"\nNumbers less than {number}: ", new_list)


user_a = get_list()
print_less_than_ten(user_a)
print_less_than_ten_in_one_list(user_a)
print("\nNumbers less than ten: ", list(filter(lambda x: x < 10, user_a)))
print_less_than_a_number(user_a)