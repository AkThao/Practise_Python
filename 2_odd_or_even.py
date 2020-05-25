user_num = int(input("Enter a number: "))
if (user_num % 4 == 0):
    print("Your number is a multiple of 4.\n")
elif (user_num % 2 == 0):
    print("Your number is even but not a multiple of 4.\n")
else:
    print("Your number is odd.\n")

num = int(input("\nEnter a number to be divided (number 1): "))
check = int(input("\nEnter a number by which to divide number 1 (number 2): "))
if (num % check == 0):
    print("Number 1 divides evenly by number 2.")
else:
    print("Number 2 divides into number 1 with a remainder of {}.".format(num % check))
