'''Write a Python program to find numbers divisible by nineteen or thirteen from a list 
of numbers using Lambda'''
# List of numbers
numbers = [10, 19, 26, 39, 52, 65, 91, 104, 130, 182, 195]

# Lambda function to filter numbers divisible by 19 or 13
divisible_by_19_or_13 = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, numbers))

# Print the result
print("Numbers divisible by 19 or 13:", divisible_by_19_or_13)
