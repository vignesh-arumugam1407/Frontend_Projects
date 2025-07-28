'''Find Common Elements 
Create a Python program that takes two sets and returns a new set containing 
elements that are common in both input sets'''

#Input from user
a=(input("Enter a number with spaces: "))
b=(input("Enter a number with spaces: "))

#String value convert to Set
set_a=set(a)
set_b=set(b)

# Find common factor
comman=set_a & set_b

print("The common Factor is : ",comman)
print(type(comman))