''' Count the Occurrences of an Element
 Write a Python function that takes a tuple and an element as input and counts 
how many times that element appears in the tuple '''

#Input from user 
a=input("Enter a number with spaces : ")

#Split the elements
b=a.split()

#Convert to tuple
c=tuple(b)

count=0

d=input("Enter a repeated number : ")

for i in c:
    if i==d:
        count+=1
print('Total times that element appears in the tuple : ', count)