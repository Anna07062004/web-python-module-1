num = [3, 5, 0, 8, -3, 1, -7]
print(num)

min_val = num[0]
max_val = num[0]
neg_count = 0
pos_count = 0
zero_count = 0

for num in num:
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num
    
    if num < 0:
        neg_count += 1
    elif num > 0:
        pos_count += 1
    else:
        zero_count += 1

print(f"min: {min_val}")
print(f"max: {max_val}")
print(f"Отрицательные: {neg_count}")
print(f"Положительные: {pos_count}")
print(f"Кол-во нулей: {zero_count}")