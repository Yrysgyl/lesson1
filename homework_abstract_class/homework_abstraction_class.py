

from abc import ABC, abstractmethod

class Course(ABC):

    def __init__(self, name_course, teacher, count_credit):
        self.name_course = name_course
        self.teacher = teacher
        self.count_credit = count_credit
        self.students = []


    @abstractmethod
    def add_student(self,student):
        self.students.append(student)
        return self.students

    @abstractmethod
    def assign_grade(self, student, grade):
        return f'{self.name_course}-{student}:{grade}'

    def __str__(self):
        return f' {self.name_course}, {self.students}, {self.teacher}, {self.count_credit}'

class Student(Course):
    def __init__(self, name, surname, id_number, name_course, teacher, count_credit):
        super().__init__(name_course, teacher, count_credit)
        self.name = name
        self.surname = surname
        self.id_number = id_number
        self.courses_list = []

    def __str__(self):
        return f' {self.name_course}, {self.students}, {self.teacher}, {self.count_credit}, {self.name}, {self.surname}, {self.id_number},{self.courses_list}'

    def add_student(self,student):
        self.students.append(student)

    def assign_grade(self, grade):
        return sum(grade)/len(grade)


class Univer:
    courses_list = []
    def add_new_course(self,new_course):
        self.courses_list.append(new_course)
        print(self.courses_list)

    def regist(self, new_student):
        self.students.append(new_student)
        print(self.students)
    def graduete(self, student, course, grade):
        return f'{student} - {course}: {grade}'


# course = Course('math','lola', 7)
# print(course.add_student('ilon'))
# print(course.assign_grade('ira', [5]))
# print(course)
# print('--------')

student = Student('lola', 'tinova', 231, 'algebra', 'inna', 4)
print(student.add_student('maria'))
print(student.assign_grade([5, 5]))
print(student)
print('---------')

# univer = Univer('iris','ilonova', 3, 'biology', 'yrys', '5')
# univer.add_new_course('english')
# print(univer.graduete('lola', 'math', 5))
# univer.regist('sam')
