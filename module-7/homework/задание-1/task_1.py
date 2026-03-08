file1_path = "file1.txt"
file2_path = "file2.txt"

with open(file1_path, "r", encoding="utf-8") as f1, open(file2_path, "r", encoding="utf-8") as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

min_length = min(len(lines1), len(lines2))

for i in range(min_length):
    if lines1[i] != lines2[i]:
        print(f"Несовпадающая строка: Файл 1: {lines1[i]}, Файл 2: {lines2[i]}")
        break
else:
    if len(lines1) != len(lines2):
        if len(lines1) > len(lines2):
            print(f"Файл 1 содержит дополнительную строку: {lines1[min_length]}")
        else:
            print(f"Файл 2 содержит дополнительную строку: {lines2[min_length]}")
    else:
        print("Все строки совпадают")