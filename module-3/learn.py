# text = "row_1\nrow_2\nrow_3"

# print(text[0:7])
# print(text[0:3])
###############################################################################################

# tuple_1_sym = ("b")
# tuple_2_sym = ("b",)
# print(tuple_1_sym, tuple_2_sym)

# #кортежи в цикле(итерирование)
# num_tuple = tuple(range(0,5))
# for index, num in enumerate(num_tuple):
#     print()

# #методы кортежей
# numbers = (1,2,3,2,4,5,2)
# print(numbers.count(2)) ##Считаем количество
# print(numbers.index(2)) ##Индекс первого вхождения поиск

# #повторение

# # pattern = ("a", "b")
# # pereated = pattern * 2
# # print(pereated)

# #пренадлежность
# f = ("appele", "banana")
# print("apple" in f)

  #объединение
# tuple1 = (1,2)
# tuple2 = (3,4)
# result = tuple1 + tuple2
# print(result)

# num1, _, num3, num4 = (1,2,3,4)
# print(num1, num3, num4)
# num1, *other, lest_el = tuple(range(0, 11))

# print(num1, other, lest_el)



###############################################################################################

#Разбиение и объединение
# sl = text.splitlines()
# print(sl)

 #Если пусто то разбивается по пробелы
# f = text.split(", ")

#Объединение элементов в строку
# u = ", ".join(f) 
# print(f, u)

###############################################################################################

#Очистка
#Очистка с левой и правой части
# print(text.strip()) 

#Очистка левой части
# print(text.lstrip())
 
#Очистка правой части
# print(text.strip())

###############################################################################################

# print("Пробелы: ", text.isspace())
# print("Только буквы и цифры: ", text.isalnum())
# print("Только буквы: ", text.isdigit())
# print("Только буквы: ", text.isalpha())
# print("Заглавные: ", text.isupper())
# print("Прописные: ", text.islower())

###############################################################################################

#изменение регистра
# print(text.swapcase())
# print(text.upper())
# print(text.lower())

###############################################################################################

#Поиск
# print(text.index("j"))
# print(text.find("p"))

###############################################################################################

#Замена
# print(text.replace("pyt", "213", 2))