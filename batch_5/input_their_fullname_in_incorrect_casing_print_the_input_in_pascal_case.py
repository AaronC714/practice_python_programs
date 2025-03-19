#Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.
#ask name from user in incorrect casing
#process pascal case
#print name in pascal case

user_name = str(input("Type your full name in an incorrect casing for (e.g.  jUAn DEla CrUZ): "))
pascal_naming = user_name.title().replace(" ", "")