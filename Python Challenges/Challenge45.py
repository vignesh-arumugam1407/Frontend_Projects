''' Write a Python program to calculate the sum of the positive and negative numbers 
of a given list of numbers using the lambda function'''
# List of numbers
numbers = [10, -5, 3, -9, 7, -7, 8, -6]

# Lambda function to calculate sum of positive numbers
sum_positive = sum(filter(lambda x: x > 0, numbers))

# Lambda function to calculate sum of negative numbers
sum_negative = sum(filter(lambda x: x < 0, numbers))

# Print the results
print("Sum of positive numbers:", sum_positive)
print("Sum of negative numbers:", sum_negative)
