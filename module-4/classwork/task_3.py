def sum(a, b):
    if a == b:
        return a
    
    else:
        return a + sum(a + 1, b)
    
a = int(input("Введите начало диапозона: "))
b = int(input("Введите начало диапозона: "))

result = sum(a, b) 
print(f"Сумма от {a} до {b} = {result}")