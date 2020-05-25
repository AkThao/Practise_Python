from random import randint


def make_random_lists():
    list_1 = [randint(1, 50) for i in range(randint(1, 100))]
    list_2 = [randint(1, 50) for i in range(randint(1, 100))]

    return list_1, list_2


print([i for i in set(make_random_lists()[0] + make_random_lists()[1]) if i in make_random_lists()[0] and i in make_random_lists()[1]])