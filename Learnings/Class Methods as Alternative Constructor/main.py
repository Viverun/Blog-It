class Employee:
    def __init__(self , name, salary):
        self.name = name
        self.salary = salary
    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], string.split("-")[1] )
        
e = Employee("Yum", 12000)
print(e.name)
print(e.salary)
string = "Harry-12000"
e = Employee.fromStr(string)
print(e.name)
print(e.salary)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))

person = Person.from_string("John Doe, 30")
print(person.name, person.age)
