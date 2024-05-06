# class Circle:
#     counter = 0
#     def __init__(self, x=0, y=0, r=1):
#         Circle.counter +=1
#
#
# c = Circle()
# d = Circle()
# print(Circle.counter)
#


# class Segment:
#     counter = 0
#
#     def __init__(self, start = 0, finish = 0):
#         self.start = start
#         self.finish = finish
#         Segment.counter += 1
#
#     @classmethod
#     def how_many(cls):
#         return cls.counter
#
#
# s1 = Segment(2,6)
# s2 = Segment(5,3)
#
# print(Segment.how_many())
# print(s1.how_many())


# class Employee:
#     all_people = []
#
#     def __init__(self, name, salary):
#         self.salary = salary
#         self.name = name
#         Employee.all_people.append(self)
#
#
#     @staticmethod
#     def all_salary(self):
#         total = sum(emp.salary for emp in cls.all_people)
#         return total
#
#     @staticmethod
#     def average_salary():
#         total_emploee = len(cls.all_people)
#         average = cls.all_salary / cls


# class MathUtils:
#     @staticmethod
#     def factorial(n):
#         if n == 0:
#             return 1
#         else:
#             return n * MathUtils.factorial(n-1)
#
#
# print(MathUtils.factorial(5))


# class StringUtils:
#     @staticmethod
#     def is_palindrome(string):
#         return string == string[::-1]
#
#
# print(StringUtils.is_palindrome('oppo'))

# print(StringUtils.is_palindrome('rose'))

class Person:
    def __init__(self, age, name):
        self.age = age

    @staticmethod
    def is_adult(age):
        return age >= 18

    @staticmethod
    def palindrom(name):
        return name == name[::-1]


age = 12
is_adult = Person.is_adult(age)
print(is_adult)
name = Person(19, 'irri')
name.palindrom('tit')

