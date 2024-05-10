from abc import ABC, abstractmethod


class Course(ABC):
    def __init__(self, name, teacher, credits):
        self.name = name
        self.teacher = teacher
        self.credits = credits
        self.students = []

    @abstractmethod
    def add_student(self, student):
        pass

    @abstractmethod
    def grade_student(self, student, grade):
        pass


class Student:
    def __init__(self, first_name, last_name, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.courses = []

    def register_to_course(self, course):
        self.courses.append(course)
        course.add_student(self)

    def get_average_grade(self):
        total_grades = 0
        total_courses = 0
        for course in self.courses:
            for student in course.students:
                if student.student_id == self.student_id:
                    total_grades += student.grade
                    total_courses += 1
        if total_courses == 0:
            return 0
        return total_grades / total_courses


class University:
    def __init__(self):
        self.courses = []
        self.students = []

    def add_course(self, course):
        self.courses.append(course)

    def register_student_to_course(self, student, course):
        student.register_to_course(course)

    def grade_student(self, student, course, grade):
        for c in self.courses:
            if c.name == course.name:
                c.grade_student(student, grade)


class ConcreteCourse(Course):
    def add_student(self, student):
        self.students.append(student)

    def grade_student(self, student, grade):
        for s in self.students:
            if s.student_id == student.student_id:
                s.grade = grade
                break


if __name__ == "__main__":
    university = University()

    course1 = ConcreteCourse("Математика", "Иванов", 3)
    course2 = ConcreteCourse("Физика", "Петров", 4)

    university.add_course(course1)
    university.add_course(course2)

    student1 = Student("Иван", "Иванов", 1)
    student2 = Student("Петр", "Петров", 2)

    university.register_student_to_course(student1, course1)
    university.register_student_to_course(student1, course2)
    university.register_student_to_course(student2, course1)

    university.grade_student(student1, course1, 4.5)
    university.grade_student(student1, course2, 3.8)
    university.grade_student(student2, course1, 4.0)

    print(f"Средняя оценка студента {student1.first_name} {student1.last_name}: {student1.get_average_grade()}")
    print(f"Средняя оценка студента {student2.first_name} {student2.last_name}: {student2.get_average_grade()}")