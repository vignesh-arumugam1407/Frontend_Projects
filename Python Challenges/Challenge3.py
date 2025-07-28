# Write a program to remove duplicate values in the given string:

# Input from User for Variable - String

string1 = input("Enter a String : ")
string2 = ""

for i in string1:
	
	if i not in string2:                     #The not in operator checks if a value does not exist within a sequence.
		string2 = string2 + i
		
print("Remove Duplicate values : ",string2)