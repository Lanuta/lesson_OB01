#Ты разрабатываешь программное обеспечение для сети магазинов.
#Каждый магазин в этой сети имеет свои особенности,
#но также существуют общие характеристики, такие как адрес,
#название и ассортимент товаров. Ваша задача — создать класс Store,
#который можно будет использовать для создания различных магазинов.

class Store:
    def __init__(self, name, address):
        """Конструктор для инициализации магазина с названием, адресом и пустым ассортиментом товаров."""
        self.name = name
        self.address = address
        self.items = {}  # Пустой словарь для товаров

    def add_item(self, item_name, price):
        """Добавить товар в ассортимент магазина."""
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен в ассортимент магазина '{self.name}' по цене {price}.")

    def remove_item(self, item_name):
        """Удалить товар из ассортимента магазина."""
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из ассортимента магазина '{self.name}'.")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте магазина '{self.name}'.")

    def get_item_price(self, item_name):
        """Получить цену товара по названию. Если товара нет, вернуть None."""
        return self.items.get(item_name, None)

    def update_item_price(self, item_name, new_price):
        """Обновить цену товара в ассортименте."""
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена в магазине '{self.name}' на {new_price}.")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте магазина '{self.name}'.")

    def __str__(self):
        """Вывод информации о магазине и его ассортименте."""
        items_info = "\n".join([f"{item}: {price}" for item, price in self.items.items()])
        return f"Магазин: {self.name}\nАдрес: {self.address}\nАссортимент товаров:\n{items_info if items_info else 'Нет товаров'}"

# 3. Пример использования

# Создаем три магазина
store1 = Store("Фрукты и овощи", "Улица Ленина, 5")
store2 = Store("Техника для дома", "Проспект Мира, 10")
store3 = Store("Книжный уголок", "Улица Пушкина, 20")

# Добавляем товары
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)
store2.add_item("washing_machine", 300)
store2.add_item("vacuum_cleaner", 150)
store3.add_item("book_1", 12)
store3.add_item("book_2", 15)

# Выводим информацию о магазинах
print(store1)
print(store2)
print(store3)

# Тестируем методы магазина store1
print("\nТестируем методы магазина store1:")

# Получаем цену товара
print("Цена на apples:", store1.get_item_price("apples"))

# Обновляем цену товара
store1.update_item_price("apples", 0.6)

# Удаляем товар
store1.remove_item("bananas")

# Проверяем после изменений
print(store1)
