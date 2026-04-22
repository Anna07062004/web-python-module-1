text = "«текст» — это связная последовательность слов или символов, передающая смысл, но также это название романа и фильма Дмитрия Глуховского о студенте, который через телефон обидчика узнает его жизнь, а еще это издательство и типографский шрифт. в лингвистике текст — это сообщения, объединенные связями, имеющие цель и структуру, состоящие из начала, основной части и концовки"
text.split(".")
s = [x.strip() for x in text.split(".") if x.strip()]
text_normalized = ". ".join(x.capitalize() for x in s) + "."
print(text)

count = sum(c.isdigit() for c in text)
print(count)

punct_count = sum(1 for c in text if c in ".,")
print(punct_count)

exc_count = text.count("?")
print(exc_count)