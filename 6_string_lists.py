user_string = input("Enter a string:\n").replace(" ", "").lower()

def check_palindrome(input_string):
    reverse_string = input_string[::-1]

    return input_string == reverse_string

if check_palindrome(user_string):
    print("Your string is a palindrome!")
else:
    print("Your string is not a palindrome.")