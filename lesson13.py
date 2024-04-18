# def num(a):
#     if a < 0:
#         raise Exception('меньше нуля')
#     print(a)
# try:
#     num(1)
# except Exception as e:
#     print('error', e)


# def num(x,y):
#     if not (isinstance(x,float)) and (isinstance(y,float)):
#         raise TypeError('должно быть int')
#     return x + y
# try:
#     print(num(1,9))
# except TypeError as a:
#     print('error', a)

# def num(a,b):
#     if b == 0:
#         raise ZeroDivisionError('не должно быть равно нулю')
#     return a / b
# try:
#     print(num(3,2))
# except ZeroDivisionError as c:
#     print('ошибка', c)


# def num(a):
#     if not isinstance(a, int):
#         raise TypeError('not int')
#     if a % 2 != 0:
#         raise ValueError('не int')
#     return a
# try:
#     print(num(4))
#     print(a[5])
# except TypeError as d:
#     print('ощибка не int', d)
# except ValueError as b:
#     print('делится без остатка на 2', b)
# except Exception as z:
#     print('другие ошибки', z)


# def num(a,b):
#     if a > 100:
#         raise Exception(f'error1 {a} не больше 100')
#     if b > 200:
#         raise Exception(f'error {b} < 200')
# try:
#     num(90, 205)
# except Exception as s:
#     print('ошибка', s)
# finally:
#     print('the end')







