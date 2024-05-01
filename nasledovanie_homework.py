
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
# #
# cat = Animal('мурлычает')
# tom = Dog('tom')
#
#
# speak(cat)
# speak(tom)


class Animal:
    def speak(self):
        print('животное издает звук')


class Dog(Animal):

    def speak(self):
        print('собака лает')


#

# class Shape:
#     def __init__(self, area):
#         self.area = area
#
#     def aread(self):
#         return self.area
#
#
# class Rectangle(Shape):
#     def __init__(self, area, width, height):
#         super().__init__(area)
#         self.width = width
#         self.height = height
#
#     def aread(self):
#         return self.width * self.height
#
#
#
# squar = Rectangle(10, 6,9)
# print(squar.aread())





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


# squar = Rectangle(5, 10)
# print( squar.area())



# class Person:
#     def __init__(self, name):
#         self.name = name
# 
#     def display_name(self):
#         return self.name
# 
# 
# class Employee(Person):
#     def __init__(self, name, position):
#         super().__init__(name)
#         self.position = position
# 
#     def info_employee(self):
#         print(f'name: {self.name}, position: {self.position}')
# 
# 
# class Manager(Employee):
#     def __init__(self, name, position, department):
#         super().__init__(name, position)
#         self.department = department
# 
#     def display_info(self):
#         return f"{self.name} - {self.position} (Department: {self.department})"
# 
# 
# person = Person("Айгүл")
# print(person.display_name())  
# 
# employee = Employee("Эрмек", "Иш аткычы")
# print(employee.info_employee())  
# 
# manager = Manager("Гулжан", "Менеджер", "HR")
# print(manager.display_info())  # Гулжан - Менеджер (Department: HR)
# 
# 
