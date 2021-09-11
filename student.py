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

    def print(self):
        pass

class persons_repository:
    persons_array: list

    def __init__(self):
        self.persons_array = []

    def addPerson(self, Person: person):
        self.persons_array.append(Person)

    def addPersons(self, personList: list):
        for person in personList:
            self.persons_array.append(person)

    def printStudents(self):
        print("------------------------------------")
        for Student in self.persons_array:
            Student.print()