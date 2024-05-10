"""
Курс
Представьте, что вы создаете систему управления учебным планом для университета.
Ваша система должна иметь возможность хранить информацию о курсах и студентах, а также выполнять различные операции,
такие как добавление нового курса, регистрация студента на курс, оценка студента и т. д.
Вам нужно создать следующие классы:
Абстрактный класс Course, который представляет курс в университете.
 У курса должны быть атрибуты, такие как название курса, преподаватель, количество кредитов и список зарегистрированных студентов.
 Также должны быть реализованы абстрактные методы для добавления студента на курс и выставления оценки студенту.
Класс Student, представляющий студента в университете.
У студента должны быть атрибуты, такие как имя, фамилия, номер студенческого билета и список курсов, на которые он зарегистрирован.
 Также должны быть реализованы методы для регистрации студента на курс и получения его средней оценки.
Класс University, который будет представлять университет и хранить информацию о всех курсах и студентах.
 Этот класс должен иметь методы для добавления нового курса, регистрации студента на курс, выставления оценки студенту и т. д.
Реализуйте эти классы и их методы таким образом, чтобы они соответствовали описанным требованиям.
"""

from abc import ABC, abstractmethod

class Course(ABC):
    name_course = ''
    teacher = ''
    count_credit = 0
    all_students = []

    def __init__(self):
        pass


    @abstractmethod
    def add_stydent(self):
        pass

    @abstractmethod
    def grade(self):
        pass

class Student(Course):

    def __init__(self, name, surname, id_number, list_course):
        super().__init__()
        self.name = name
        self.surname = surname
        self.id_number = id_number
        Course.name_course.append(list_course)

    def add_stydent(self, name):
        Course.all_students.append(name)
        return Course.all_students

    def grade(self, grade):
        return sum(grade)/len(grade)

    def __str__(self):
        return f'name: {self.name}, surname: {self.surname}, id: {self.id_number}'


class Univercity(Course):

    def add_new_course(new_course):
        Course.name_course += new_course
        return Course.name_course

    def add_stydent(name):
        Course.all_students += name
        return Course.all_students

    def grade_student(student, course, grade):
        return f'student: {student}, course: {course}, grade: {grade}'

# stydent = Student('iris', 'talantbekova', 23, ['math', 'biology', 'geogrphy'])
# print(stydent.add_stydent('rita'))
# print(stydent.grade([5,5,4]))
# print(stydent)

univer = Univercity
print(univer.add_new_course('algebra'))
print(univer.add_stydent('daniel'))
print(univer.grade_student('dasha', 'math', 5))