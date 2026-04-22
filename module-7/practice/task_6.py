input_file = "isxod.txt"
output_file = "new.txt"

word_find = input("Что искать? ").strip()
word_replace = input("На что заменить? ").strip()

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

content_new = content.replace(word_find, word_replace)

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(content_new)

print("Замена завершена. Результат сохранен в файл.")