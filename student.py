class person:
    name: str
    surname: str
    height: float

    def __init__(self, name, surname, height=175):
        self.name = name
        self.surname = surname
        self.height = height

    def print(self):
        print(f"name {self.name}, surname {self.surname}, height {self.height}")

    @staticmethod
    def printId():
        print(10.0)


class student(person):
    def __init__(self, name, surname, height=177):
        super().__init__(name, surname, height)

    @staticmethod
    def printId():
        pass
        # person.printId()

class teacher(person):
    lecture: str
    def __init__(self,name,surname,height,lecture):
        super().__init__(name,surname,height)
        self.lecture = lecture

class students_repository:
    students_array: list

    def __init__(self):
        self.students_array = []

    def addStudent(self, Student: student):
        self.students_array.append(Student)

    def addStudents(self, students: list):
        for Student in students:
            self.students_array.append(Student)

    def printStudents(self):
        print("------------------------------------")
        for Student in self.students_array:
            Student.print()