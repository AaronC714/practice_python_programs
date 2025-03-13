#Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.
#user input numbers
#process
#display the number with the most number of duplicate

inputted_numbers = []

while True:
    try:
        num = int(input("Enter a number (or any non-number to stop): "))
