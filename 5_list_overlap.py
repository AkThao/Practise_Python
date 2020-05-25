from random import randint

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def find_overlap(list_1, list_2):
    combined_list = list_1 + list_2
    combined_set = set(combined_list)

    overlap = [i for i in combined_set if i in list_1 and i in list_2]

    return overlap


def make_random_lists():
    list_1 = [randint(1, 50) for i in range(randint(1, 100))]
    list_2 = [randint(1, 50) for i in range(randint(1, 100))]

    return list_1, list_2


overlap_nums = find_overlap(a, b)
print(overlap_nums)

(x, y) = make_random_lists()
random_overlap_nums = find_overlap(x, y)
print(random_overlap_nums)

#### One-liner ####
print([i for i in set(make_random_lists()[0] + make_random_lists()[1]) if i in make_random_lists()[0] and i in make_random_lists()[1]])