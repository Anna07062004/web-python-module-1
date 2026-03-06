library = []

def add_book():
    author = input("Автор: ")
    title = input("Название книги: ")
    genre = input("Жанр: ")
    year = input("Год выпуска: ")
    pages = input("Количество страниц: ")
    publisher = input("Издательство: ")
    book = {
        "автор": author,
        "название": title,
        "жанр": genre,
        "год": year,
        "страниц": pages,
        "издательство": publisher
    }
    library.append(book)
    print("Книга добавлена.")

def delete_book():
    title = input("Введите название книги для удаления: ")
    for book in library:
        if book["название"].lower() == title.lower():
            library.remove(book)
            print("Книга удалена.")
            return
    print("Книга не найдена.")

def search_book():
    title = input("Введите название книги для поиска: ")
    found = False
    for book in library:
        if title.lower() in book["название"].lower():
            print_book_info(book)
            found = True
    if not found:
        print("Книга не найдена.")

def update_book():
    title = input("Введите название книги для редактирования: ")
    for book in library:
        if book["название"].lower() == title.lower():
            print("Введите новые данные (оставьте пустым, чтобы оставить без изменений):")
            author = input(f"Автор ({book['автор']}): ") or book['автор']
            genre = input(f"Жанр ({book['жанр']}): ") or book['жанр']
            year = input(f"Год выпуска ({book['год']}): ") or book['год']
            pages = input(f"Количество страниц ({book['страниц']}): ") or book['страниц']
            publisher = input(f"Издательство ({book['издательство']}): ") or book['издательство']
            book.update({
                "автор": author,
                "жанр": genre,
                "год": year,
                "страниц": pages,
                "издательство": publisher
            })
            print("Данные обновлены.")
            return
    print("Книга не найдена.")

def print_book_info(book):
    print(f"Автор: {book['автор']}")
    print(f"Название: {book['название']}")
    print(f"Жанр: {book['жанр']}")
    print(f"Год выпуска: {book['год']}")
    print(f"Количество страниц: {book['страниц']}")
    print(f"Издательство: {book['издательство']}\n")

def main():
    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Редактировать книгу")
        print("5. Выход")
        choice = input("Выберите действие (1-5): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            delete_book()
        elif choice == '3':
            search_book()
        elif choice == '4':
            update_book()
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод, попробуйте еще раз.")

if __name__ == "__main__":
    main()