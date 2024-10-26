# A program to demonstrate the power of polymorphism.
class Shape:
    def __init__(self):
        pass

    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__()
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length


rectangle_1 = Rectangle(2, 3)
square_1 = Square(9)
print(rectangle_1.area())
print(square_1.area())
