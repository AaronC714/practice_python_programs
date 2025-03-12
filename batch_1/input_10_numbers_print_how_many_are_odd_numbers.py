#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.
# input ten numbers
# process
# print number of odd numbers 

num1 = [int(input("Type a number: ")) for _ in range (10)]
odd_count = sum(1 for num in num1 if num % 2 != 0)

print("Count of odd numbers:", odd_count)