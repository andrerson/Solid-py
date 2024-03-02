from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    name = 'Rectangle'

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    name = 'Circle'

    def __init__(self, radius):
        self.raius = radius

    def area(self):
        return 3.14 * self.raius * self.raius
    
class Triangle(Shape):
    name = 'Triangle'

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2

def calculate_total_area(shapes):
    total_area = sum(shape.area() for shape in shapes)
    return total_area

def calculate_each_area(shape):
    for shape in shapes:
        print(f'{shape.name}: {shape.area()}')

shapes = [Rectangle(4,5), Circle(3), Triangle(13, 7)]
total_area = calculate_total_area(shapes)
calculate_each_area(shapes)
print("Total area:", total_area)