'''You are developing a system to handle different shapes. Implement an abstract 
class called Shape with an abstract method calculateArea() . The calculateArea() 
method should be implemented by the concrete classes that inherit from Shape 
and should return the area of the specific shape. 
Create two concrete classes Circle and Rectangle that extend the Shape class. 
Implement the calculateArea() 
method in both classes according to the area 
calculation formulas for circles and rectangles. Display the areas of a circle and 
a rectangle object. 
Write the abstract class Shape , the concrete classes Circle and Rectangle , and 
the code to display the areas.'''
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculateArea(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculateArea(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculateArea(self):
        return self.width * self.height

# Example usage
circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Area of the circle: {circle.calculateArea()}")
print(f"Area of the rectangle: {rectangle.calculateArea()}")
