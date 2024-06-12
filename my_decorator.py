#1
# def select(input_func):
#     def output_func():
#         print('*****')
#         input_func()
#         print('******')
#     return output_func
#
#
# @select
# def hello():
#     print('hello world')
#
#
# hello()

#2
# def check(input_func):
#     def output_func(*args):
#         input_func(*args)
#
#     return output_func
#
#
# @check
# def print_person(name, age):
#     print(f'Name: {name}, age: {age}')
#
#
# print_person('tom', 34)
#
#3
# def decor1(func):
#     def wrapper():
#         print('this first print')
#         func()
#         print('this second print')
#     return wrapper
#
#
# @decor1
# def decor2():
#     print('this 3rd print in decor2')
#
#
# decor2()
#
#4
# def my_func(func):
#     def info(now):
#         print('morning')
#         func(now)
#         print('evening')
#     return info
#
#
# @my_func
# def full_info(now):
#     print(f'Сейчас {now}')
#
#
# full_info('обед')
#

#5
#import time


# def time_test(func):
#     def wrapper(*args):
#         start_time = time.time()
#         res = func(*args)
#         final_time = time.time()
#         time_in = final_time - start_time
#         print(f'время работы функции {time_in}')
#         return res
#     return wrapper
#
#
# @time_test
# def get1(a, b):
#     while a != b:
#         if a > b:
#             a -= b
#         else:
#             b -= a
#     return a
#
#
# @time_test
# def get2(a, b):
#     if a < b:
#         a, b = b, a
#     while b:
#         a, b = b, a % b
#     return a
#
#
# res = get1(2, 1000000)
# res2 = get1(2, 1000000)
# print(res, res2)






















#
