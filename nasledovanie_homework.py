
# class Animal:
#
#     def __init__(self, zvuk):
#         self.__zvuk = zvuk
#
#     @property
#     def zvuk(self):
#         return self.__zvuk
#
#     def say(self):
#         print(f"{self.__zvuk} животное издает звук")
#
#
#
# class Dog(Animal):
#
#     def dog_say(self):
#         print(" собака лает")
#
#
# def speak(pet):
#     if isinstance(pet, Dog):
#         print(pet.dog_say())
#     elif isinstance(pet, Animal):
#         print(pet.say())
#
#
# cat = Animal('мурлычает')
# tom = Dog('tom')
#
#
# speak(cat)
# speak(tom)


from abc import ABC, abstractmethod


# class Shape(ABC):
#     def area(self):
#         pass
#
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#
#
# squar = Rectangle(5, 10)
# print( squar.area())



class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        return self.name


class Employee(Person):
    def __init__(self, name, position):
        super().__init__(name)
        self.position = position

    def info_employee(self):
        print(f'name: {self.name}, position: {self.position}')


class Manager(Employee):
    def __init__(self, name, position, department):
        super().__init__(name, position)
        self.department = department

    def display_info(self):
        return f"{self.name} - {self.position} (Department: {self.department})"


# Тест кылуу
person = Person("Айгүл")
print(person.display_name())  # Айгүл

employee = Employee("Эрмек", "Иш аткычы")
print(employee.info_employee())  # Эрмек

manager = Manager("Гулжан", "Менеджер", "HR")
print(manager.display_info())  # Гулжан - Менеджер (Department: HR)


