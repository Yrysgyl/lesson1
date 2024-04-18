#1
# def check_divisbility(a):
#     if a % 10  != 0:
#         raise ValueError(f'{a} не делится на 10')
#     return a
# try:
#     print(check_divisbility(99))
# except ValueError as b:
#     print('ошибка', b)
# finally:
#     print('программа завершена')


#2
# def validate_input(x):
#     if not isinstance(x, int):
#         raise ValueError(f'{x} is not int type')
#     return x
# x = input('введите цифру: ')
# try:
#     print(validate_input(x))
# except ValueError as y:
#     print('ошибка', y)
# finally:
#     print('повторите попытку')


#3
# def check_length(z):
#     if len(z) > 10:
#         raise ValueError(f'длина {z} больше десяти')
#     return z
# z = input('Введите слово: ')
# try:
#     print(check_length(z))
# except ValueError as v:
#     print('попробуйте другое слово' , v)


#4
# def check_list(in_list):
#     if len(in_list) == 0:
#         raise ValueError('пустой список')
#     return in_list
# try:
#     print(check_list([]))
# except ValueError as f:
#     print('error', f)
# finally:
#     print('end')



#5
# try:
#     age = int(input('ваш возраст: '))
#     if age < 18:
#         raise PermissionError('Вам нельзя входить в бар! ')
#     print(age)
# except PermissionError as d:
#     print('error', d)



#6
# try:
#     number = int(input(''))
#     if number % 2 != 0:
#         raise ValueError('нечетное число')
#     print(number)
# except ValueError as g:
#     print('error', g)



#7
# try:
#     num = input('num: ')
#     if not isinstance(num, float):
#         raise ValueError('this float type')
#     print(num)
# except ValueError as h:
#     print('error', h)



#8
# try:
#     password = input('пароль: ')
#     if len(password) < 8:
#         raise ValueError('пароль слишком короткий!')
#     print(password)
# except ValueError as j:
#     print('error', j)



#9
# try:
#     email = input('введите email: ')
#     if '@' in email:
#         print(email)
#     else:
#         raise ValueError('пишите правильный адрес почты')
# except ValueError as l:
#     print('error', l)




