# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#             Benefit = Add additional logic when read, write, or delete attributes
#             Gives you getter, setter and deleter method


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    @property
    def width(self):
        return f"{self._width:.lf}cm"
    @property
    def height(self):
        return f"{self._height:.lf}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._width = new_height
        else:
            print("Height must be greater than zero")
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")
    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")


rectangle = Rectangle(3,4)
rectangle.width = 6
rectangle.height = 10
# print(rectangle._width)
# print(rectangle._height)
del rectangle.width
del rectangle.height