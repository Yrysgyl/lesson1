from abc import ABC, abstractmethod

class School(ABC):
    count_people = 0
    list_names = []
    teacher_names = []

    def __init__(self):
        School.count_people += 1

    @abstractmethod
    def add_student():
        pass

    @abstractmethod
    def add_teacher():
        pass


class OurClass(School):

    def __init__(self, count_class, teacher, subject):
        super().__init__()
        self.count_class = count_class
        self.teacher = teacher
        self.subject = subject

    def add_student(name):
        School.list_names.append(name)
        print(School.list_names)

    def add_teacher(name_teacher):
        School.teacher_names.append(name_teacher)
        print(School.teacher_names)

    def __str__(self):
        return f'Номер класса: {self.count_class}, имя учителя: {self.teacher}, предмет: {self.subject}'


# class_1 = OurClass(9, 'cholpon', 'english')
# print(class_1)
# class_1.add_student('iris')
# class_1.add_teacher('mirra')


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False

    def check_out(self):
        if self.checked_out:
            print('книга находится у тебя')
        else:
            self.checked_out = True
            print('Выдаем книгу абоненту')

    def check_in(self):
        if not self.checked_out:
            print('книга в наличии')
        else:
            self.checked_out = False
            print('Принимаем книгу в библиотеку.')


book1 = Book('Мир', 'tolstoi', '978-0743273665')
book1.check_out()
book1.check_out()
book1.check_in()
book1.check_in()


# import math
# class Shape:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#     def describe(self):
#         print(f'Это геометрическая фигура, цвет {self.color}.')
#
#
# class Circle(Shape):
#     def __init__(self, name, color, radius):
#         super().__init__(name, color)
#         self.radius = radius
#
#     def area(self):
#         return math.pi * self.radius ** 2
#
#     def describe(self):
#         super().describe()
#         print(f'Это окружность. Радиус - {self.radius} см, цвет - {self.color}')
#
#
# class Rectangle(Shape):
#     def __init__(self, name, color, length, width):
#         super().__init__(name, color)
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.width * self.length
#
#     def describe(self):
#         super().describe()
#         print(f'Это {self.color} прямоугольник. Длина - {self.length} см, ширина - {self.width}')
#
# class Triangle(Shape):
#     def __init__(self, name, color, base, height):
#         super().__init__(name, color)
#         self.base = base
#         self.height = height
#
#     def area(self):
#         return self.base * self.height * 0.5
#
#     def describe(self):
#         super().describe()
#         print(f'Это {self.color} треугольник с основанием {self.base} см, и высотой {self.height} см.')
#
#
# circle = Circle('circle', 'red', 5)
# rectangle = Rectangle('rect', 'blue', 4, 5)
# triangle = Triangle('trio', 'white', 6, 4)
#
# circle.describe()
# rectangle.describe()
# triangle.describe()
# print(f'Площадь треугольника {triangle.area()}, окружности {circle.area()}, прямоугольника {rectangle.area()}')

