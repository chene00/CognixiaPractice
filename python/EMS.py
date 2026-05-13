"""
Create a Department class with attributes deptID and name.
"""

class Department:
    def __init__(self, deptID:int, name:str):
        self.deptID = deptID
        self.name = name

"""
Create an Employee class with attributes id, name, salary, and dept. 
Add set methods to allow the user to change their attributes.
"""
class Employee:
    def __init__(self, id:int, name:str, salary:float, dept:Department):
        self.id = id
        self.name = name
        self.salary = salary
        self.dept = dept
        
    def setID(self, id:int):
        self.id = id
    
    def setName(self, name:str):
        self.name = name

    def setSalary(self, salary:float):
        self.salary = salary
    
    def setDepartment(self, dept:Department):
        self.dept = dept

"""
Print Employee function that prints all data for each employee in a list.
"""
def printEmployees(list):
    for emp in list:
        print(f"ID: {emp.id} Name: {emp.name} Salary: {emp.salary} Department: {emp.dept.deptID}")

"""
Modify an employee using kwargs for the parameters.
kwargs take any additional parameters and adds them into a dictionary
this dictionary can then be used to check whether or not a certain attribute is changed 
and if so set the employee attribute to the new attribute.
"""
def modifyEmployee(employee:Employee, **kwargs):
    if 'name' in kwargs:
        employee.setName(kwargs['name'])
    if 'salary' in kwargs:
        employee.setSalary(kwargs['salary'])
    if 'dept' in kwargs:
        employee.setDepartment(kwargs['dept'])

"""
Remove Employee function that removes a specific employee from a list.
"""
def removeEmployee(list, employee:Employee):
    for i, emp in enumerate(list):
        if emp.id == employee.id:
            list.pop(i)

"""
Print Department function that totals all employee that works in each department.
"""
def printDepartments(list):
    departments = {}

    for emp in list:
        if emp.dept.name in departments:
            departments[emp.dept.name] += 1
        else:
            departments[emp.dept.name] = 1    

    for (dept, value) in departments.items():
        print(f"{dept}: {value}")

"""
Check Department function that checks if two employees work in the same department
"""
def checkDepartment(emp1:Employee, emp2:Employee):
    if emp1.dept.deptID == emp2.dept.deptID:
        return True
    else:
        return False

if __name__ == "__main__":
    listofEmployees = []
    
    d1 = Department(20, "Legal")
    d2 = Department(10, "HR")
    d3 = Department(12, "Software")

    e1 = Employee(1, "Timmy Jones", 90000, d1)
    e2 = Employee(2, "John Doe", 45341, d1)
    e3 = Employee(3, "Jane Doe", 52342, d1)
    e4 = Employee(4, "Eric Chen", 23013, d1)
    e5 = Employee(5, "Johnathon Ham", 90000, d2)
    e6 = Employee(6, "Turkey Hen", 45341, d2)
    e7 = Employee(7, "Bob Jones", 52342, d3)

    listofEmployees.append(e1)
    listofEmployees.append(e2)
    listofEmployees.append(e3)
    listofEmployees.append(e4)
    listofEmployees.append(e5)
    listofEmployees.append(e6)
    listofEmployees.append(e7)

    printEmployees(listofEmployees)

    removeEmployee(listofEmployees, e3)
    e2.setName("Jimmy John")
    modifyEmployee(e4, name = "Harry Doe", salary =67000)

    print("New List:")
    printEmployees(listofEmployees)

    print("Departments:")
    printDepartments(listofEmployees)

    print(f"Does {e1.name} work with {e6.name} in the same department? Conclusion: {checkDepartment(e1, e6)}")

