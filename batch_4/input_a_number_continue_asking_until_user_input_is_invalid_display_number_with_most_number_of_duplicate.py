#Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.
#user input numbers
#process
#display the number with the most number of duplicate

from collections import Counter

inputted_numbers = []

while True:
    try:
        num = int(input("Enter a number (or any non-number to stop): "))
        inputted_numbers.append(num)  # Add valid number to the list
    except ValueError:
        # Break the loop when input is invalid
        break


if inputted_numbers:
    duplicates_number = Counter(inputted_numbers)  # Count occurrences of each number
    most_common = duplicates_number.most_common(1)  # Get the most frequent number
    
    # Extract the number and its count
    number, count = most_common[0]

    print(f"The number with the most duplicates is: {number} (appeared {count} times)")
else:
    print("No valid numbers were entered.")