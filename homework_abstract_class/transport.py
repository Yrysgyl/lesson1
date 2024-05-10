"""
Допустим, вы разрабатываете программу для моделирования различных видов транспорта.
 Вам нужно создать абстрактный класс Transport, который будет представлять общие характеристики и методы для всех видов транспорта.
  Затем вы будете создавать конкретные классы для каждого типа транспорта, например, Car, Bicycle, Plane и т. д.

Вот что должен содержать абстрактный класс Transport:

Абстрактный метод move, который будет моделировать перемещение транспорта.
Абстрактный метод stop, который будет моделировать остановку транспорта.
Ваша задача состоит в том, чтобы создать абстрактный класс Transport и добавить абстрактные методы move и stop.
 Затем создайте несколько конкретных классов (например, Car, Bicycle, Plane) и реализуйте эти методы для каждого из них в соответствии с их поведением.
"""


from abc import ABC, abstractmethod


class Transport(ABC):

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Transport):

    def __init__(self, name):
        self.name = name
    def move(self):
        return f'{self.name} едет на четырех колесах по дорогам'

    def stop(self):
        return f'{self.name} останавливается через тормоз'


class Bycicle(Transport):

    def move():
        return f'едет на двух колесах'

    def stop():
        return f'останавливатся через тормоз'


class Plane(Transport):
    def move():
        return f'летит в воздухе'

    def stop():
        return f'приземляется на земле'


car = Car('car')
print(car.move())
print(car.stop())
print(car.name)

bycicle = Bycicle
print(bycicle.move())
print(bycicle.stop())

plane = Plane
print(plane.move())
print(plane.stop())

