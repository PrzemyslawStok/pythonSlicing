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
        pass
    def addStudent(array: list, students: student):
        pass
    def addStudents(array: list, students: list):
        pass
    def printStudents(self):
        pass
    pass