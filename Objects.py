from student import student as Student

student1: Student = Student("Przemysław","Stokłosa")
student1.print()

Student.printId()

students: list = []

n = 10

for i in range(n):
    students.append(Student("Przemysław",f"Stokłosa_{i}"))

for student in students:
    student.print()

#dodajemy n studentów z numerowanymi nazwiskami
#wypisujemy ich pętlą
