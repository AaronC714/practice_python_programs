#Prog06: Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.
#ask user for their full name in incorrect casing
#reverse casing
#print each letter of the name in reverse casing

user_name = str(input("Type your full name in an incorrect casing for (e.g.  jUAn DEla CrUZ): "))
swap_case = user_name.swapcase()