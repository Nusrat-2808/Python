from abc import ABC,abstractmethod
class Polygon(ABC):
    def area(self):
        pass
# Rectangle class
class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Triangle class
class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
# Circle class
class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1415 * self.radius ** 2

# Square class
class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
polygon=input('Enter the type of Polygon.')
if polygon=="Rectangle":
    length=int(input('Enter the length'))
    width=int(input('Enter the width'))
    print('AREA: ',Rectangle(length,width).area())
else:
    print('Invalid calculative object.')
Square.area(5)