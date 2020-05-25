import sys

user_num = int(input("How many Fibonacci numbers?\n"))

if user_num <= 0:
    print("Must be a postive integer.")
    sys.exit()


def fibonacci(num_of_terms):
    n1, n2 = 0, 1
    count = 0

    if num_of_terms == 1:
        print(f"\n{n1}")
    else:
        print("")
        while(count < num_of_terms):
            print(n1)
            next_term = n1 + n2
            n1 = n2
            n2 = next_term

            count += 1


def fibonacci_recursive(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


fibonacci(user_num)
print("")
for i in range(1, user_num + 1):
    print(fibonacci_recursive(i))