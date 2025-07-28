'''Write a Python program to sort a list of dictionaries using Lambda.
 Original list of dictionaries :
 [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 
'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]'''
# Original list of dictionaries
phones = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

# Sorting the list of dictionaries by the 'model' key
sorted_phones = sorted(phones, key=lambda x: int(x['model']))

# Displaying the sorted list
print("Sorted list of dictionaries by 'model':")
print(sorted_phones)
