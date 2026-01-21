element = list(map(int, input("Введите элементы списка через пробел: ").split()))
target_number = int(input("Введите число для поиска: "))

count = 0
for number in element:
    if number == target_number:
        count += 1

print(f"Число {target_number} встречаются в списке {count}")