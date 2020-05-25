def max_of_three_ifs(var_1, var_2, var_3):
    if var_1 > var_2 and var_1 > var_3:
        return var_1
    elif var_2 > var_3:
        return var_2
    else:
        return var_3


def max_of_three_sort(var_1, var_2, var_3):
    list_of_vars = sorted([var_1, var_2, var_3])

    return list_of_vars[-1]


if __name__ == "__main__":
    from timeit import timeit

    num_1 = 1
    num_2 = 2
    num_3 = 3
    if_time = timeit("max_of_three_ifs(num_1, num_2, num_3)", setup="from __main__ import max_of_three_ifs", globals=globals())
    sort_time = timeit("max_of_three_sort(num_1, num_2, num_3)", setup="from __main__ import max_of_three_ifs", globals=globals())

    if if_time <= sort_time:
        print(f"\nIf statements are faster than sorting by {round(sort_time/if_time, 2)} times.\n")
    else:
        print(f"\nSorting is faster than if statements by {round(if_time/sort_time, 2)} times.\n")