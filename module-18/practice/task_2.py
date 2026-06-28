#задача 1

def sort_by_ids(ids, phones):
    combined = sorted(zip(ids, phones), key=lambda x: x[0])
    sorted_ids, sorted_phones = zip(*combined) if combined else ([], [])
    return list(sorted_ids), list(sorted_phones)

def sort_by_phones(ids, phones):
    combined = sorted(zip(ids, phones), key=lambda x: x[1])
    sorted_ids, sorted_phones = zip(*combined) if combined else ([], [])
    return list(sorted_ids), list(sorted_phones)

def print_users(ids, phones):
    if not ids:
        print("Список пользователей нет.")
        return

    print("Список пользователей:")
    print("_*_* 40")
    for i, (user_id, phone) in enumerate(zip(ids, phones), 1):
        print(f"{i}: ID: {user_id} | Телефон: {phone}")
    print("_*_* 40")

def main():
    print("Программа «Справочник»")
    print("=" * 50)

    user_ids = [101, 205, 150, 300, 120]
    phone_numbers = [79161234567, 79262345678, 79363456789, 79464567890, 79565678901]

    print(f"Начальное количество пользователей: {len(user_ids)}")

while True:
    print("\n" + "=" * 50)
    print("МЕНЮ:")
    print("1 – Отсортировать по идентификационным кодам (по возрастанию)")
    print("2 – Отсортировать по номерам телефона (по возрастанию)")
    print("3 – Вывести список пользователей 📋 кодами и телефонами")
    print("0 – Выход")
    print("=" * 50)

    choice = input("Выберите действие (0-3): ")

    if choice == '1':
        user_ids, phone_numbers = sort_by_ids(user_ids, phone_numbers)
        print("Список отсортирован по идентификационным кодам (по возрастанию).")

    elif choice == '2':
        user_ids, phone_numbers = sort_by_phones(user_ids, phone_numbers)
        print("Список отсортирован по номерам телефона (по возрастанию).")

    elif choice == '3':
        print_users(user_ids, phone_numbers)
    elif choice == '0':
        print("До свидания!")
        break

    else:
        print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()

#задача 2

def sort_by_titles(titles, years):
    combined = sorted(zip(titles, years), key=lambda x: x[0].lower())
    sorted_titles, sorted_years = zip(*combined) if combined else ([], [])
    return list(sorted_titles), list(sorted_years)

def sort_by_years(titles, years):
    combined = sorted(zip(titles, years), key=lambda x: x[1])
    sorted_titles, sorted_years = zip(*combined) if combined else ([], [])
    return list(sorted_titles), list(sorted_years)

def print_books(titles, years):
    if not titles:
        print("Список книг пуст.")
        return

    print("Список книг:")
    print("-" * 50)
    for i, (title, year) in enumerate(zip(titles, years), 1):
        print(f"{i}. {title} ({year})")
    print("-" * 50)

def main():
    print("Программа «Книги»")
    print("=" * 50)

    book_titles = [
        "Война и мир",
        "Преступление и наказание",
        "Мастер и Маргарита"
    ]
    book_years = [1869, 1866, 1966]

    print(f"Начальное количество книг: {len(book_titles)}")

    while True:
        print("\n" + "=" * 50)
        print("МЕНЮ:")
        print("1 — Отсортировать по названию книг (по алфавиту)")
        print("2 — Отсортировать по годам выпуска (по возрастанию)")
        print("3 — Вывести список книг с названиями и годами выпуска")
        print("0 — Выход")
        print("=" * 50)

        choice = input("Выберите действие (0-3): ")

        if choice == '1':
            book_titles, book_years = sort_by_titles(book_titles, book_years)
            print("Список отсортирован по названиям книг (по алфавиту).")

        elif choice == '2':
            book_titles, book_years = sort_by_years(book_titles, book_years)
            print("Список отсортирован по годам выпуска (по возрастанию).")

        elif choice == '3':
            print_books(book_titles, book_years)

        elif choice == '0':
            print("До свидания!")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()