'''Unique Characters 
Create a Python program that takes a string as input and checks if all the
 characters in the string are unique (i.e., no character repeats). Return True if all 
characters are unique, and False otherwise.'''

#Get Input from user
a=input("Enter a characters : ")

#Use a set to track seen characters
seen=set()
unique=True
for char in a:
    if char in seen:
        unique=False
        break
    seen.add(char)
if unique:
    print(True)
else:
    print(False)