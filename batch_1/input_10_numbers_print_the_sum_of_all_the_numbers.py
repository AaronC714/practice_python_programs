# Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
# input ten numbers
# process
# print sum

numbers = [int(input("type a number: ")) for _ in range (10)]
print ("the sum is: ", sum(numbers))