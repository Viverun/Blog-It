class Employee:
    companyName = "Apple"
    def __init__(self, name, ):
        self.name = name
        self.raise_amount = 0.02
    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount in {self.companyName} is {self.raise_amount}")

emp1 = Employee("Harry")
emp1.raise_amount = 0.3
emp1.companyName = "Apple India"
emp1.showDetails()
Employee.companyName = "Google"
# Employee.showDetails(emp1)
emp2 = Employee("Jelly")
emp2.companyName = "Nestle"
emp2.showDetails()

print(Employee.companyName)