def improv_bubble(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True 

        if not swapped:
            print(f"Сортировка завершена на проходе {i + 1} — перестановок больше нет.")
            break

    return arr

user_input = input("Введите числа через пробел: ")
numbers = list(map(int, user_input.split()))

print(f"\nИсходный список: {numbers}")

sorted_numbers = improv_bubble(numbers.copy()) 

print(f"Отсортированный список: {sorted_numbers}")