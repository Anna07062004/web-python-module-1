codes = [102, 101, 104, 103]
phones  = ["555-1234", "555-2345", "555-3456", "555-4567"]

while True:
    print("1. Отсортировать по идентификационным кодам")
    print("2. Отсортировать по номерам телефона")
    print("3. Вывести список пользователей")
    print("4. Выход")
    choice = input("Введите номер пункта (1–4): ")
    if choice == "1":
        sorted_data = sorted(zip(codes, phones))
        codes, phones = zip(*sorted_data)
        codes = list(codes)
        phones = list(phones)
        print("Список отсортирован по идентификационным кодам!")

    elif choice == "2":
        sorted_data = sorted(zip(phones, codes))
        phones, codes = zip(*sorted_data)
        phones = list(phones)
        codes = list(codes)
        print("Список отсортирован по номерам телефона!")

    elif choice == "3":
        for i in range(len(codes)):
            print(f"ID: {codes[i]} | Телефон: {phones[i]}")
        print("-" * 25)

    elif choice == "4":
        print("Программа завершена. До свидания!")
        break

    else:
        print("Ошибка! Введите число от 1 до 4.")