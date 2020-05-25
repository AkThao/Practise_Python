user_num = int(input("Enter a number:\n"))

def find_divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]

    return divisors

divisors = find_divisors(user_num)
print(f"Divisors of {user_num} are: {divisors}")