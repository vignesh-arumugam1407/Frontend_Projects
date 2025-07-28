''' Write a Python program to sort a list of tuples using Lambda.
 Original list of tuples:
 [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]'''

# Original list of tuples
subjects = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Sorting the list of tuples by the second element (score)
sorted_subjects = sorted(subjects, key=lambda x: x[1])

# Displaying the sorted list
print("Sorted list of tuples by scores:")
print(sorted_subjects)
