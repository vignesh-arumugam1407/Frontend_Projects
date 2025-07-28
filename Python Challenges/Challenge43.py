'''Write a Python program to create Fibonacci series up to n using Lambda'''
from functools import reduce

# Function to generate Fibonacci series up to n
def fibonacci_series(n):
    fib = lambda x, _: x + [x[-1] + x[-2]]
    return reduce(fib, range(n-2), [0, 1])[:n]

# Example usage
n = 10  # Change this value to generate more or fewer Fibonacci numbers
print(fibonacci_series(n))

