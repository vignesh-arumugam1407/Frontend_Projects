'''Write a program to create an abstract class Shape with abstract methods
 calculateArea() and calculatePerimeter(). Create subclasses Circle and Triangle 
that extend the Shape class and implement the respective methods to calculate 
the area and perimeter of each shape'''

from abc import ABC , abstractmethod
import math

class shape(ABC):
    @abstractmethod
    def calculateArea(self):
        pass
    @abstractmethod
    def calculatePerameter(self):
        pass
class Circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def calculateArea(self):
        return math.pi * self.radius ** 2

    def calculatePerameter(self):
        return 2 * math.pi * self.radius

class Triangle(shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculateArea(self):
        # Using Heron's formula
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def calculatePerameter(self):
        return self.a + self.b + self.c

if __name__ == "__main__":
    # Create instances of Circle and Triangle
      circle = Circle(5)  # Radius = 5
      triangle = Triangle(3, 4, 5)  # Sides = 3, 4, 5

    # Display Circle properties
print("Circle:")
print("Area:", circle.calculateArea())
print("Perimeter:", circle.calculatePerameter())

    # Display Triangle properties
print("\nTriangle:")
print("Area:", triangle.calculateArea())
print("Perimeter:", triangle.calculatePerameter())
