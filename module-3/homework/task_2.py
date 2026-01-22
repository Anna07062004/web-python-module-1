text = input("Введите текст: ")
reserved = input("Введите зарезервированные слова через пробел: ").split()
words = text.split()
result_words = []

for word in words:
    clean_word = word.strip(".,!?\"'()[]{}:;")
    if clean_word.lower() in [r.lower() for r in reserved]:
        result_words.append(word.upper())
    else:
        result_words.append(word)

result = " ".join(result_words)

print(result)