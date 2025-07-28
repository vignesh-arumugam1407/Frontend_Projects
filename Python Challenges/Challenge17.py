'''Write a program to print sum of digits.'''
num = int(input("Enter a number: "))

# Convert the number to a string
str_num = str(num)

# Calculate the sum of digits
sum = 0
for digit in str_num:
    sum += int(digit)

print("The sum of digits is:", sum)
