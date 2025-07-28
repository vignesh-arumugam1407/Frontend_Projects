'''Write a program to check palindrome number'''

num = int(input("Enter a number: "))

# Convert the number to a string
str_num = str(num)

# Check if the string is equal to its reverse
if str_num == str_num[::-1]:
    print(num, "is a palindrome number.")
else:
    print(num, "is not a palindrome number.")