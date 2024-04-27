# class Animal:
#     def __init__(self, name, age, color):
#         self.name = name
#         self.__age = age
#         self.color = color
#
#     @property
#     def age(self):
#         return self.age
#
#     def show_info(self):
#         print(f'{self.name}, {self.__age}, {self.color}')
#
# class Zebra(Animal):
#     def sey(self):
#         print('zebra alot')
#
# class Buka(Animal):
#
#     def byka(self):
#         print('bykyit')
#
# def erbol(animal):
#     if isinstance(animal, Animal):
#         animal.show_info()
#
#     elif isinstance(animal, Zebra):
#         animal.sey()
#
#     elif isinstance(animal, Buka):
#         animal.byka()
#
#
# animal = Animal('erbol', 20, 'yllow')
# zebra = Zebra('zebr', 10 , 'black')
# buka = Buka('bukka', 30, 'lrsfv')
#
# erbol(animal)
# erbol(zebra)
# erbol(buka)



class Animal:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f"{self.name} Animal")


class Zebra(Animal):
    def sey(self):
        print(f"{self.name} Zebra")


class Buka(Animal):

    def byka(self):
        print(f"{self.name} Buka")


def erbol(animal):
    if isinstance(animal, Zebra):
        animal.sey()

    elif isinstance(animal, Buka):
        animal.byka()

    elif isinstance(animal, Animal):
        animal.show_info()


animal = Animal('animal')
zebra = Zebra('zebra')
buka = Buka('buka')

erbol(animal)
erbol(zebra)
erbol(buka)