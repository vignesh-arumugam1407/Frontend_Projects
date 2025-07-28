'''Count Vowels and Consonants 
Create a Python function that takes a string as input and counts the number of 
vowels and consonants in the string'''
def count_vowels_consonants(input_string):

    # Convert the input string to lowercase
    input_string = input_string.lower()

    # Initialize counters for vowels and consonants
    vowel_count = 0
    consonant_count = 0

    # Define the set of vowels
    vowels = set('aeiou')

    # Iterate over each character in the input string
    for char in input_string:
        # Check if the character is an alphabet letter
        if char.isalpha():
            # Check if the character is a vowel
            if char in vowels:
                vowel_count += 1
            # If not a vowel, increment the consonant count
            else:
                consonant_count += 1

    # Return the counts of vowels and consonants
    return vowel_count, consonant_count

# Example usage:
input_str = "Hello, World!"
vowels, consonants = count_vowels_consonants(input_str)
print(f"Vowels: {vowels}, Consonants: {consonants}")