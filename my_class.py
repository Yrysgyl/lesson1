"""
Домашнее задание 1
Задание № 1
Изучите самостоятельно чем отличается атрибут класса от атрибута экземпляра класса? Как можно просмотреть все атрибуты и методы объекта?
В чем разница между функцией dir() и dict?
Задание № 2
Изучите, что значит public, private и protected атрибуты и методы в ООП Python.
Задание № 3
Представьте, что вы работаете над разработкой видеоигры. Вам нужно прописать классы для персонажей игры.
Создайте класс Эльфов. Опишите атрибуты Эльфов: количество глаз, рук, ног, цвет волос и т.д. Придумайте, что хотите. Также у Эльфов должно быть: имя,
тип лука, которым он пользуется (по-умолчанию деревянным, еще он может быть алюминиевым или карбоновым),  племя в котором он состоит,  количество стрел,
господин, которому он служит.
По-умолчанию, специальность у Эльфов лучник, но они могут переквалифицироваться в снайперов.
Как и у любого воина, у Эльфа должен быть ранг. В самом начале он является Эльфом 1 ранга. Это самый низкий ранг. Самый высокий - 5.
Так как он воин, он не может раскрывать имя своего господина и свое оружие (лук и количество стрел). Поэтому эти параметры не могут быть публичными.
Эльфы должны уметь приветствовать своего господина и улучшать свои навыки, увеличивая свой ранг. Если ранг достигает 5 уровня,
он становится снайпером. Напишите методы greeting и improve для этого. Также напишите методы для увеличения и уменьшения количества стрел.
Задание № 4
Создайте класс Волшебников. Опишите атрибуты Волшебников: количество глаз, рук, ног, цвет волос и т.д. Придумайте, что хотите. Также у Волшебников должно быть:
 имя, отряд,  стихия (огонь, вода, земля или воздух),  оружие (посох, волшебная палочка, зачарованный кристалл и т.п.),
количество маны (мана - это энергия, которая необходима для волшебства) господин, которому он служит.
По-умолчанию, специальность у Волшебников маг, но они могут переквалифицироваться в архимагов.
Как и у любого воина, у мага должен быть ранг. В самом начале он является Магом 1 ранга. Это самый низкий ранг. Самый высокий - 5.
Так как он воин, он не может раскрывать имя своего господина и свое оружие. Поэтому эти параметры не могут быть публичными.
Волшебники должны уметь приветствовать своего господина и улучшать свои навыки, увеличивая свой ранг. Если ранг достигает 5 уровня,
он становится архимагом. Напишите методы greeting и improve для этого. Также напишите методы для увеличения и уменьшения количества маны.
"""


class Hero:
    eyes_count = 2
    hand_count = 2
    legs_count = 2

    def __init__(self, name, sir):
        self.name = name
        self._sir = sir

    def greeting(self):
        pass

    def improve(self):
        pass


class Bow:
    WOODEN = 'wooden'
    ALUMINIUM = 'aluminium'
    CARBON = 'carbon'


class Arms:
    WAND = 'палочка'
    STAFF = 'посох'
    CRYSTAL = 'зачарованный кристалл'


class Element:
    FIRE = 'fire'
    WATER = 'water'
    AIR = 'air'
    EARTH = 'earth'


class Elves(Hero):

    def __init__(self, name,  sir, count_arrow):
        super().__init__(name, sir)
        self.__count_arrow = count_arrow
        self.color_hair = 'black'
        self.bow_type = Bow.WOODEN
        self.breed = 'племя - "sun"'
        self.rang = 1
        self.speciality = 'лучник'

    def get_sir(self):
        return self._sir

    def set_sir(self, sir):
        self._sir = sir

    def get_count_arrow(self):
        return self.__count_arrow

    def set_count_arrow(self, arrow):
        self.__count_arrow = arrow

    def greeting(self):
        return f' Приветствую вас гасподин {self._sir}'

    def improve(self):
        if self.rang < 5:
            self.rang += 1

        elif self.rang == 5:
            self.speciality = 'снайпер'
            self.bow_type = Bow.ALUMINIUM
            return f' вы стали - {self.speciality}, ваш тип лука - {self.bow_type}, ваш ранг - {self.rang}'
        return self.speciality

    def add(self, new_count_arrow):
        self.__count_arrow += new_count_arrow
        return self.__count_arrow

    def decrease(self, count_arrow):
        self.__count_arrow -= count_arrow
        return self.__count_arrow

    def __str__(self):
        return (f'цвет волос - {self.color_hair}, имя - {self.name}, тип лука - {self.bow_type}, племя - {self.breed}, '
                f'количество лука - {self.__count_arrow}, имя гасподина - {self._sir}, ранг - {self.rang}, специальность - {self.speciality}')


elf_1 = Elves('irina', 'selena', 20)
print(elf_1)
print(elf_1.greeting())
print(elf_1.add(9))
print(elf_1.decrease(4))
print(elf_1.improve())
print(elf_1.improve())
print(elf_1.improve())
print(elf_1.improve())
print(elf_1.improve())
elf_1.set_sir('samara')
print(elf_1.get_sir())
elf_1.set_count_arrow(15)
print(elf_1.get_count_arrow())
print(elf_1)



class Magic(Hero):

    def __init__(self, name, sir,   squad):
        super().__init__(name, sir)
        self.squad = squad
        self.element = Element.FIRE
        self.__weapon = Arms.WAND
        self.count_mana = 20
        self.rang = 1
        self.speciality = 'mag'

    def get_sir(self):
        return self._sir

    def set_sir(self, sir):
        self._sir = sir

    def get_weapon(self):
        return self.__weapon

    def set_weapon(self, weapon):
        self.__weapon = weapon

    def greeting(self):
        return f' {self.name} приветсвует своего господина {self._sir}'

    def improve(self):
        if self.rang < 5:
            self.rang += 1
        elif self.rang == 5:
            self.speciality = 'arhimag'
            self.__weapon = Arms.STAFF
            return f'максимальный уровень {self.rang}, он теперь {self.speciality}, оружие - {self.__weapon}'
        return f'уровень ранг {self.rang}'

    def add(self, new_mana_count):
        self.count_mana += new_mana_count
        return self.count_mana

    def decrease(self, new_mana_count):
        self.count_mana -= new_mana_count
        return self.count_mana

    def __str__(self):
        return (f'имя волшебника - {self.name},'
                f'\nотряд - {self.squad}, '
                f'\nстихия - {self.element}, '
                f'\nоружие - {self.__weapon}, '
                f'\nколичество маны - {self.count_mana}, '
                f'\nимя гасподина - {self._sir}, '
                f'\nранг - {self.rang}, '
                f'\nспециальность волшебника - {self.speciality}')


mag1 = Magic('lia',  'andreas', 'wizard')
# print(mag1)
# print(mag1.greeting())
# print(mag1.improve())
# print(mag1.improve())
# print(mag1.improve())
# print(mag1.improve())
# print(mag1.improve())
# print(mag1.add(50))
# print(mag1.decrease(30))
# print(mag1)
# mag1.set_sir('tiran')
# print(mag1.get_sir())
# mag1.set_weapon(Arms.CRYSTAL)
# print(mag1.get_weapon())