'''Write a program to create a custom iterator that iterates from 1 to 10 in 0.5 intervals'''
# Basic method using a loop
if __name__ == "__main__":
    current = 1
    while current <= 10:
        print(current, end=" ")
        current += 0.5
