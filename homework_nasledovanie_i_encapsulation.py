class Employee:
    def __init__(self, name, age, email, local):
        self.__name = name
        self.__age = age
        self.__email = email
        self.__local = local

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_email(self):
        return self.__email

    def get_local(self):
        return self.__local
    def display_info(self):
        print(f'имя : {self.__name}'
              f'\tвозраст : {self.__age}'
              f'\tэлектронный адрес : {self.__email}'
              f'\tместо жительства : {self.__local}')


class Manager(Employee):
    def __init__(self, name, age, email, local, salary):
        super().__init__(name, age, email, local)
        self.salary = salary

    def display_info(self):
        super().display_info()
        print(f'зарплата: {self.salary}')


class Developer(Employee):
    def __init__(self, name, age, email, local):
        super().__init__(name, age, email, local)


    def display_info(self):
        super().display_info()


class Designer(Employee):
    def __init__(self, name, age, email, local):
        super().__init__(name, age, email, local)

    def display_info(self):
        super().display_info()


employee = Employee('tom', 23, '@tom', 'osh')
employee.display_info()

manager = Manager('Ira', 21, '@ira', 'bishkek', 25000)
manager.display_info()

developer = Developer('Sam', '25', '@sam', 'Talas')
developer.display_info()

designer = Designer('iris', 26, '@iris', 'moskva')
designer.display_info()

