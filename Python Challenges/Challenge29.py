# Create a simple calculator operations  using function :-
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


print("Addition = " , {add(num1, num2)})

print("Subraction = " ,{subtract(num1, num2)})

print("Multipication = " , {multiply(num1, num2)})

print("Division = " , {divide(num1, num2)})
