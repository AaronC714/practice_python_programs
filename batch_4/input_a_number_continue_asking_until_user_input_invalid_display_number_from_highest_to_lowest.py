#Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function
#ask number input from user
#continue asking until invalid
#display numbers in descending order

inputted_numbers = []

while True:
    try:
        num = int(input("Enter a number (or any non-number to stop): "))
        inputted_numbers.append(num)  # Add valid number to the list
    except ValueError:
        break