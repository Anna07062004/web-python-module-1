text = input("Введите текст: ")
sen_count = 0

for char in text: 
    if char in ".!?":
        sen_count += 1

if text and text[-1] not in ".!?":
    sen_count += 1
print(sen_count)