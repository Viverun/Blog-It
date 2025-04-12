# class Employee:
#     def __init__(self):
#         self.__name="Jelly"
# a = Employee()
# # print(a.__name) Cannot be accessed directly but can be accessed inderectly
# print(a._Employee__name)
# print(a.__dir__())
# print(a.__module__)

class Student():
    def __init__(self):
        self._name = "Jello"
    def _function(self):
        return "Jelly is tasty"
class Subject(Student):
    pass
obj = Student()
obj1 = Subject()
print(obj._name)
print(obj._function())
print(obj1._name)
print(obj1._function())
print(obj.__dir__())
print(obj1.__dir__())

print(obj.__dir__)
print(dir(obj))