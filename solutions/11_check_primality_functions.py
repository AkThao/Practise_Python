def find_divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]

    return divisors


def is_prime(divisors, num):
    return divisors == [1, num]


user_input = int(input("Enter a number:\n"))

divisors = find_divisors(user_input)
if is_prime(divisors, user_input):
    print(f"{user_input} is prime")
else:
    print(f"{user_input} is not prime")