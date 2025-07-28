''' Find the Sum and Average
 Write a Python program that takes a list of numbers as input and calculates and
 prints the sum and   average of those numbers'''

# Get input from the user

a = input("Enter a list of numbers separated by spaces: ")

# Convert the input string into a list of integers

numbers = a.split()                           # Split the Strings
numbers = (map (int,numbers))                 # Using Map function converted to Integers
numbers = list(numbers)                       # Converted to list type

# Find SUM:

total_sum=sum(numbers)
print("Total Sum of the Values: ",total_sum)

#Find Average:

avg=total_sum/(len(numbers))
print("Total Average of the Values: ",avg)
