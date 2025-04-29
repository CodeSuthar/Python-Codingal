import math

class Shape:
    def __init__(self):
        pass

    def area(self):
        raise NotImplementedError("Area calculation not defined for this shape")

    def __str__(self):
        return "Shape"


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height

    def __str__(self):
        return f"Rectangle (width={self._width}, height={self._height})"
    
    def get_width(self):
        return self._width

    def get_height(self):
        return self._height
    
    def set_width(self, width):
        self._width = width

    def set_height(self, height):
        self._height = height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self._side = side

    def __str__(self):
        return f"Square (side={self._side})"

    def get_side(self):
        return self._side

    def set_side(self, side):
        self._side = side
        self._width = side
        self._height = side


class Circle(Shape):
    def __init__(self, radius):
        super().__init__() # Call the constructor of the base class.
        self._radius = radius

    def area(self):
        return math.pi * self._radius * self._radius

    def __str__(self):
        return f"Circle (radius={self._radius})"

    def get_radius(self):
        return self._radius

    def set_radius(self, radius):
        self._radius = radius

if __name__ == "__main__":
    rectangle = Rectangle(5, 10)
    square = Square(7)
    circle = Circle(3)

    shapes = [rectangle, square, circle]

    for shape in shapes:
        print(f"Area of {shape}: {shape.area()}")