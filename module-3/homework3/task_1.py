num1 = [7, 0, 4, 5, -2, 4]
num2 = [1, 2, 4, 7, 8, -9]

print(num1)
print(num2)

combined = num1 + num2
print(f"Оба списка: {combined}")

comi_no_dup = list(set(num1 +num2))
print(f"Не повторяющиеся: {comi_no_dup}")

com_elem = list(set(num1) & set(num2))
print(f"Общие элементы: {com_elem}")

un = list(set(num1) ^ set(num2))
print(f"Уникальное: {un}")

min_max_num1 = [min(num1), max(num1)]
min_max_num2 = [min(num2), max(num2)]
combi = min_max_num1 +min_max_num2
print(f"min и max  каждого списка: {combi}")