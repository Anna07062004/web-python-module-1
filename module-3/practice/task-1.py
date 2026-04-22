text = input("Введите строку: ")
text_lower = text.lower()
if text_lower == text_lower[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")