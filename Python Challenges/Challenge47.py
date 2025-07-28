''' Write a function in Python to count words in a text file those are ending with 
alphabet "e"'''
def count_words_ending_with_e(filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            # Split the line into words
            words = line.split()
            for word in words:
                # Check if the word ends with 'e' (case-insensitive)
                if word.lower().endswith('e'):
                    count += 1
    return count

# Example usage
filename = 'story.txt'
result = count_words_ending_with_e(filename)
print(f"Number of words ending with 'e': {result}")
