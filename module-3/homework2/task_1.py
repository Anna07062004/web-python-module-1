num = input("Введите арифметическое выражение: ")

if "+" in num:
    num1, num2 = num.split("+")
    result = float(num1) + float(num2)
elif "-" in num:
    num1, num2 = num.split("-")
    result = float(num1) - float(num2)
elif "*" in num:
    num1, num2 = num.split("*")
    result = float(num1) * float(num2)
elif "/" in num:
    num1, num2 = num.split("/")
    if float(num2) == 0:
        print("Ошибка")
    else:    
        result = float(num1) / float(num2)
else:
    print("Неверная операция, проверьте и попробуйте снова")

print(result)