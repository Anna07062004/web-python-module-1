input_file = "isxod2.txt"
output_file = "new.txt"

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

if lines:
    lines.pop()

with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(lines)

print("Готово")