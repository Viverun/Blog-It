class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'Not filled'}")


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
    def describe(self):
        super().describe()
        print(f"The area of circle is {3.1412*(self.radius**2)} sq-cm")
class Square(Shape):
    def __init__(self, color, is_filled,width):
        self.width = width
        super().__init__(color, is_filled)
    def describe(self):
        print(f"The area of square is {(self.width**2)} sq-cm")
        super().describe()


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

circle = Circle(color="red", is_filled=True, radius=5)
square = Square(color="blue", is_filled=False, width= 10)
triangle = Triangle(color="blue", is_filled=True, width= 10, height=30)
# print(triangle.color)
# print(triangle.is_filled)
# print(f"{triangle.width}cm")
# print(f"{triangle.height}cm")
# circle.describe()
square.describe()
# triangle.describe()
# square.describe()