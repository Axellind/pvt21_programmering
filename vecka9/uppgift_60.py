

class Student:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age


class Course:
    students = [Student]

    def __init__(self, name, code, students=[]):
        self.name = name
        self.code = code
        self.students = students

    def show_students(self):
        for s in self.students:
            print(f'{s.name} {s.last_name}, ålder: {s.age}')

    def add_student(self, li):
        for s in li:
            self.students.append(s)


class Teacher:
    name: str
    last_name: str
    age: int
    courses = [Course]

    def __init__(self, name, last_name, age, courses=[]):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.courses = courses

    def assign_course(self, course: Course):
        self.courses.append(course)

    def show_courses(self):
        for c in self.courses:
            print(f'Namn på kursen: {c.name}')

    def remove_course(self, course: Course):
        self.courses.remove(course)




first_student = Student('Axel', 'Lindström', 23)
second_student = Student('Anders', 'Andersson', 30)

python_course = Course('Python', 'PVT21')
python_course.show_students()

print()
python_course.add_student([first_student, second_student])
python_course.show_students()

first_teacher = Teacher('Björn', 'K', 40)
print(first_teacher.name)
print()

first_teacher.show_courses()
first_teacher.assign_course(python_course)
first_teacher.show_courses()

print('test', first_teacher.courses[0])
first_teacher.remove_course(python_course)
print('Nu har kursen tagits bort')
first_teacher.show_courses()
