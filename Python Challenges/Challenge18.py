'''Print the Fibonacci series for first 12 numbers'''

a, b = 0, 1
for _ in range(12):
    print(a, end=" ")
    a, b = b, a + b
