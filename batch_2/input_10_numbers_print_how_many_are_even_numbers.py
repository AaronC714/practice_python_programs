#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.
#input 10 numbers
#process
#print how many even numbers are there.

numbers = [int(input("type a number: ")) for _ in range (10)]
even_count = sum(1 for num in numbers if num % 2 == 0)

print("the total even numbers present is: ", even_count)