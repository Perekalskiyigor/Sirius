words: list = []
while len(words) < 3:
    words.append(input(">"))  # Считывание и добавление в список
for c in words:
    print(c)  # Вывод строк по очедеди
