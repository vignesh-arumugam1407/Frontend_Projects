''' Write a Python program to square and cube every number in a given list of integers
 using Lambda.
 Original list of integers:
 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'''
# Original list of integers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Squaring every number in the list
squared_numbers = list(map(lambda x: x ** 2, numbers))

# Cubing every number in the list
cubed_numbers = list(map(lambda x: x ** 3, numbers))

# Displaying the results
print("Original list of integers:")
print(numbers)
print("\nSquared numbers:")
print(squared_numbers)
print("\nCubed numbers:")
print(cubed_numbers)
