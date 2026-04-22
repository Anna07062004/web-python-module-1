elements = list(map( int, input("Введите элементы списка через пробел: ").split()))
total_sum = sum(elements)

average = total_sum / len(elements) if elements else 0

print(f"Сумма: {total_sum}")
print(f"Среднее: {average}")