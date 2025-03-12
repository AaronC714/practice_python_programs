#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
#input 10 numbers
#process
#print the result of the first number minus all of the remaining numbers.


numbers = [int(input(f"Enter number {i+1}: ")) for i in range(10)]

first_number = numbers[0]

result = first_number
for num in numbers[1:]:
    result -= num

print("The result of the first number minus all remaining numbers is:", result)
