from datetime import datetime

current_year = datetime.now().year

name, age = input("Enter your name and age in the format [name age]: ").split()
num = input("Enter a number: ")

hundred_year = current_year + 100 - int(age)

#print("{}, you will turn 100 years old in the year {}.".format(name, hundred_year))
#print(f"{name}, you will turn 100 years old in the year {hundred_year}.")
#print(name, ", you will turn 100 years old in the year ", hundred_year, ".", sep="")
#print(name + ", you will turn 100 years old in the year " + str(hundred_year) + ".")
#print("{n}, you will turn 100 years old in the year {y}.".format(n = name, y = hundred_year))
#print("{0}, you will turn 100 years old in the year {1}.".format(name, hundred_year))
#print("%s, you will turn 100 years old in the year %d." % (name, hundred_year))
#print("%(n)s, you will turn 100 years old in the year %(y)d." % {"n" : name, "y" : hundred_year})

for i in range(int(num)):
    print("%s, you will turn 100 years old in the year %d." % (name, hundred_year), end = "")

print("\n")
for i in range(int(num)):
    print("%s, you will turn 100 years old in the year %d." % (name, hundred_year))
