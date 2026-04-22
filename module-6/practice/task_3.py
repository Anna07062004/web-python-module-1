fruits_count = ["banan", "apple", "bananamango", "mango", "strawberry-banana"]
fruits = input("Введите название фрукта: ")

count = 0

for item in fruits_count:
    if fruits in item:
        count += 1
print(count)
