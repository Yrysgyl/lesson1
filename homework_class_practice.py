#1
# class Taxi:
#     count_client = 0
#     total_money = 0
#
#     def __init__(self, order_number, money):
#         self.order_number = order_number
#         self.money = money
#         self.status = 'в ожидании'
#         Taxi.count_client += 1
#         Taxi.total_money += self.money
#
#     def change_status(self, new_status):
#         self.status = new_status
#
#     @staticmethod
#     def average_money():
#         return Taxi.total_money // Taxi.count_client
#
#     @staticmethod
#     def total_client():
#         return Taxi.count_client
#
#     @staticmethod
#     def total_salary():
#         return Taxi.total_money
#
#     def display_info(self):
#         print(f'Номер заказа: {self.order_number}\nСколько денег за за один заказ: {self.money}\nstatus: {self.status}')
#
#
# client1 = Taxi(1,200)
# client2 = Taxi(2,260)
# client2.change_status('go')
# client1.display_info()
#
# print(Taxi.total_client())
# print(Taxi.total_salary())
#
# print(Taxi.average_money())
#
#
#2
# class Pizza:
#     total_order = 0
#     def __init__(self, name, ingredient, price):
#         self.name = name
#         self.ingredient = ingredient
#         self.price = price
#         self.status = 'готовиться'
#         Pizza.total_order += 1
#
#     @staticmethod
#     def total_order_sum():
#         return Pizza.total_order
#
#     def new_status(self, new_status):
#         self.status = new_status
#
#     def inform_pizza(self):
#         print(f'name: {self.name}\tprice: {self.price}')
#         print('ingredient:')
#         for x in self.ingredient:
#             print(x)
#         print(f' status: {self.status}')
#
#
# pizza1 = Pizza('pepperoni', ['dough', 'sausage', 'cheese', 'tomato sauce'], 450)
#
# pizza1.inform_pizza()
# pizza1.new_status('готово')
#
# print(Pizza.total_order_sum())


#3
# class User:
#     total_person = 0
#     def __init__(self, username, password, age, address):
#         self.username = username
#         self.password = password
#         self.age = age
#         self.address = address
#         User.total_person += 1
#
#     @staticmethod
#     def my_username(username):
#         if username.isalnum() and len(username) >= 6:
#             return f'вы правильно ввели данные'
#         else:
#             return f'введите только буквы и цифры а также больше или равно  6 символов'
#
#     @staticmethod
#     def my_password(password):
#         if len(password) >= 8:
#             return f'вы правильно ввели пароль'
#         else:
#             return f'введите больше или равно 8 символов'
#
#     def inform(self):
#         print(f'username: {self.username}')
#         print('x' * len(self.password))
#         if self.age >= 18:
#             print(f'{self.username} годен для работы')
#         else:
#             print('вы не годны для работы')
#         if self.address == 'Bishkek':
#             print('Приходите на собеседование по адресу: Садырбаева 27')
#         else:
#             print(f'К сожелению у нас нет филиалов в вашем городе {self.address}')
#
#
# asel = User('asel', 'asellia7', 22, 'Bishkek')
# inna = User('inna', '12345678', 17, 'moskva')
# asel.my_username('asellia')
# asel.my_password('asel12345')
# asel.inform()
# inna.inform()
# print(User.total_person)


#4
class Bankaccount:
    def __init__(self, owner, percent, year, balance=0):
        self.owner = owner
        self.balance = balance
        self.percent = percent
        self.year = year

    def total_invest_money(self):
        return self.balance * (1 + self.percent / 100) ** self.year

    def income(self):
        return (self.balance * (1 + self.percent / 100) ** self.year) - self.balance
    def deposit(self, amount):
        self.balance += amount

    def take_of(self,amount):
        if amount > self.balance:
            return f' недостаточно средств'
        else:
            self.balance -= amount

    def check_balance(self):
        print(f' owner- {self.owner} :\t balance- {self.balance}')


# alisa = Bankaccount('alisa',10, 3, 1000)
# alisa.deposit(10000)
# alisa.check_balance()
# alisa.take_of(5000)
# alisa.check_balance()
# print(alisa.total_invest_money())
# print(alisa.income())






















