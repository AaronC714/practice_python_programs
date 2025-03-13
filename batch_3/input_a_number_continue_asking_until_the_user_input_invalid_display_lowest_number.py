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

        # Check if it's the lowest number so far
        if lowest_number is None or num < lowest_number:
            lowest_number = num  # Update lowest number
    except ValueError:
        # Break the loop if input is invalid
        break

# Display the lowest number if any numbers were entered
if lowest_number is not None:
    print("The lowest number entered is:", lowest_number)
else:
    print("No valid numbers were entered.")