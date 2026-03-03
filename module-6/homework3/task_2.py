book_titles = ["Война и мир", "Преступление и наказание", "Мастер и Маргарита", "1984", "Гарри Поттер"]
book_years = [1869, 1866, 1966, 1949, 2000]

while True:
    print("1. Отсортировать по названию книг")
    print("2. Отсортировать по годам выпуска")
    print("3. Вывести список книг с названиями и годами выпуска")
    print("4. Выход")
    choice = input("Введите номер пункта (1–4): ")

    if choice == "1":
        sorted_books = sorted(zip(book_titles, book_years))
        book_titles, book_years = zip(*sorted_books)
        book_titles = list(book_titles)
        book_years = list(book_years)
        print("Список отсортирован по названиям книг!")

    elif choice == "2":
        sorted_books = sorted(zip(book_years, book_titles))
        book_years, book_titles = zip(*sorted_books)
        book_years = list(book_years)
        book_titles = list(book_titles)
        print("Список отсортирован по годам выпуска!")

    elif choice == "3":
        for i in range(len(book_titles)):
            print(f"Название: {book_titles[i]} | Год выпуска: {book_years[i]}")
        print("-" * 40)

    elif choice == "4":
        print("Программа завершена. До свидания!")
        break 

    else:
        print("Ошибка! Введите число от 1 до 4.")