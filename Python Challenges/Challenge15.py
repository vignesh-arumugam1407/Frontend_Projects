'''Write a program to check Armstrong number? '''

num = int(input("Enter a number: "))

# Calculate the number of digits
num_digits = len(str(num))

# Initialize sum
sum = 0

# Calculate the sum of each digit raised to the power of the number of digits
for digit in str(num):
    sum += int(digit) ** num_digits

# Check if the sum is equal to the original number
if sum == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")