# from abc import ABC,abstractmethod
class Shape:
    # @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.1412* self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
         return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5* self.base * self.height

class Pizza(Circle):
    def __init__(self, toppings, radius):
        self.toppings = toppings
        # self.radius = radius
        super().__init__(radius)

shapes = [Circle(radius=10), Square(side=10),Triangle(10,10), Pizza("Pepperoni", radius = 20)]
for shape in shapes:
    print(f"The area is {shape.area()}cm\u00b2")

