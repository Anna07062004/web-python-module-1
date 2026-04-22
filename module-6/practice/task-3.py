"""
ЗАДАЧА: Анализ покупок в магазине

Дан список покупок. Каждая покупка содержит:
- user      : имя покупателя (строка)
- items     : список купленных товаров (список строк)
- price     : общая стоимость покупки (целое число)
- timestamp : время покупки (целое число)

НЕОБХОДИМО РЕАЛИЗОВАТЬ:

1. Посчитать общее количество покупок каждого пользователя.

2. Посчитать общую сумму потраченных денег каждым пользователем.

3. Для каждого пользователя:
   - найти множество уникальных товаров, которые он покупал
   - посчитать общее количество купленных товаров (с учётом повторов)

4. Найти товар, который покупали чаще всего
   (если таких несколько — можно вернуть любой).

5. Найти пользователя, который:
   - потратил больше всего денег
   - купил больше всего товаров
   (это могут быть разные пользователи)

6. Для каждого пользователя найти самый большой перерыв
   между его покупками (по timestamp).
"""

purchases = [
    {"user": "Алиса", "items": ["яблоко", "банан"],          "price": 120, "timestamp": 1},
    {"user": "Боб",   "items": ["банан"],                    "price": 50,  "timestamp": 2},
    {"user": "Алиса", "items": ["апельсин", "яблоко"],       "price": 150, "timestamp": 5},
    {"user": "Боб",   "items": ["яблоко", "апельсин"],       "price": 130, "timestamp": 6},
    {"user": "Алиса", "items": ["банан", "банан"],           "price": 70,  "timestamp": 15},
    {"user": "Боб",   "items": ["банан"],                    "price": 40,  "timestamp": 25},
]

purchase_count = {}
for purchase in purchases:
    user = purchase["user"]
    if user in purchase_count:
        purchase_count[user] += 1
    else:
        purchase_count[user] = 1

total_spent = {}
for purchase in purchases:
    user = purchase["user"]
    price = purchase["price"]
    if user in total_spent:
        total_spent[user] += price
    else:
        total_spent[user] = price

unique_items = {} 
total_items_count = {} 

for purchase in purchases:
    user = purchase["user"]
    items = purchase["items"]
    
    if user not in unique_items:
        unique_items[user] = set()
    unique_items[user].update(items)
    
    if user in total_items_count:
        total_items_count[user] += len(items)
    else:
        total_items_count[user] = len(items)

item_frequency = {}
for purchase in purchases:
    for item in purchase["items"]:
        if item in item_frequency:
            item_frequency[item] += 1
        else:
            item_frequency[item] = 1

most_common_item = None
max_count = 0
for item, count in item_frequency.items():
    if count > max_count:
        max_count = count
        most_common_item = item

max_spent_user = None
max_spent_amount = 0
for user, amount in total_spent.items():
    if amount > max_spent_amount:
        max_spent_amount = amount
        max_spent_user = user

max_items_user = None
max_items_count = 0
for user, count in total_items_count.items():
    if count > max_items_count:
        max_items_count = count
        max_items_user = user

max_breaks = {}
user_timestamps = {}

for purchase in purchases:
    user = purchase["user"]
    timestamp = purchase["timestamp"]
    if user not in user_timestamps:
        user_timestamps[user] = []
    user_timestamps[user].append(timestamp)

for user, timestamps in user_timestamps.items():
    timestamps.sort()
    max_break = 0
    for i in range(1, len(timestamps)):
        break_time = timestamps[i] - timestamps[i-1]
        if break_time > max_break:
            max_break = break_time
    max_breaks[user] = max_break

print("Количество покупок каждого пользователя:")
for user, count in purchase_count.items():
    print(f"{user}: {count}")

print("Общая сумма потраченных денег:")
for user, total in total_spent.items():
    print(f"{user}: {total} руб.")

print("Информация по пользователям:")
for user in unique_items:
    print(f"{user}:")
    print(f"Уникальные товары: {sorted(unique_items[user])}")
    print(f"Всего куплено товаров: {total_items_count[user]}")

print(f"Самый популярный товар: '{most_common_item}' (куплен {max_count} раз)")

print(f"Лидеры:")
print(f"Больше всего потратил: {max_spent_user} ({max_spent_amount} руб.)")
print(f"Больше всего товаров купил: {max_items_user} ({max_items_count} товаров)")

print("Самые большие перерывы между покупками:")
for user, max_break in max_breaks.items():
    print(f"{user}: {max_break} единиц времени")