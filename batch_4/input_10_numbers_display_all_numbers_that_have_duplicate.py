#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.
#user input of 10 numbers 
#display all numbers that have duplicate

inputted_num = [int(input(f"Enter number {i+1}: ")) for i in range(10)]

duplicates = sorted(set(num for num in inputted_num if inputted_num.count(num) > 1))

if duplicates:
    print("Numbers that have duplicates:", duplicates)
else:
    print("No duplicate numbers found.")