#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.
#ask input from user
#continue asking until non integer input
#compute average

inputted_numbers = []

while True:
    try:
        num = float(input("Enter a number (or any non-number to stop): "))
        inputted_numbers.append(num)  # Add valid number to the list
    except ValueError:
        break