#Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.
#input 10 numbers
#process
#display all numbers. For numbers with duplicate, display only the first entry.

numbers = [int(input(f"type a number {i+1}: ")) for i in range (10)]
first_entry = []
for num in numbers:
    if num not in first_entry:
        first_entry.append(num)
        print (num)