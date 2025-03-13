#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.
#input 10 numbers
#process
#display all numbers that don't have duplicate

numbers = [int(input("type a number: ")) for _ in range (10)]
no_duplicates = [num for num in numbers if numbers.count(num) == 1]
print (no_duplicates)