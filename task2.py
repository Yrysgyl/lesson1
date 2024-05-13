class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn

    def get_title(self):
        return self.__title
    def set_title(self, title):
        self.__title = title
    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, isbn):
        self.__isbn = isbn


book1 = Book('Terror', 'den simmons', '397r65847')
print(book1.get_title())
print(book1.get_isbn())
print(book1.get_author())

book1.set_title('endimion')
print(book1.get_title())

book1.set_author('i dont know')
print(book1.get_author())

book1.set_isbn('23876')
print(book1.get_isbn())




class Publication:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print('name: ', self.title)
        print('author: ', self.author)
        print('year: ', self.year)

class Book(Publication):
    def __init__(self, title, author, year, isbn):
        super().__init__(title, author, year)
        self.isbn = isbn

    def display_info(self):
        super().display_info()
        print('Isbn: ',self.isbn)

class Magazine(Publication):
    def __init__(self, title, author, year, issue_number):
        super().__init__(title, author, year)
        self.issue_number = issue_number

    def display_info(self):
        super().display_info()
        print('Issue_number: ', self.issue_number)

book2 =  Book('chose', 'edit eger', 2019, '112-33')
magazine = Magazine('Time', 'collektiv', 2023, 5)

book2.display_info()
magazine.display_info()

import random
class MusicAlbum:
    def __init__(self, title, artist, release_year, genre, tracklist):
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.genre = genre
        self.tracklist = tracklist

    def play_track(self, track_number):
        print(f' Воспрооизводится трек: {track_number}: {self.tracklist[track_number-1]}')


    def play_random_track(self):
        track_number = random.randint(1, len(self.tracklist))
        self.play_track(track_number)


albom2 = MusicAlbum('life', 'Rammstein', 2019, 'Harte', ['radio', 'Diamint', 'Zeig dich'])
print(f'Название: {albom2.title}'
      f'\nartist: {albom2.artist}'
      f'\nrelease_year: {albom2.release_year}'
      f'\ngenre: {albom2.genre}'
      f'\ntrack_list: {albom2.tracklist}')
albom2.play_random_track()


class Student:
    def __init__(self, name, age, grade, scores):
        self.name = name
        self.age = age
        self.grade = grade
        self.scores = scores

    def average_score(self):
        return sum(self.scores) / len(self.scores)


stydent = Student('Tom', 20, 3, [3, 5, 2, 5, 5])
print(f'Имя: {stydent.name} '
      f'\tВозраст: {stydent.age}'
      f'\tКласс: {stydent.grade}'
      f'\tОценки: {stydent.scores}')
print('Cредний балл:', stydent.average_score())


class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def print_ingredients(self):
        print(f' Ингредиенты для {self.name}:')
        for ingredient in self.ingredients:
            print(f'-{ingredient}')

    def cook(self):
        print(f"Сегодня готовим {self.name}."
              f"\n Выполняем инструкцию по приготовлению блюда {self.name}..."
              f"\n Блюдо {self.name} готово")


spaghetti = Recipe('Спагетти', ['spagetti', 'фарш', 'cоус', 'лук'])
spaghetti.print_ingredients()

spaghetti.cook()



class Publisher:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def get_info(self):
        return f'{self.name} ({self.location})'

    def publish(self,message):
        print(f'Готовим "{message}"  к публикации в {self.get_info()}')

class BookPublisher(Publisher):
    def __init__(self, name, location,  num_authors):
        super().__init__(name, location)
        self.num_authors = num_authors

    def publish(self, title, author):
        print(f"Передаем рукопись '{title}', написанную автором {author} в издательство {self.get_info()}")


class NewspaperPublisher(Publisher):
    def __init__(self, name, location, num_pages):
        super().__init__(name, location)
        self.num_pages = num_pages

    def publish(self, headline):
        print(f'Печатаем свежий номер со статьей "{headline}" на главной странице в издательство {self.get_info()}')

publisher = Publisher('press', 'moskva')
publisher.publish('spravochnik')

book_publisher = BookPublisher('Math', 'Samara', 52)
book_publisher.publish('algoritm', 'chernyshev')

newspaper_publisher = NewspaperPublisher('vesti', 'moskva', 12)
newspaper_publisher.publish('Новая версия  Midjourney будет платной')

class BankAccount:
    def __init__(self, balance, interest_rate):
        self.__balance = balance
        self.__interest_rate = interest_rate
        self.__transactions = []

    def deposit(self,amount):
        self.__balance += amount
        self.__transactions.append(f'Внесение наличных на счет: {amount}')

    def withdraw(self, amount):
        if  self.__balance >= amount:
            self.__balance -= amount
            self.__transactions.append(f'Снятие наличных: {amount}')
        else:
            print(f'недастоточно средств на счете')

    def add_interest(self):
        interest = self.__balance * self.__interest_rate
        self.__balance += interest
        self.__transactions.append(f'Начислены проценты по вкладу : {interest}')

    def history(self):
        for transaction in self.__transactions:
            print(transaction)

account = BankAccount(100000, 0.05 )
account.deposit(15000)
account.withdraw(7500)
account.add_interest()
account.history()

class Employee:
    def __init__(self, name, age, salary, bonus):
        self.__name = name
        self.__age = age
        self.__salary = salary
        self.__bonus = 0

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_salary(self):
        return self.__salary

    def set_bonus(self, bonus):
        self.__bonus = bonus

    def get_bonus(self):
        return self.__bonus

    def get_total_salary(self):
        return self.__salary + self.__bonus


employee = Employee("ira", 30, 15000, 0)
employee.set_bonus(1000)

print('имя', employee.get_name())
print('возраст', employee.get_age())
print('зарплата', employee.get_salary())
print('Бонус', employee.get_bonus())
print('итиго зачислено', employee.get_total_salary())



class Candy:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self. weight = weight


class Chocolate(Candy):
    def __init__(self, name, price, weight, cocao_percentage, chocolate_type):
        super().__init__(name, price, weight)
        self.cocao_percentage = cocao_percentage
        self.chocolate_type = chocolate_type


class Gummy(Candy):
    def __init__(self, name, price, weight, flavor, shape):
        super().__init__(name, price, weight)
        self.flavor = flavor
        self.shape = shape


class HardCandy(Candy):
    def __init__(self, name, price, weight, flavor, filled):
        super().__init__(name, price, weight)
        self.flavor = flavor
        self.filled = filled


chocolate = Chocolate('albengold', 120, 250, 40, 'milk')
gummy = Gummy('marmelad', 75, 150, 'melon', 'ьедведь')
hard_candy = HardCandy('barbaris', 90, 250, 'mango', True)

print(chocolate.__dict__)
print(gummy.__dict__)
print(hard_candy.__dict__)


# try:
#     a = int(input('number: '))
#     b = int(input('number: '))
#     print(a/b)
#
# except ZeroDivisionError:
#     print('неудачно')
# print('завершение программы')


#
# try:
#     num = int(input('num: '))
#     print(num)
# except ValueError as e:
#     print('mistake', e)
# print('end')

try:
    num1 = int(input('num1:'))
    num2 = int(input('num2:'))
    if num2 == 0:
        raise Exception('не должно быть ноль')
    print( num1 / num2)
except ValueError:
    print('данные не корректны')
except Exception as e:
    print(e)
print('end')





























