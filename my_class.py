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


class Elves:
    eyes_count = 2
    hand_count = 2
    legs_count = 2

    def __init__(self, color_hair, name, bow_type, breed, count_arrow, sir):
        self.color_hair = color_hair
        self.name = name
        self.bow_type = 'деревянный'
        self.breed = breed
        self.__count_arrow = count_arrow
        self.__sir = sir
        self.rang = 1
        self.speciality = 'лучник'

    def greeting(self):
        return f' Приветствую вас гасподин {self.__sir}'

    def improve(self):
        if self.rang == 5:
            self.speciality = 'снайпер'
            return self.speciality
        else:
            return self.speciality

    def change_arrow(self, arrow):
        self.__count_arrow = arrow
        return self.__count_arrow

    def __str__(self):
        return (f'цвет волос - {self.color_hair}, имя - {self.name}, тип лука - {self.bow_type}, племя - {self.breed}, '
                f'количество лука - {self.__count_arrow}, имя гасподина - {self.__sir}, ранг - {self.rang}, специальность - {self.speciality}')


# elf_1 = Elves('black', 'iris', 'деревянный', 'bugu', 15, 'sirius')
# print(elf_1.greeting())
# print(elf_1.change_arrow(45))
# print(elf_1.improve())
# print(elf_1)

class Magic:
    count_eyes = 2
    count_hands = 2
    count_legs = 2

    def __init__(self, name_magic, squad, element, weapon, count_mana, sir_mag, rang):
        self.name_magic = name_magic
        self.squad = squad
        self.element = element
        self.__weapon = weapon
        self.count_mana = count_mana
        self.__sir_mag = sir_mag
        self.rang_mag = 1
        self.spec_mag = 'mag'

    def greeting(self):
        return f' {self.name_magic} приветсвует своего господина {self.__sir_mag}'

    def improve(self):
        if self.rang_mag == 5:
            self.spec_mag = 'arhimag'
            return self.spec_mag
        else:
            return self.spec_mag

    def change_mana(self,new_mana_count):
        self.count_mana = new_mana_count
        return self.count_mana

    def __str__(self):
        return (f'имя волшебника - {self.name_magic},'
                f'отряд - {self.squad}, '
                f'стихия - {self.element}, '
                f'оружие - {self.__weapon}, '
                f'количество мпны - {self.count_mana}, '
                f'имя гасподина - {self.__sir_mag}, '
                f'ранг - {self.rang_mag}, '
                f'специальность волшебника - {self.spec_mag}')


mag1 = Magic('lia', 4, 'water', 'посох', 20, 'andreas', 1)
print(mag1)
print(mag1.greeting())
print(mag1.improve())
print(mag1.change_mana(60))
