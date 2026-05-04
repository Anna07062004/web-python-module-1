from dataclasses import dataclass, field
from typing import List, Dict, Optional
import json

@dataclass
class Ingredient:
    name: str
    price: float
    quantity: int

@dataclass
class HotDog:
    name: str
    base_ingredient: List[str]
    topping: List[str]
    extras: Dict[str, bool]

@dataclass
class OrderItem:
    hot_dog: HotDog
    total_price: float

class InventoryManager:
    def __init__(self):
        self.ingredients: Dict[str, Ingredient] = {}
        self.load_ingredients()

    def load_ingredients(self):
        try:
            with open("ingredients.json", "r") as file:
                data = json.load(file)
                for ingr in data:
                    self.ingredients[ingr["name"]] = Ingredient(**ingr)
        except FileNotFoundError:
            self.ingredients = {
                "Булочка": Ingredient("Булочка", 0.5, 10),
                "Сосиска": Ingredient("Сосиска", 1.0, 10),
                "Горчица": Ingredient("Горчица", 0.2, 10),
                "Кетчуп": Ingredient("Кетчуп", 0.2, 10),
                "Майонез": Ingredient("Майонез", 0.2, 10),
                "Лук": Ingredient("Лук", 0.3, 10),
                "Халапеньо": Ingredient("Халапеньо", 0.3, 10),
                "Чили": Ingredient("Чили", 0.3, 10),
                "Огурец": Ingredient("Огурец", 0.4, 10),
            }
            self.save_ingredients()

    def save_ingredients(self):
        data = [ingr.__dict__ for ingr in self.ingredients.values()]
        with open("ingredients.json", "w") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def check_ingredients(self, needed: List[str]) -> List[str]:
        shortages = []
        for name in needed:
            if name not in self.ingredients or self.ingredients[name].quantity <= 0:
                shortages.append(name)
        return shortages

    def use_ingredients(self, needed: List[str]):
        for name in needed:
            if name in self.ingredients and self.ingredients[name].quantity > 0:
                self.ingredients[name].quantity -= 1
        self.save_ingredients()

    def get_status(self):
        return self.ingredients

    def get_shortages(self):
        shortages = [name for name, ingr in self.ingredients.items() if ingr.quantity <= 5]
        return shortages

class PriceCalculator:
    def __init__(self, base_price: float):
        self.base_price = base_price

    def calculate_total(self, hot_dog: HotDog, inventory: InventoryManager) -> float:
        price = self.base_price
        for extra, chosen in hot_dog.extras.items():
            if chosen and extra in inventory.ingredients:
                price += inventory.ingredients[extra].price
        return price

    def apply_discount(self, total: float, quantity: int) -> float:
        if quantity >= 3:
            return total * 0.9
        return total

class OrderManager:
    def __init__(self):
        self.orders: List[OrderItem] = []
        self.total_revenue = 0.0
        self.total_profit = 0.0
        self.load_orders()

    def load_orders(self):
        try:
            with open('orders.json', 'r') as file:
                data = json.load(file)
                for order_data in data:
                    hot_dog_data = order_data['hot_dog']
                    hot_dog = HotDog(
                        name=hot_dog_data['name'],
                        base_ingredient=hot_dog_data['base_ingredient'],
                        topping=hot_dog_data['topping'],
                        extras=hot_dog_data['extras']
                    )
                    order_item = OrderItem(hot_dog=hot_dog, total_price=order_data['total_price'])
                    self.orders.append(order_item)
                    self.total_revenue += order_item.total_price
                    self.total_profit += order_item.total_price * 0.8
        except FileNotFoundError:
            pass

    def add_order(self, order_item: OrderItem):
        self.orders.append(order_item)
        self.total_revenue += order_item.total_price
        self.total_profit += order_item.total_price * 0.8  # Можно заменить на расчёт по себестоимости
        self.save_orders()

    def save_orders(self):
        data = []
        for order in self.orders:
            data.append({
                'hot_dog': order.hot_dog.__dict__,
                'total_price': order.total_price
            })
        with open('orders.json', 'w') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def get_sales_summary(self):
        return {
            "Количество заказов": len(self.orders),
            "Выручка": self.total_revenue,
            "Прибыль": self.total_profit
        }

