'''Write a function in Python to count and display the total number of words in a 
text file.'''
def count_total_words(filename):
    total_words = 0
    with open(filename, 'r') as file:
        for line in file:
            # Split the line into words and count them
            words = line.split()
            total_words += len(words)
    return total_words

# Example usage
filename = 'story.txt'
result = count_total_words(filename)
print(f"Total number of words in the file: {result}")
