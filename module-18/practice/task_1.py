# задача 1

def process_list(lst):
    if not lst:
        return lst
    
    n = len(lst)
    avg = sum(lst) / n

    if avg > 0:
        split_index = 2 * n // 3
        sorted_part  = sorted(lst[:split_index])
        reversed_part = lst[split_index:][::-1]
        return sorted_part + reversed_part
    
    else:
        split_index = n // 3
        sorted_part = sorted(lst[:split_index])
        reversed_part = lst[split_index][::-1]
        return sorted_part +reversed_part
    
original_list = [3, 1, 4, 1, 5, 9, 2, 6]
result = process_list(original_list)
print("Исходный список: ", original_list)
print("Обработаный список: ", result)

# задача 2

def print_grades(grades):
    print("Оценки студента:", grades)

def retake_exam(grades):
    try:
        index = int(input("Введите номер оценки для пересдачи (1-10): ")) - 1
        if 0 <= index < len(grades):
            new_grade = int(input("Введите новую оценку (1-12): "))
            if 1 <= new_grade <= 12:
                grades[index] = new_grade
                print("Оценка успешно обновлена!")
            else:
                print("Ошибка: оценка должна быть от 1 до 12.")
        else:
            print("Ошибка: номер оценки должен быть от 1 до 10.")
    except ValueError:
        print("Ошибка: введите корректное число.")

def check_scholarship(grades):
    average = sum(grades) / len(grades)
    if average >= 10.7:
        print(f"Средний балл: {average:.2f}. Стипендия выплачивается!")
    else:
        print(f"Средний балл: {average:.2f}. Стипендия не выплачивается.")

def sort_grades(grades):
    choice = input("Выберите порядок сортировки (1 — по возрастанию, 2 — по убыванию): ")
    if choice == '1':
        sorted_grades = sorted(grades)
        print("Отсортированные оценки (по возрастанию):", sorted_grades)
    elif choice == '2':
        sorted_grades = sorted(grades, reverse=True)
        print("Отсортированные оценки (по убыванию):", sorted_grades)
    else:
        print("Ошибка: выберите 1 или 2.")

def main():
    print("Программа «Успеваемость»")
    print("Введите 10 оценок студента (от 1 до 12):")

    grades = []
    for i in range(10):
        while True:
            try:
                grade = int(input(f"Оценка {i + 1}: "))
                if 1 <= grade <= 12:
                    grades.append(grade)
                    break
                else:
                    print("Ошибка: оценка должна быть от 1 до 12. Попробуйте снова.")
            except ValueError:
                print("Ошибка: введите целое число от 1 до 12.")
    while True:
        print("\n" + "=" * 40)
        print("МЕНЮ:")
        print("1 – Вывод оценок")
        print("2 – Пересдача экзамена")
        print("3 – Проверка стипендии")
        print("4 – Сортировка оценок")
        print("0 – Выход")
        print("=" * 40)

        choice = input("Выберите действие (0-4): ")

        if choice == '1':
            print_grades(grades)
        elif choice == '2':
            retake_exam(grades)
        elif choice == '3':
            check_scholarship(grades)
        elif choice == '4':
            sort_grades(grades)
        elif choice == '0':
            print("До свидания!")
        else:
            print("Неверный выбор. Попробовать снова.")

if __name__ == "__main__":
    main()

# задача 3

def optimized_bubble_sort(arr): 
    n = len(arr)
    sorted_arr = arr.copy()

    for i in range(n): 
        swapped = False

        for j in range(0, n-i- 1): 
            if sorted_arr[j] > sorted_arr[j + 1]: 
                sorted_arr[j], sorted_arr[j + 1] - sorted_arr[j + 1], sorted_arr[j]  
                swapped = True
        if not swapped: 
            break

    return sorted_arr
def demonstrate_algorithm():
    print("\n" + "=" * 50) 
    print("Дeмoнcтpaция работы алгоритма: ") 
    example = [64, 34, 25, 12, 22, 11, 90] 
    print(f"Пример: {example}")

    n = len(example) 
    arr = example.copy()

    for i in range(n): 
        swapped = False 
        print(f"\nПроход {i + 1}:") 
        print(f" Teкущий список: {arr}")
        
        for j in range(0, n - i - 1): 
            if arr[j] > arr[j + 1]: 
                arr[j], arr[j + 1] - arr[j + 1], arr[j] 
                swapped = True  
                print(f" Перестановка: {arr[j + 1]} и {arr[j]} -> {arr}")

        if not swapped: 
            print("    Перестановок не было - список отсортирован!") 
            break
        else: 
            print(f"После прохода: {arr}")

    print(f"Итоговый результат: {arr}")

def main():
    print("Пpoгpaммa; Усовершенствованная пузырьковая сортировка") 
    print("=" * 50)

    while True:
        try:
            user_input = input("Введите числа через пробел: ") 
            numbers = list(map(int, user_input.split())) 
            if len(numbers) == 0:
                print("Ошибка: вводите хотя бы одно число.") 
                continue
            break
        except ValueError:
            print("Ошибка: пожалуста, вводите только целые числа.")

    print(f"Исходный список: {numbers}") 
    sorted_numbers = optimized_bubble_sort(numbers) 
    print(f"Отсортировный список: {sorted_numbers}")

demonstrate_algorithm()
if __name__ == "__main__":
    main()