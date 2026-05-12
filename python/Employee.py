
class Student:
    def __init__(self, id:int, name:str, marks:float):
        self.id = id
        self.name = name
        self.marks = marks

    def setID(self, id:int):
        self.id = id

    def setName(self, name:str):
        self.name = name
    
    def setMarks(self, marks:float):
        self.marks = marks
    
    def getInfo(self):
        return f"ID:{self.id} {self.name} with a score of {self.marks}"
    
    @staticmethod
    def getTopStudent(listofStudents):

        topStudent = listofStudents[0]

        for student in listofStudents:
            if student.marks > topStudent.marks:
                topStudent = student

        return topStudent

if __name__ == "__main__":
    list = [
        Student(1, "Eric Chen", 90.0),
        Student(2, "John Doe", 80.0),
        Student(3, "Jane Doe", 67.1),
        Student(4, "Little Timmy", 100)
    ]

    bestStudent = Student.getTopStudent(list)

    print(F"The top student is: {bestStudent.getInfo()}")

