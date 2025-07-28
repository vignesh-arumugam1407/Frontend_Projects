'''Reverse a List
 Write a Python function that takes a list and returns a new list with the elements 
reversed. Do this without using the built-in reverse method: '''

## Get input from the user

Original_text=input("Enter a list of Numbers or Characters : ")

Reversed_text=(Original_text[::-1])              # Reverse the order of elements in a sequence

print("Reverse Method : ",Reversed_text)