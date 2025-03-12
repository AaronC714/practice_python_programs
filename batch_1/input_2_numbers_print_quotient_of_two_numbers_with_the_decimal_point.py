#Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point
# input two numbers
# process
# print quotient

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

if num1 == 0 or num2 == 0:
    print ("zero cannot be an input")
else:
    print("the quotient is: ", num1 / num2)