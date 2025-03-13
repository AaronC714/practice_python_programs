#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function
#ask user for input
#continue asking until invalid
#display number in ascending order

inputted_numbers = []

while True:
    try:
        num = int(input("Enter a number (or any non-number to stop): "))
        inputted_numbers.append(num)  # Add the valid number to the list
    except ValueError:
        # Break the loop if input is invalid
        break