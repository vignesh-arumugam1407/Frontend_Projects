'''You are developing a class called MathUtils that provides various mathematical 
utility functions. Implement a static method called calculateSum() 
MathUtils class. The calculateSum() 
in the 
method should accept an array of numbers 
and return the sum of those numbers. 
Write the MathUtils class with the static calculateSum() 
code to test the functionality.'''

class Mathutils:
    @staticmethod
    def calculateSum(numbers):
        return sum(numbers)

# Test the functionality of Mathutils.calculateSum
if __name__ == "__main__":
    # Test cases
    test_case_1 = [1, 2, 3, 4, 5]  
    test_case_2 = [-1, -2, -3, -4, -5]  
    test_case_3 = [0.5, 1.5, 2.5]  

    print("Sum of test_case_1:", Mathutils.calculateSum(test_case_1))
    print("Sum of test_case_2:", Mathutils.calculateSum(test_case_2))
    print("Sum of test_case_3:", Mathutils.calculateSum(test_case_3))
