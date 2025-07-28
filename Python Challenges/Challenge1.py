# Write a program that counts the number of vowels and consonants in a string:

# Input form User for Variable-String

String=(input("Enter a string: "))

Vowels="aeiouAEIOU"                            # Total Vowels in alphabets

vowels_counts=0
consonants_counts=0

for char in String:
    if char.isalpha():                         # Python checks if all characters in a string are alphabetic (a-z, A-Z)
        if char in Vowels:
            vowels_counts+=1                   # if the alphabet is Vowels , vowels_counts is Increasd +1
        else:
            consonants_counts+=1               # Otherwise, consonants_counts is Increased +1 

print("Total Vowels Counts : ",vowels_counts)
print("Total Consonants Counts : ",consonants_counts)



