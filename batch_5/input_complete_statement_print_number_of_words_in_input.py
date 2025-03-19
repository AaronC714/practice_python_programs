#Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.
#ask user for statement
#count number of words
#print number of words

user_statement = str(input("Type a statement: "))
number_word = len(user_statement.split())
print ("The number of words in your inputted statement is: ", number_word)