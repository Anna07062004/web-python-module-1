number = input("Введите четырёхзначное числа: ")
product = 1
for digit in number:
    product *= int(digit)

print(product)    

