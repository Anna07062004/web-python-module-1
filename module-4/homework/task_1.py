import random

list1 = [random.randint(1, 20) for _ in range(10)]
list2 = [random.randint(1, 20) for _ in range(10)]
print("1:", list1)
print("2:", list2)

combined = list1 + list2
print("Объединённый список:", combined)

un_com = list(set(combined))
print("Без повторений:", un_com)

com = list(set(list1) & set(list2))
print("Общие элементы:", com)

uniqu = list(set(list1) ^ set(list2))
print("Уникальные элементы каждого списка:", uniqu)

min_max_list1 = [min(list1), max(list1)]
min_max_list2 = [min(list2), max(list2)]
min_max_combined = min_max_list1 + min_max_list2
print("5. Минимальные и максимальные значения:", min_max_combined)