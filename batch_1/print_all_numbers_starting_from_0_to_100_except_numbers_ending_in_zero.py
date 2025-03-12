#Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.
#number in range
#process
#print result

for num in range(101):
    if num % 10 != 0:  # Exclude numbers that end in 0
        print(num)