class Kiosk:
    def __init__(self):
        self.inventory = InventoryManager()
        self.order_manager = OrderManager()
        self.base_price = 3.0
        self.price_calculator = PriceCalculator(self.base_price)

        self.standard_recipes = [
            HotDog("Классический", ["Булочка", "Сосиска"], [], {}),
            HotDog("Владельческий", ["Булочка", "Сосиска"], [], {}),
            HotDog("Острый", ["Булочка", "Сосиска"], [], {})
        ]

    def main_menu(self):
        while True:
            print("\n1. Оформить заказ")
            print("2. Просмотреть состояние компонентов")
            print("3. Посмотреть продажи и прибыль")
            print("4. Просмотреть короткое наличие компонентов для изготовления")
            print("5. Выйти")
            choice = input("Выберите опцию: ")

            if choice == '1':
                self.make_order()
            elif choice == '2':
                self.view_components()
            elif choice == '3':
                self.view_sales()
            elif choice == '4':
                self.view_shortages()
            elif choice == '5':
                print("Спасибо за визит!")
                break
            else:
                print("Некорректный ввод")
    def make_order(self):
        print("\nВыберите рецепт или создайте свой:")
        print("1. Классический")
        print("2. Владельческий")
        print("3. Острый")
        print("4. Создать свой рецепт")
        choice = input("Введите выбор: ")

        if choice in ['1', '2', '3']:
            recipe = self.standard_recipes[int(choice) - 1]
        elif choice == '4':
            recipe = self.create_custom_recipe()
        else:
            print("Некорректный выбор.")
            return

        extras = {
            "Майонез": False,
            "Горчица": False,
            "Кетчуп": False,
            "Лук": False,
            "Халапеньо": False,
            "Чили": False,
            "Огурец": False
        }
        print("Добавки (да/нет):")
        for extra in extras:
            ans = input(f"{extra}? ").lower()
            extras[extra] = (ans == 'да' or ans == 'yes')

        hot_dog = HotDog(
            name=recipe.name,
            base_ingredient=recipe.base_ingredient,
            topping=recipe.topping,
            extras=extras
        )

        needed_ingredients = hot_dog.base_ingredient.copy()
        for extra, chosen in hot_dog.extras.items():
            if chosen:
                needed_ingredients.append(extra)

        shortages = self.inventory.check_ingredients(needed_ingredients)
        if shortages:
            print(f"Недостаточно компонентов: {', '.join(shortages)}. Пожалуйста, закажите заранее.")
            return

        total = self.price_calculator.calculate_total(hot_dog, self.inventory)
        quantity = 1
        total = self.price_calculator.apply_discount(total, quantity)

        print(f"Общая цена: {total:.2f} руб.")
        payment_method = input("Оплата наличными или картой? (нал/карта): ")
        print(f"Заказ оформлен на сумму {total:.2f} руб., оплата: {payment_method}.")

        self.inventory.use_ingredients(needed_ingredients)

        order_item = OrderItem(hot_dog=hot_dog, total_price=total)
        self.order_manager.add_order(order_item)

        self.display_order(hot_dog, total)

    def create_custom_recipe(self):
        name = input("Введите название вашего рецепта: ")
        base_ingredients = ["Булочка", "Сосиска"]
        toppings = []

        print("Добавьте топпинги (введите 'стоп' для завершения):")
        while True:
            ing = input("Топпинг: ").strip()
            if ing.lower() == 'стоп':
                break
            if ing: 
                toppings.append(ing)

        return HotDog(name=name, base_ingredient=base_ingredients, topping=toppings, extras={})

    def display_order(self, hot_dog: HotDog, total: float):
        print("\nВаш заказ")
        print(f"Рецепт: {hot_dog.name}")
        print("Основные ингредиенты:", ", ".join(hot_dog.base_ingredient))
        if hot_dog.topping:
            print("Топпинги:", ", ".join(hot_dog.topping))
        selected_extras = [ext for ext, chosen in hot_dog.extras.items() if chosen]
        if selected_extras:
            print("Добавки:", ", ".join(selected_extras))
        print(f"Итого к оплате: {total:.2f} руб.")
        print("=" * 20)

    def view_components(self):
        print("\nНаличие ингредиентов")
        for comp in self.inventory.get_status().values():
            status = "В наличии" if comp.quantity > 5 else "Мало!"
            print(f"{comp.name}: {comp.quantity} шт. ({status})")

    def view_shortages(self):
        shortages = self.inventory.get_shortages()
        if shortages:
            print("\n=== Ингредиенты на исходе ===")
            for s in shortages:
                quantity = self.inventory.ingredients[s].quantity
                print(f"- {s}: осталось {quantity} шт.")
        else:
            print("\nВсе компоненты в достаточном количестве.")

    def view_sales(self):
        summary = self.order_manager.get_sales_summary()
        print("\n=== Статистика продаж ===")
        print(f"Общее количество заказов: {summary['Количество заказов']}")
        print(f"Общая выручка: {summary['Выручка']:.2f} руб.")
        print(f"Общая прибыль: {summary['Прибыль']:.2f} руб.")

if __name__ == "__main__":
    kiosk = Kiosk()
    kiosk.main_menu()