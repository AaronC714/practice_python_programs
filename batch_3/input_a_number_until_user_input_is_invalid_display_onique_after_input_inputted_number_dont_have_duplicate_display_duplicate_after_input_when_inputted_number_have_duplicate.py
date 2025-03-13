#Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.
#user input
#continue asking until the user input is invalid
#Display unique after input when the inputted number don't have duplicate
#display duplicate after input when the inputted number have duplicate


inputted_numbers = []

while True:
    try:
        num = int(input("Enter a number (or any non-number to stop): "))

        # Check if the number is a duplicate
        if num in inputted_numbers:
            print("Duplicate")
        else:
            print("Unique")
            inputted_numbers.append(num)  # Add to list if unique
    except ValueError:
        # Break the loop when input is invalid (not a number)
        print("Invalid input! Stopping program.")
        break
