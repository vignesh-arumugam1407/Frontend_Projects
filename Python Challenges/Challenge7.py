'''Create a Python program that takes two lists and returns a new list containing 
elements that are common in both input lists.'''

#Input from User
a=input("Enter a number with spaces: ").split()
b=input("Enter a number with spaces: ").split()

#Convert to list
c=list(a)
d=list(b)

#Convert to set for faster lookup
a_set=set(c)
b_set=set(d)

if a_set & b_set:
    print(a_set & b_set)
else:
    print('no common element')
