num = int(input("Введите 4-хзначное число: "))
a = num % 10
b = num // 1000
c = num // 100 % 10
d = num // 10 % 10

print(f"{a} {b} {c} {d}")