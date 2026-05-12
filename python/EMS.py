class Department:
    def __init__(self, deptID:int, name:str):
        self.deptID = deptID
        self.name = name

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

def printEmployees(list):
    for emp in list:
        print(f"ID: {emp.id} Name: {emp.name} Salary: {emp.salary} Department: {emp.dept.deptID}")

def removeEmployee(list, employee:Employee):
    for i, emp in enumerate(list):
        if emp.id == employee.id:
            list.pop(i)

def printDepartments(list):
    departments = {}

    for emp in list:
        if emp.dept.name in departments:
            departments[emp.dept.name] += 1
        else:
            departments[emp.dept.name] = 1    

    for (dept, value) in departments.items():
        print(f"{dept}: {value}")

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

    print("New List:")
    printEmployees(listofEmployees)

    print("Departments:")
    printDepartments(listofEmployees)

    print(f"Does {e1.name} work with {e6.name} in the same department? Conclusion: {checkDepartment(e1, e6)}")

