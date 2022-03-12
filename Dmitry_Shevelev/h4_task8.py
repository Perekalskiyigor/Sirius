s: list = list(input(">"))
total: list = []
times = 0  # Вводим переменные

for x in s:
    times += 1
    if times == 1:
        total.append(x)
        total.append("1")  # Первый раз добавляем элемент
    else:
        if total[-2] != x:
            total.append(x)
            total.append("1")  # Добавляем новый элемент
        else:
            total.append(str(int(total[-1]) + 1))
            del(total[-2])  # Если повторяется, то добавляем кол-во

print(''.join(total))  # Выводим строкой
