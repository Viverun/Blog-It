# class Employee:
#     company = "Apple"
#     def show(self):
#         print(f"The name is {self.name} and the company is {self.company}")
#     @classmethod
#     def changeCompany(cls, newCompany):
#         cls.company = newCompany
# e1 = Employee()
# e1.name = "Yum_Yum"
# e1.show()
# e1.changeCompany("Tesla")
# e1.show()
# print(Employee.company)


# Allows operations related to class itself
# Take first parameter as cls which represent class itself
class Student:
    count = 0
    total_gpa = 0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # This is an instance method
    def get_info(self):
        return f"{self.name}{self.gpa}"


    @classmethod
    def get_count(cls):
        return f"The total number of student is: {cls.count}"
    @classmethod
    def get_avg_gpa(cls):
        return f"The average gpa of students out of 4 is {cls.total_gpa/cls.count:.2f}"
student1 = Student("SpongeBob", 3.3)
student2 = Student("Squidward", 3.4)
student3 = Student("Sandy", 4.0)
print(Student.get_count())
print(Student.get_avg_gpa())


