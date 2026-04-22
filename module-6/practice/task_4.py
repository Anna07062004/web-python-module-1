car_br = ["Тойота", "Форд", "Вольво", "Мазда"]
name_car = input("Введите название производителя: ")
rep = input("Введите слово для замены: ")

new_br = []
for car in car_br:
    if car == name_car:
        new_br.append(rep)
    else:
        new_br.append(car)

print(new_br)



