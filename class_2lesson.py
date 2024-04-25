# class Student:
#     def __init__(self, name, course, pol):
#         self.__name = name
#         self.__course = course
#         self.__pol = pol
#
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @property
#     def course(self):
#         return self.__course
#
#     @course.setter
#     def course(self, course):
#         self.__course = course
#
#     @property
#     def pol(self):
#         return self.__pol
#
#     @pol.setter
#     def pol(self, pol):
#         self.__pol = pol
#
#
# yrys = Student('Yrys', 4, 'girl')
# yrys.name = 'iris'
# print(yrys.name)
#



# class Person:
#     def init(self, name, age):
#         self.name = name  # устанавливаем имя
#         self.age = age  # устанавливаем возраст

#     @property
#     def age(self):
#         return self.age
#
#     @age.setter
#     def age(self, age):
#         if 0 < age < 110:
#             self.age = age
#         else:
#             print("Недопустимый возраст")
#
#     @property
#     def name(self):
#         return self.name
#
#     def print_person(self):
#         print(f"Имя: {self.name}\tВозраст: {self.age}")
#
#
# tom = Person("Tom", 39)
#
# tom.age = 111
# print(tom.age)



# """
# Инкапсуляция
#
# name
# __age
#
# @property - геттер
# @age.setter - сеттер
# @name.setter - сеттер
#
# """



class Person:
    def init(self, name, age):
        self.name = name  # устанавливаем имя
        self.age = age  # устанавливаем возраст

    def set_age(self, age):
        if 0 < age < 110:
            self.age = age
        else:
            print("Недопустимый возраст")

    def get_age(self):
        return self.age

    # геттер для получения имени
    def get_name(self):
        return self.name

    def print_person(self):
        print(f"Имя: {self.name}\tВозраст: {self.__age}")


tom = Person("Tom", 39)
tom.print_person()


tom.set_age(30)
tom.print_person()
print(tom.get_age())
print(tom.get_name())