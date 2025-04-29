import math

class Shape:
    def area(self):
        raise NotImplementedError("Area calculation not defined for this shape")

    def __str__(self):
        return "Shape"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle (width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def __str__(self):
        return f"Square (side={self.side})"
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def __str__(self):
        return f"Circle (radius={self.radius})"


if __name__ == "__main__":
    rectangle = Rectangle(5, 10)
    square = Square(7)
    circle = Circle(3)

    shapes = [rectangle, square, circle]
    for shape in shapes:
        print(f"Area of {shape}: {shape.area()}")