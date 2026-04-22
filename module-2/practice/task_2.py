n = int(input("Сколько пар ключ-значение хотите добавить?"))
d = {}

for i in range(n):
    key = input(f"Введите ключ {i+1}: ")
    value = input(f"Введите значения: ")
    d[key] = value

print(f"Создан словарь: ")
for key, value in d.items():
    print(f"{key}={value}")