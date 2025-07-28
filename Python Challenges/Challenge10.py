'''Write a Python program that takes a list of person tuples (name, age) and
 calculates and prints the  average age of the group'''

# Example list of person tuples (name, age)
persons = [
    ("Alice", 10),
    ("Bob", 20),
    ("Charlie", 30),
    ("Diana", 40)
]

# Extract ages from the list of tuples
ages = [person[1] for person in persons]
    
# Calculate the average age
average_age = sum(ages) / len(ages)
    
# Print the result
print("The average age of the group is:" ,average_age)
