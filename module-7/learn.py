# file = open("file.txt", "r")
# print(file.read(1))
# print(file.read(1))
# file.close()

# r - чтение
# w - запись (с очисткой)
# a - дозапись текста в конец файла
# x - создает новый файл
# t - текстовый режим 
# b - бинарный режим
# + - чтение и запись

#----------------------------------
#Лучший способ
#file = open("C:/Windows")

#Экранирование
#file = open("C:\\Windows")

# ошибка
# file = open("C:\Windows")

#----------------------------------

# file = open("file.txt", "w")
# file.write("54321")
# file.close()

#вышло: 54321
#----------------------------------

# file = open("file.txt", "a", encoding="utf-8")
# file.write("- добавили в конец")
# file.close()

#вышло с первым: 54321 - добавили в конец 

#----------------------------------

# f = open("file.txt", "a", encoding="utf-8")
# f.write("1,2,3\n")
# f.write("4,5,6\n")
# f.write("7,8,9")
# f.close()

# f = open("file.txt", "r", encoding="utf-8")
# print(f.readline().strip())
# print(f.readline().strip())

# старый способ
# for line in f:
#     print(line.strip())

# современный споcоб
# with open("file.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())