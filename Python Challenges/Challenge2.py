# Write Program to given string is a palindrome (reads the same forwards and backwords)

# Input from user for variable - a

a=input("Enter a string : ")

if a==a[::-1]:                          #This condition involves reversing the string and comparing it with the original string.
    print("This is Palindrome")        
else:
    print("This is not palindrome")
