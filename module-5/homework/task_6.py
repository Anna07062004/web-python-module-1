dictionary = {}

def add_word(english_word, french_translation):
    if english_word in dictionary:
        print(f"'{english_word}' уже есть в словаре.")
    else:
        dictionary[english_word] = french_translation
        print(f"Добавлено: {english_word} -> {french_translation}")

def delete_word(english_word):
    if english_word in dictionary:
        del dictionary[english_word]
        print(f"'{english_word}' удалено из словаря.")
    else:
        print(f"'{english_word}' не найдено в словаре.")

def find_word(english_word):
    translation = dictionary.get(english_word)
    if translation:
        print(f"{english_word} -> {translation}")
    else:
        print(f"'{english_word}' не найдено в словаре.")

def update_word(english_word, new_french_translation):
    if english_word in dictionary:
        dictionary[english_word] = new_french_translation
        print(f"Обновлено: {english_word} -> {new_french_translation}")
    else:
        print(f"'{english_word}' не найдено в словаре.")

add_word("apple", "pomme")
add_word("orange", "orange")
find_word("apple")
update_word("apple", "pomme rouge")
delete_word("orange")
find_word("orange")