# Rectangle class
class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Triangle class
class Triangle():
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
# Circle class
class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1415 * self.radius ** 2

# Square class
class Square():
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
obj1=Rectangle(4,5)
obj2=Triangle(5,6)
obj3=Circle(7)
obj4=Square(6)
for object in (obj1,obj2,obj3,obj4):
    print('My area is ',object.area())