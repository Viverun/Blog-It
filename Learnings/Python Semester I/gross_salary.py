#To calculate gross salary of an employee
#First let's ask the Base Salary from the user
base_salary = int(input("Enter the base salary please: "))
#Secondly calculate the allowances
dearness_allowance = 0.7*base_salary
travel_allowance = 0.3*base_salary
house_rent_allowance = 0.1*base_salary

gross_salary = dearness_allowance + travel_allowance + house_rent_allowance
#Display gross salary
print(f"The gross salary of the employee is {gross_salary:.2f}")