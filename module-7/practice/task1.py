import json

filename = "sotrudniki.json"

def load_data():
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def add_employee(data):
    id = input("Введите ID: ")
    surname = input("Фамилия: ")
    name = input("Имя: ")
    age = int(input("Возраст: "))
    position = input('Должность: ')
    employee = {"ID": id, "Фамилия": surname, "Имя": name, "Возраст": age, "Должность": position}
    data.append(employee)
    print("Сотрудник добавлен")

def edit_employee(data):
    id = input("Введите ID сотрудника для редактирования: ")
    for emp in data:
        if emp["ID"] == id:
            print(f"Редактируем сотрудника: {emp}")
            emp["Фамилия"] = input("Фамилия: ") or emp["Фамилия"]
            emp["Имя"] = input("Имя: ") or emp["Имя"]
            age_input = input("Возраст: ")
            if age_input:
                emp["Возраст"] = int(age_input)
            emp["Должность"] = input("Должность: ") or emp["Должность"]
            print("Данные обновлены")
            return
    print("Сотрудник с таким ID не найден.")

def delete_employee(data):
    id = input("Введите ID для удаления: ")
    for i, emp in enumerate(data):
        if emp["ID"] == id:
            del data[i]
            print("Сотрудник удален")
            return
    print("Сотрудник с таким ID не найден")

def search_by_surname(data):
    surname = input("Введите фамилию для поиска: ")
    result = [emp for emp in data if emp["Фамилия"].startswith(surname)]
    print("Результат поиска: ")
    for emp in result:
        print(emp)
    save_option = input("Сохранить результат в файл?: ").lower()
    if save_option == "да":
        filename = input("Введите название файла: ")
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=4)

def list_all(data):
    print("Все сотрудники:")
    for emp in data:
        print(emp)

def filter_by_age(data):
    age = int(input("Введите возраст для фильтрации: "))
    result = [emp for emp in data if emp["Возраст"] == age]
    print(f"Сотрудники возрастом {age}: ")
    for emp in result:
        print(emp)

def filter_by_letter(data):
    letter = input("Введите букву для фильтрации фамилий: ").upper()
    result = [emp for emp in data if emp["Фамилия"].startswith(letter)]
    print(f"Фамилии, начинающиеся на {letter}: ")
    for emp in result:
        print(emp)

def main():
    data = load_data()
    while True:
        print("1. Добавить сотрудника")
        print("2. Редактировать сотрудника")
        print("3. Удалить сотрудника")
        print("4. Найти по фамилии")
        print("5. Вывести всех сотрудников")
        print("6. Фильтр по возрасту")
        print("7. Фамилии на букву")
        print("8. Сохранить и выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            add_employee(data)
        elif choice == "2":
            edit_employee(data)
        elif choice == "3":
            delete_employee(data)
        elif choice == "4":
            search_by_surname(data)
        elif choice == "5":
            list_all(data)
        elif choice == "6":
            filter_by_age(data)
        elif choice == "7":
            filter_by_letter(data)
        elif choice == "8":
            save_data(data)
            print("Данные сохранены. Выход из программы.")
            break
        else:
            print("Некорректный выбор.")

if __name__ == "__main__":
    main()