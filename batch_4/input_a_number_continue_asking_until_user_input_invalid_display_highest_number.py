#Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number
#ask input from user
#process what number is the highest
#print highest number

highest_number = None

while True:
    try:
        # Ask the user for a number
        num = int(input("Enter a number (or any non-number to stop): "))