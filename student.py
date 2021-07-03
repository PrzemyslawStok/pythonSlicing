class student:
    name: str
    surname: str

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def print(self):
        print(f"name {self.name}, surname {self.surname}")

    @staticmethod
    def printId():
        print(10.0)


class students_repository:
    students_array: list

    def __init__(self):
        self.students_array = []

    def addStudent(self, students: student):
        self.students_array.append(student)

    def addStudents(self, students: list):
        for Student in students:
            self.students_array.append(Student)

    def printStudents(self):
        print("------------------------------------")
        for Student in self.students_array:
            pass
            #Student.print()


