input_file = "isxod.txt"
output_file = "stata.txt"

num_symbols = 0
num_lines = 0
num_vowels = 0
num_consonants = 0
num_disits = 0

vowels = "аеёиоуыэюяaeiou"
consonants = "бвгджзйклмнпрстфхцчшщбвгджзйклмнпрстфхцчшщ"

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        num_lines += 1
        num_symbols += len(line)
        for char in line.lower():
            if char in vowels:
                num_vowels += 1
            elif char.isalpha() and char not in vowels:
                num_consonants += 1
            elif char.isdigit():
                num_disits += 1

with open(output_file, "w", encoding="utf-8") as f:
    f.write(f"Количество символов: {num_symbols}\n")
    f.write(f"Количество строк: {num_lines}\n")
    f.write(f"Количество гласных букв: {num_vowels}\n")
    f.write(f"Количество согласных букв: {num_consonants}\n")
    f.write(f"Количество цифр: {num_disits}")
    
print("Статистика записана в файл")