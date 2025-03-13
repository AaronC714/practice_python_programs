#Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number.
#ask user for input (number)
#continue asking (loop)
#display lowest number

# Initialize a variable to store the lowest number
lowest_number = None

while True:
    try:
        # Ask the user for a number
        num = int(input("Enter a number (or any non-number to stop): "))