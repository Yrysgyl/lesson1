# class Employee:
#     all_employees = 0
#     all_salary = 0
#
#     def __init__(self):
#         self.name = None
#         self.salary = None
#
#     def add_employee(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.all_employees += 1
#         Employee.all_salary += self.salary
#
#     def display_info(self):
#         print(f' name: {self.name}, salary: {self.salary}')
#
#     @staticmethod
#     def total_salary():
#         return Employee.all_salary
#
#     @staticmethod
#     def average_salary():
#         return Employee.all_salary // Employee.all_employees
#
#
# person1 = Employee()
# person2 = Employee()
# person3 = Employee()
# person1.add_employee('tom', 3000)
# person2.add_employee('sam', 4000)
# person3.add_employee('sara', 5000)
# person1.display_info()
# person2.display_info()
# person3.display_info()
# print("Total salary of all employees:", Employee.total_salary())
# print("Average salary of all employees:", Employee.average_salary())
#
#
#
#
#
# class User:
#     total_users = 0
#
#     def __init__(self, username, password):
#             self.username = username
#             self.password = password
#             User.total_users += 1
#
#     def display_info(self):
#         print(f"Username: {self.username}")
#         print({'*' * len(self.password)})
#
#     @staticmethod
#     def validate_username(username):
#         # Имя пользователя должно содержать только буквы и цифры, а также быть не короче 5 символов
#         if username.isalnum() and len(username) >= 5:
#             return True
#         else:
#             return False
#
#     @staticmethod
#     def validate_password(password):
#         # Пароль должен содержать не менее 8 символов
#         if len(password) >= 8:
#             return True
#         else:
#             return False
#
#
# user1 = User("john_doe", "strong_password123")
# # user2 = User("janes_mith", "password_8")
# #
# # user1.display_info()
# # user2.display_info()
# #
# # # print(f"Total users created: {User.total_users}")
# #
# # print("Username validation:", User.validate_username("john_doe"))
# # print("Password validation:", User.validate_password("strong_password123"))
# # user3 = User.total_users()