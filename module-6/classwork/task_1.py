my_set = {1,2,3}
print(3 in my_set)
print(5 not in my_set)
#Длина множеств
print(len(my_set))
#Cумма множеств
print(sum(my_set))
#Min/max число в множество
print(min(my_set), max(my_set))

for num in my_set:
    print(num)

#Операция над множествами
#4.Симметрическая разность
set_a = {1,2,3,4}
set_b = {3,4,5,6}
#Метод
result = set_a.symmetric_difference(set_b)
#Оператор
result_operator = set_a ^ set_b
#Присвоение
set_a ^= set_b

print(set_a, result, result_operator)

#3.Разность
set_a = {1,2,3,4}
set_b = {4,5,6,7}
#Метод
result = set_a.difference(set_b)
#Оператор
result_operator = set_a - set_b
#Присвоение
set_a -= set_b

print(set_a, result, result_operator)

#2. Пересечения
set_a = {1,2,3,4}
set_b = {3,4,5,6,7}
#Метод
result = set_a.intersection(set_b) 
#Оператор
result_operator = set_a & set_b
#Присвоение
set_a &= set_b

print(set_a, result, result_operator)
#1. Объединение
set_a = {1,2,3,4}
set_b = {4,5,6,7}
#Метод
result = set_a.union(set_b) 
#Оператор
result_operator = set_a | set_b
#Присвоение
set_a |= set_b
print(set_a, result, result_operator)

#Удаление элементов
# fruits = {"яблоко", "банан", "апельсин"}
# fruits.remove("яблоко")
# fruits.discard("груша")
# fruits.pop()
# print(fruits)

#Добовление элементов
# fruits = {"яблоко", "банан", "апельсин"}
# fruits.add("груша")
# fruits.update(["смородина", "клубника"])
# print(fruits)

#Генератор множеств
# my_set = {x for x in range(5)}
# print(my_set)

#------------------------
# set_tuple = set((1,1,2,2,3))
# print(set_tuple)

#------------------------
# letters = set("привет")
# print(letters)

#------------------------
# my_set_1 = set([1,2,3,3,4])
# print(my_set_1)

#------------------------
# my_set = {1,1,2,2,3,3}
# print(my_set)
