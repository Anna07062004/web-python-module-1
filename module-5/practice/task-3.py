firm = {}

def add_employee(employee_id, full_name, phone, email, position, office_number, skype):
    firm[employee_id] = {
        'ФИО': full_name,
        'Телефон': phone,
        'Email': email,
        'Должность': position,
        'Кабинет': office_number,
        'Skype': skype
    }
    print(f"Сотрудник '{full_name}' добавлен")

def remove_employee(employee_id):
    if employee_id in firm:
        del firm[employee_id]
        print(f"Сотрудник с ID {employee_id} удален")
    else:
        print(f"Сотрудник с ID {employee_id} не найден")

def search_employee(employee_id):
    if employee_id in firm:
        print(f"Информация о сотруднике с ID {employee_id}: ")
        for key, value in firm[employee_id].items():
            print(f"{key}: {value}")
    else:
        print(f"Сотрудник с ID {employee_id} не найден")

def update_employee(employee_id, field, new_value):
    if employee_id in firm:
        if field in firm[employee_id]:
            firm[employee_id][field] = new_value
            print(f"Поле '{field}' обновлено на '{new_value}'")
        else:
            print(f"Поле '{field}' не существует")
    else:
        print(f"Сотрудник с ID {employee_id} не найден")

while True:
    print("\nМеню программы 'Фирма': ")
    print("1) Добавить сотрудника")
    print("2) Удалить сотрудника")
    print("3) Поиск сотрудника по ID")
    print("4) Изменить информацию о сотруднике")
    print("5) Показать всех сотрудников")
    print("6) Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        employee_id = input("Введите ID сотрудника: ")
        full_name = input("Введите ФИО: ")
        phone = input("Введите телефон: ")
        email = input("Введите рабочий email: ")
        position = input("Введите должность: ")
        office_number = input("Введите номер кабинета: ")
        skype = input("Введите Skype: ")
        add_employee(employee_id, full_name, phone, email, position, office_number, skype)
    
    elif choice == "2":
        employee_id = input("Введите ID сотрудника для удаления: ")
        remove_employee(employee_id)
    
    elif choice == "3":
        employee_id = input("Введите ID сотрудника для поиска: ")
        search_employee(employee_id)
    
    elif choice == "4":
        employee_id = input("Введите ID сотрудника: ")
        field = input("Введите поле для обновления (ФИО, Телефон, Email, Должность, Кабинет, Skype): ")
        new_value = input(f"Введите новое значение для поля '{field}': ")
        update_employee(employee_id, field, new_value)
    
    elif choice == "5":
        if firm:
            print("\nВсе сотрудники фирмы: ")
            for emp_id, info in firm.items():
                print(f"ID сотрудника: {emp_id}")
                for key, value in info.items():
                    print(f"  {key}: {value}")
        else:
            print("Список сотрудников пуст")
    
    elif choice == "6":
        print("Выход из программы")
        break
    
    else:
        print("Неверный выбор. Попробуйте снова")