dictionary = {}

def add_word(english_word, french_translation):
    if english_word in dictionary:
        print(f"Слово {english_word} уже есть в словаре.")
    else:
        dictionary[english_word] = french_translation
        print(f"Добавлено: {english_word} - {french_translation}")

def delete_word(english_word):
    if english_word in dictionary:
        del dictionary[english_word]
        print(f"Слово {english_word} удалено.")
    else:
        print(f"Слово {english_word} не найдено в словаре.")

def find_word(english_word):
    if english_word in dictionary:
        print(f"{english_word} => {dictionary[english_word]}")
    else:
        print(f"Слово {english_word} не найдено в словаре.")

def replace_word(english_word, new_french_translation):
    if english_word in dictionary:
        dictionary[english_word] = new_french_translation
        print(f"Перевод слова {english_word} обновлен на {new_french_translation}.")
    else:
        print(f"Слово {english_word} не найдено в словаре.")

add_word("apple", "pomme")
add_word("book", "livre")
find_word("apple")
replace_word("apple", "pomme")
find_word("apple")
delete_word("book")