"""
1
Условные операторы:
Написать программу, которая будет делить введенные пользователем два вещественных числа и выводить результат на экран,
 сообщая об ошибке в случае деления на ноль.
"""
import random

# num1 = int(input('num1: '))
# num2 = int(input('num2: '))
# try:
#     print(num1 / num2)
# except ZeroDivisionError as a:
#     print('на ноль нельзя делить', a)
# except Exception:
#     print('ошибка')


# """
#2
# Определить, является ли введенное с клавиатуры натуральное число кратным трем. Вывести результат на экран"""
#
# number = int(input())
# if number % 3 == 0:
#     print(number % 3, 'число кратно трем')
# else:
#     print('не кратно трем')


# """
# 3
# Рассчитать стоимость покупки с учетом скидки в 35%, которая предоставляется покупателю, если сумма покупки превышает 20 у.е.
# Сумму покупки ввести с клавиатуры, а результаты округлить до сотых (копейки, центы и т.д.). Вывести на экран итоговую стоимость и размер предоставленной скидки"""
#
# purchase_amount = int(input())
# if purchase_amount > 20:
#     discount = purchase_amount * 0.35
#     print(f'сумма скидки: {discount}')
#     print(f'сумма без скидки: {purchase_amount} + {discount} = {purchase_amount + discount}')
# else:
#     print('без скидки')


"""
4
Напишите программу, которая будет проверять, является ли введенное пользователем значение цифрой десятичной системы счисления. 
В случае положительного результата, на экран пользователя должно выводиться название цифры, например, «3 - это три». 
В противном случае должно выводиться предупреждение «Введите цифру 10-й СС»"""

# user_num = input()
# if len(user_num) == 1 and user_num.isdigit():
#     num = int(user_num)
#     if 0 <= num <= 9:
#         if num == 0:
#             print(num, '- это ноль')
#         elif num == 1:
#             print(num, '-это один')
#
#         elif num == 2:
#             print(num, '-это два')
#
#         elif num == 3:
#             print(num, '-это три')
#
#         elif num == 4:
#             print(num, '-это четыре')
#
#         elif num == 5:
#             print(num, '-это пять')
#
#         elif num == 6:
#             print(num, '-это шесть')
#
#         elif num == 7:
#             print(num, '-семь')
#
#         elif num == 8:
#             print(num, '-восемь')
#
#         elif num == 9:
#             print(num, '-девять')
# else:
#     print('Введите цифру 10-й СС')


"""
5
Сформируйте список li из 10-ти случайных натуральных чисел не превышающих 100. Для этого используйте инструкции from random import randint и for k in range(1, 11): 
li.append(randint(1, 100)). Далее, используя для обхода элементов списка цикл for, выведите на экран: максимальное значение четных чисел, если их меньше, чем нечетных; 
максимальное значение нечетных чисел, если их меньше, чем четных; максимальное значение из двух, если в списке содержится равное количество четных и нечетных чисел. 
 для решения задачи другие встроенные функции запрещается
"""

from random import randint
random_list = [random.randint(1, 100) for k in range(1, 11)]
print(random_list)
count = 0
count_list = []
total = 0
total_list = []
for num in random_list:
    if num % 2 == 0:
        count_list.append(num)
        count += 1
    else:
        total_list.append(num)
        total += 1

if count > total:
    print('количество четных чисел много')
    print(max(count_list))

elif count < total:
    print('количество нечетных чисел много')
    print(max(total_list))

else:
    print('количество четных и нечетных равно')


