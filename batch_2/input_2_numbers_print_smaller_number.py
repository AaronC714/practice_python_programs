#Prog01: Create a program that ask user to input 2 numbers. Print the smaller number
# input two numbers
# process
# print smaller number

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

if num1 > num2:
    print (num2)
elif num2 > num1:
    print (num1)
else:
    print ("Numbers are equal")