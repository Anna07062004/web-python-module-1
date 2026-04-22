grades = []

for i in range(10):
    while True:
        try:
            grade = int(input(f"Оценка {i + 1}: "))
            if 1 <= grade <= 12:
                grades.append(grade)
                break
            else:
                print("Ошибка! Оценка должна быть от 1 до 12. Попробуйте ещё раз.")
        except ValueError:
            print("Ошибка! Введите целое число от 1 до 12.")

while True:
    print("1. Вывод оценок")
    print("2. Пересдача экзамена")
    print("3. Выходит ли стипендия?")
    print("4. Вывод отсортированного списка оценок")
    print("5. Выход")

    choice = input("Выберите пункт меню (1–5): ")

    if choice == "1":
        print("Список оценок:")
        for i, grade in enumerate(grades, 1):
            print(f"Предмет {i}: {grade}")

    elif choice == "2":
        while True:
            try:
                index = int(input("Введите номер предмета (1–10): ")) - 1
                if 0 <= index < 10:
                    break
                else:
                    print("Ошибка! Номер должен быть от 1 до 10.")
            except ValueError:
                print("Ошибка! Введите число от 1 до 10.")

        while True:
            try:
                new_grade = int(input("Введите новую оценку (1–12): "))
                if 1 <= new_grade <= 12:
                    grades[index] = new_grade
                    print(f"Оценка успешно изменена!")
                    break
                else:
                    print("Ошибка! Оценка должна быть от 1 до 12.")
            except ValueError:
                print("Ошибка! Введите целое число от 1 до 12.")

    elif choice == "3":
        average = sum(grades) / len(grades)
        print(f"\nСредний балл: {average:.2f}")
        if average >= 10.7:
            print("Стипендия ВЫХОДИТ! 🎉")
        else:
            print("Стипендия НЕ выходит.")

    elif choice == "4":
        sort_choice = input("Сортировать по возрастанию (1) или убыванию (2)? ")
        if sort_choice == "1":
            sorted_grades = sorted(grades)
            print("Оценки по возрастанию:", sorted_grades)
        elif sort_choice == "2":
            sorted_grades = sorted(grades, reverse=True)
            print("Оценки по убыванию:", sorted_grades)
        else:
            print("Ошибка! Выберите 1 или 2.")

    elif choice == "5":
        print("Программа завершена. До свидания!")
        break

    else:
        print("Ошибка! Введите число от 1 до 5.")