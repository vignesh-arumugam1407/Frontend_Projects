'''Write a program to create an iterator to print English alphabets from A to Z'''
def alphabet_iterator():
    for i in range(65, 91):  # ASCII values for 'A' to 'Z'
        yield chr(i)  # Yield each letter

# Create the iterator
alphabet_iter = alphabet_iterator()

# Iterate through and print each letter
for letter in alphabet_iter:
    print(letter, end=" ")
