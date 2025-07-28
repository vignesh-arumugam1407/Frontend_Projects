'''Find Keys with Maximum Value 
Write a Python function that takes a dictionary of items and their prices as input 
and finds and prints the keys (items) with the highest prices'''

items = {'apple': 2.5, 'banana': 1.0, 'cherry': 2.5, 'date': 3.0}
if not items:
    print("The dictionary is empty.")
    
max_value = max(items.values())
for key, value in items.items():
    if value == max_value:
        print(key,value)
