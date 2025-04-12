# class Math:
#     def __init__(self, num):
#         self.num = num
#     def addtonum(self,n):
#         self.num = self.num + n
#
#     @staticmethod
#     def add(a,b):
#         return a + b
#
# a = Math(5)
# print(a.num)
# a.addtonum(6)
# print(a.num)

#Static Method = A method that usually belong to a class rather than any object from that class(instance)
#                Used for general utility functions that do not need access to class data
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} {self.position}"
    @staticmethod
    def is_valid_position(position):
        valid_position = ["Manager", "Cook", "Janitor"]
        return position in valid_position
print(Employee.is_valid_position("Cook"))
print(Employee.is_valid_position("Free Loader"))
employee = Employee("Jelly", "Food")
print(employee.get_info())