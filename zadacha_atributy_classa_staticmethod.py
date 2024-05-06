"""
Управление заказами в ресторане:
Создайте класс Order, который представляет заказ в ресторане. Каждый заказ должен содержать следующую информацию:
Номер заказа
Список блюд
Общая сумма заказа
Статус заказа (например, "в обработке", "готов", "доставлен")
Добавьте методы для добавления блюд к заказу, расчета общей суммы заказа, изменения статуса заказа и отображения информации о заказе.
"""


class Order:
    def __init__(self, number_order):
        self.number_order = number_order
        self.list_food = []
        self.total_sum = 0
        self.status = 'в обработке'

    def add_food(self, name_food, price_food):
        self.list_food.append((name_food, price_food))

    def change_status(self, new_status):
        self.status = new_status

    def inform(self):
        print(f'номер заказа: {self.number_order}')
        print(f'foods: ')
        for i in self.list_food:
            print(f"{i[0]}: {i[1]}")
        print(f'status: {self.status}')


zakaz1 = Order(1)
zakaz1.add_food('lagman', 100)
zakaz1.change_status('готов')
zakaz1.inform()





