from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def say(self):
         pass

    def run(self):
        return f' животное бежит'


class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def say(self):
        return f'мяу-мяу'

    def run(self):
        return f'{self.name} бежит'


class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        return f'вов-вов'

    def run(self):
        return f'{self.name} бежит'


cat = Cat('tom')
print(cat.run())
print(cat.say())
print('')
dog = Dog('dog', 4)
print(dog.say())
print(dog.run())