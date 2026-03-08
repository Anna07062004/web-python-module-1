file_path = "isxod.txt"

search_word = input("Введите слово для поиска: ").lower()

count = 0

with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        words = line.lower().split()
        count += words.count(search_word)

print(f"Слово {search_word} встречается {count} разa")