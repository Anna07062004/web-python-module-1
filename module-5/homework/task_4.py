book_collection = {}

def add_book(book_id, author, title, genre, year, pages, publisher):
    book_collection[book_id] = {
        'Автор': author,
        'Название': title,
        'Жанр': genre,
        'Год выпуска': year,
        'Количество страниц': pages,
        'Издательство': publisher
    }
    print(f"Книга '{title}' добавлена в коллекцию")

def remove_book(book_id):
    if book_id in book_collection:
        del book_collection[book_id]
        print(f"Книга с ID {book_id} удалена из коллекции")
    else:
        print(f"Книга с ID {book_id} не найдена")

def search_book(book_id):
    if book_id in book_collection:
        print(f"Информация о книге с ID {book_id}: ")
        for key, value in book_collection[book_id].items():
            print(f"{key}: {value}")
    else:
        print(f"Книга с ID {book_id} не найдена")

def update_book(book_id, field, new_value):
    if book_id in book_collection:
        if field in book_collection[book_id]:
            book_collection[book_id][field] = new_value
            print(f"Поле '{field}' обновлено на '{new_value}'")
        else:
            print(f"Поле '{field}' не существует")
    else:
        print(f"Книга с ID {book_id} не найдена")

# Основная программа
while True:
    print("\nМеню программы 'Книжная коллекция': ")
    print("1) Добавить книгу")
    print("2) Удалить книгу")
    print("3) Поиск книги по ID")
    print("4) Изменить информацию о книге")
    print("5) Показать все книги")
    print("6) Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        book_id = input("Введите ID книги: ")
        author = input("Введите автора: ")
        title = input("Введите название книги: ")
        genre = input("Введите жанр: ")
        year = input("Введите год выпуска: ")
        pages = input("Введите количество страниц: ")
        publisher = input("Введите издательство: ")
        add_book(book_id, author, title, genre, year, pages, publisher)
    
    elif choice == "2":
        book_id = input("Введите ID книги для удаления: ")
        remove_book(book_id)
    
    elif choice == "3":
        book_id = input("Введите ID книги для поиска: ")
        search_book(book_id)
    
    elif choice == "4":
        book_id = input("Введите ID книги: ")
        field = input("Введите поле для обновления (Автор, Название, Жанр, Год выпуска, Количество страниц, Издательство): ")
        new_value = input(f"Введите новое значение для поля '{field}': ")
        update_book(book_id, field, new_value)
    
    elif choice == "5":
        if book_collection:
            print("\nВсе книги в коллекции: ")
            for book_id, info in book_collection.items():
                print(f"\nID книги: {book_id}")
                for key, value in info.items():
                    print(f"  {key}: {value}")
        else:
            print("Коллекция пуста")
    
    elif choice == "6":
        print("Выход из программы")
        break
    
    else:
        print("Неверный выбор. Попробуйте снова")