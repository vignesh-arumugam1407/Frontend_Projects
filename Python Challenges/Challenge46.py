'''Write a function in python to count the number of lines from a text file "story.txt" 
which is not starting with an alphabet "T"'''
def count_lines_not_starting_with_T(filename):
    with open(filename, 'r') as file:
        # Use list comprehension to count lines not starting with 'T'
        return sum(1 for line in file if not line.lstrip().startswith('T'))

# Example usage
filename = 'story.txt'
result = count_lines_not_starting_with_T(filename)
print(f"Number of lines not starting with 'T': {result}")
