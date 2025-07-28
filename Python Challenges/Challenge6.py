'''Remove Duplicates from a List
 Create a Python function that takes a list as input and removes duplicate 
elements, preserving the order of the elements. Return the new list : '''

#Input From User
input_number = input("Enter a list of numbers : ")

#Split the Strings
number=input_number.split()

#convert to Integer using map
number=(map(int,number))

#convert to list
number=list(number)
result=[]
for item in number:
    if item not in result:
        result.append(item)
print(result)







