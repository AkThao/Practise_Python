with open("primeslist.txt") as read_file:
    primes = read_file.read()

with open("happieslist.txt") as read_file:
    happies = read_file.read()

prime_list = primes.split("\n")
happy_list = happies.split("\n")


# Method 1: for loop
def find_overlaps(list_1, list_2):
    overlap_list = []
    for num in prime_list:
        if num in happy_list:
            overlap_list.append(num)

    return overlap_list

print(find_overlaps(prime_list, happy_list))

# Method 2: list comprehension
overlaps = [num for num in prime_list if num in happy_list]
print(overlaps)