basketball_players = {}

def add_player(name, height):
    if not name or not name.strip():
        print("Ошибка: ФИО не может быть пустым.")
        return False
    if height <= 0:
        print("Ошибка: рост должен быть положительным числом.")
        return False

    if name in basketball_players:
        print(f"Игрок {name} уже есть в базе.")
        return False
    else:
        basketball_players[name] = height
        print(f"Добавлен игрок: {name}, рост: {height} см.")
        return True

def delete_player(name):
    if name in basketball_players:
        del basketball_players[name]
        print(f"Игрок {name} удалён.")
        return True
    else:
        print(f"Игрок {name} не найден.")
        return False

def find_player(name):
    height = basketball_players.get(name)
    if height is not None:
        print(f"{name}: рост {height} см.")
        return True
    else:
        print(f"Игрок {name} не найден.")
        return False

def update_player(name, new_height):
    if new_height <= 0:
        print("Ошибка: рост должен быть положительным числом.")
        return False

    if name in basketball_players:
        basketball_players[name] = new_height
        print(f"Обновлён рост для {name}: {new_height} см.")
        return True
    else:
        print(f"Игрок {name} не найден.")
        return False

def show_all_players():
    if not basketball_players:
        print("Список баскетболистов пуст.")
        return

    sorted_players = sorted(
        basketball_players.items(),
        key=lambda x: x[0].split()[-1]
    )
    for name, height in sorted_players:
        print(f"{name} — {height} см")
    print("-" * 25)

def get_valid_height():
    while True:
        try:
            height = float(input("Введите рост (в см): "))
            if height <= 0:
                print("Рост должен быть положительным числом.")
                continue
            return height
        except ValueError:
            print("Введите числовое значение для роста.")

def main_menu():
    while True:
        print("1. Добавить игрока")
        print("2. Удалить игрока")
        print("3. Найти игрока")
        print("4. Обновить данные игрока")
        print("5. Показать всех игроков")
        print("6. Выход")

        choice = input("Ваш выбор (1–6): ").strip()

        if choice == "1":
            name = input("Введите ФИО баскетболиста: ").strip()
            height = get_valid_height()
            add_player(name, height)

        elif choice == "2":
            name = input("Введите ФИО баскетболиста для удаления: ").strip()
            delete_player(name)

        elif choice == "3":
            name = input("Введите ФИО баскетболиста для поиска: ").strip()
            find_player(name)

        elif choice == "4":
            name = input("Введите ФИО баскетболиста для обновления: ").strip()
            new_height = get_valid_height()
            update_player(name, new_height)

        elif choice == "5":
            show_all_players()

        elif choice == "6":
            print("Программа завершена. До свидания!")
            break

        else:
            print("Неверный выбор! Введите число от 1 до 6.")

if __name__ == "__main__":
    add_player("Майкл Джордан", 198)
    add_player("Леброн Джеймс", 206)
    find_player("Майкл Джордан")
    update_player("Майкл Джордан", 200)
    delete_player("Леброн Джеймс")
    find_player("Леброн Джеймс")

    print("\n" + "="*40)
    main_menu()