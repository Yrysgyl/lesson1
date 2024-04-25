# class BankovskiiChet:
#     def __init__(self, balance, owner):
#         self.__balance = balance
#         self.__owner = owner
#
#
#     def set_owner(self, owner):
#         self.__owner = owner
#
#     def get_owner(self):
#         return self.__owner
#
#     def get_balance(self):
#         return self.__balance
#
#
#     def info(self):
#         print(f'Balance: {self.__balance}\t Owner: {self.__owner}')
#
# yrys =BankovskiiChet(9000, 'yrys')
# yrys.info()
# yrys.set_owner('iris')
# yrys.info()
#
# class User:
#     def __init__(self, name, age, email):
#         self.__name = name
#         self.__age = age
#         self.__email = email
#
#     def set_name(self,name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#
#     def set_email(self,email):
#         self.__email = email
#
#     def get_name(self):
#         return self.__email
#
#
#     def get_age(self):
#         return self.__age
#
#     def about_user(self):
#         print(f'Name: {self.__name}\t Age: {self.__age}\t Email: {self.__email}')
#
# rabah = User('Rabah', 8, '@rabah5' )
# rabah.about_user()
# rabah.set_name('yrys')
# rabah.set_email('@iris6')
# rabah.about_user()


class Product:
    def __init__(self, name, price, count):
        self.__name = name
        self.__price = price
        self.__count = count

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_count(self, count):
        self.__count = count

    def get_count(self):
        return self.__count

    def about_product(self):
        print(f' Name: {self.__name}\t Price: {self.__price}\t Count:{self.__count}')
              
    
sugar = Product('sugar', 100, 60)
sugar.about_product()
sugar.set_name('bread')
sugar.set_price(30)
sugar.set_count(15)
sugar.about_product()