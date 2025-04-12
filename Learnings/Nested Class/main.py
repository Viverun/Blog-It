
class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position
        def get_details(self):
            return f"{self.name} is the {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []
    def add_Employee(self, name, position):
        new_Employee = self.Employee(name, position)
        self.employees.append(new_Employee)
    def list_Employee(self):
        return [employee.get_details() for employee in self.employees ]
company = Company("Krusty Krab")
print(company.company_name)
company.add_Employee("Eugene", "Manager")
company.add_Employee("Spongebob", "Cook")
company.add_Employee("Squidward", "Cashier")

for employee in company.list_Employee():
    print(employee)

new_company = Company("ChumBucket")
new_company.add_Employee("Sheldon", position = "Manager")
new_company.add_Employee("Karen", "Assistant")
for every_employee in new_company.list_Employee():
    print(every_employee)