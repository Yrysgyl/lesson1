# import random
#
#
# def number():
#     try:
#         num = random.randint(1, 100)
#         total = 0
#         while True:
#             my_num = int(input('num: '))
#             total += 1
#             if my_num < num:
#                 print('твое  меньше моего')
#             elif my_num > num:
#                 print('твое  больше моего')
#             else:
#                 print(f'Угадал правильно число {num}, за {total} раз')
#                 break
#     except ValueError as a:
#         print('введите целое число', a)
#
#
# number()

# def add_food(food_dict, food_name, calories):
#     food_dict[food_name] = calories
#     print(f'продукт "{food_name}" добавлен.({calories} калорий)')
#     def display_food(food_dict):
#         print('список продуктов:')
#
#         for food, calories in food_dict.items():
#             print(f"{food}:{calories} калорий")
#
#             def total_calories(food_dict):
#                 total = sum(food_dict.values())
#                 print(f'общее количество потребленных калорий:{total} калорий')
#
#                 def main():
#                     food_dict = {}
#                     while True:
#                         print("\nМеню:")
#                         print('1.Добавить продукт')
#                         print('посмотреть список продуктов')
#                         print('3.Посчитать общее количество потребленных калорий')
#                         print('4. Выход')
#                         choise = input('Выберите действие: ')
#                         if choise == '1':
#                             food_name = input('Введите название продукта: ')
#                             calories = int(input('Введите количество калорий: '))
#                             add_food(food_dict, food_name, calories)
#                         elif choise == '2':
#                             display_food(food_dict)
#                         elif choise == '3':
#                             total_calories(food_dict)
#                         elif choise == 4:
#                             print('Выход из программы.')
#                             break
#                         else:
#                             print('Некорректный выбор.')
#                         if _name_ == 'main':
#                             main()


# def add_food(food_dict, food_name, calories):    food_dict[food_name] = calories
#
#
# print(f"Продукт '{food_name}' добавлен. ({calories} калорий)")


# def display_food(food_dict):
#     print("Список продуктов:")
#     for food, calories in food_dict.items():
#         print(f"{food}: {calories} калорий")
#
#
# def total_calories(food_dict):
#     total = sum(food_dict.values())
#     print(f"Общее количество потребленных калорий: {total} калорий")
#
#
# def main():    food_dict = {}
#
#
# while True:
#     print("\nМеню:")
#     print("1. Добавить продукт")
#     print("2. Просмотреть список продуктов")
#     print("3. Посчитать общее количество потребленных калорий")
#     print("4. Выход")
#     choice = input("Выберите действие: ")
#     if choice == '1':            food_name = input("Введите название продукта: ")
#     calories = int(input("Введите количество калорий: "))
#     add_food(food_dict, food_name, calories)
#     elif choice == '2':
#     (display_food(food_dict))
#     elif choice == '3':
#     (total_calories(food_dict))
#     elif choice == '4':
#         (print("Выход из программы."))
#         break
#     else:
#         print("Некорректный выбор.")
# if __name__ == "__main__":
#     main()


#p_ages = {'kate': 23, 'stella': 20, 'bloom': 22}
# print(p_ages['bloom'])
# print(p_ages.keys())
# print(p_ages.values())
# print(p_ages.items())
# print(p_ages.get('kate'))
# a = p_ages.copy()
# print(a)
# print(len(a))
# print(p_ages['stella'])
#print(p_ages.get('bloom'))


