file_path = "isxod.txt"

max_length = 0

with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        line_length = len(line.rstrip("\n"))
        if line_length > max_length:
            max_length = line_length

print(f"Длина самой длинной строки: {max_length}")