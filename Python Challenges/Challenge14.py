'''Convert two lists into a dictionary in Python without using a built-in method'''
keys = ['apple', 'banana', 'cherry']
values = [1, 2, 3]
dictionary = {}
for i in range(len(keys)):
    dictionary[keys[i]] = values[i]
print(dictionary)
