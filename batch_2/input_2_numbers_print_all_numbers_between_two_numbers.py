#Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.
# input two numbers
# process
# print all the numbers between the two numbers

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

if num1 > num2:
    num1, num2 = num2, num1  # numbers should be in increasing order

print(f"Numbers between {num1} and {num2}:")
for num in range(num1 + 1, num2):
    print(num)