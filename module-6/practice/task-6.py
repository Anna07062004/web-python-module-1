def proc_list(numbers):
    if not numbers:
        return []
    average = sum(numbers) / len(numbers)

    n = len(numbers)

    if average > 0:
        two_thirds = n * 2 // 3
        sorted_part = sorted(numbers[:two_thirds])
        reversed_part = numbers[two_thirds:][::-1]
    else:
        one_third = n // 3
        sorted_part = sorted(numbers[:one_third])
        reversed_part = numbers[one_third:][::-1]

    result = sorted_part + reversed_part
    return result

user_input = input("Введите числа через пробел: ")
numbers = list(map(int, user_input.split()))

print(f"\nИсходный список: {numbers}")

result = proc_list(numbers)

print(f"Обработанный список: {result}")

if numbers:
    average = sum(numbers) / len(numbers)
    print(f"Среднее арифметическое: {average}")
    if average > 0:
        print("Условие: среднее > 0 -> отсортированы первые 2/3")
    else:
        print("Условие: среднее < 0 -> отсортирована первая 1/3")