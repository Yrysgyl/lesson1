def add_food(food_dict, food_name, calories):
    food_dict[food_name] = calories


    print(f"Продукт '{food_name}' добавлен. ({calories} калорий)")


def display_food(food_dict):
    print("Список продуктов:")
    for food, calories in food_dict.items():
        print(f"{food}: {calories} калорий")


def total_calories(food_dict):
    total = sum(food_dict.values())
    print(f"Общее количество потребленных калорий: {total} калорий")


def main():
    food_dict = {}


    while True:
        print("\nМеню:")
        print("1. Добавить продукт")
        print("2. Просмотреть список продуктов")
        print("3. Посчитать общее количество потребленных калорий")
        print("4. Выход")
        choice = input("Выберите действие: ")
        if choice == '1':
            food_name = input("Введите название продукта: ")
            calories = int(input("Введите количество калорий: "))
            add_food(food_dict, food_name, calories)
        elif choice == '2':
            display_food(food_dict)
        elif choice == '3':
            total_calories(food_dict)
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор.")


if __name__ == "__main__":
    main()