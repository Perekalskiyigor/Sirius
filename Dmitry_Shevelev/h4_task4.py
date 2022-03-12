num: int = 0
total: int = []  # Вводим переменные
while num <= 100:
    num = int(input("Ещё число? >"))  # Пока строка ввода не пустая - всё ок
    if num >= 10 and num <= 100:
        total.append(num)  # Если число меньше 10 и больше 100-не берём
for x in total:
    print(x)  # Выводим по отдельности
