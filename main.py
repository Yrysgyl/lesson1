# def upper_all(x):
#     print( x.upper())
#
# upper_all('father')
#
#
# def obratnui_poriadok(z):
#     print(z[::-1])
#
# obratnui_poriadok('my life is pretty')
import random
# def is_palindrom(a):
#    a=a.lower()
#    return a==a[::-1]
# #a=input('str: ')
# print(is_palindrom('ata'))


# def replace_s(k):
#     print(k.replace('.' , '!'))
# replace_s('yrys...')

#
# def bukva(n):
#     print(sum([1 for x in n.lower() if x in 'уеыаоэяию']))
#     print( sum([1 for z in n.lower() if z in 'йцкнгшщзхъфвпрлджчсмтб']))
# bukva('адил')


# def capitalize_words(v):
#     #print(s= ' '.join(word.capitalize() for word in v.split()))
#     v=v.title()
#     print(v)
# capitalize_words('sun shine ')


# def snake_case(b):
#     b=b.replace(' ','_')
#     return b
# b=input('str: ')
# print(snake_case(b))

# word1=input('str1: ')
# word2=input('str2: ')
# print(word1+'_'+word2)

# symbol=input('str: ')
# a1=symbol.count(',')
# a2=symbol.count('.')
# a3=symbol.count('?')
# a4=symbol.count('!')
# print(a1+a2+a3+a4)
# print(len(symbol))

# a=int(input('длина см: '))
# b=int(input('ширина см: '))
# print(a*b)
#
# name=input('name: ')
# age=input('age: ')
# color(in)
#
#
#
# my_list = list(range(15))
# print(my_list)
#
# for x in my_list:
#     if x % 2!=0:
#         print(x)





from random import randint

empty_list = []
numbers=[3, 8, 9, 6, 7]

for x in range(10):
    empty_list.append(random.randint(1, 10))

empty_list.pop()

empty_list.insert(5,200)

empty_list.extend(numbers)


print(empty_list)
















































