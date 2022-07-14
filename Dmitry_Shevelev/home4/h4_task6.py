a: int = int(input("Число>"))
b: int = int(input("Число>"))  # Вводим переменные
range: list = list(range(a, b+1))  # Диапазон чисел в лист
range2: list = []
sum: int = 0  # Ещё немного переменных
for x in range:
    if x % 3 == 0:
        range2.append(x)
        sum += x  # Если кратно 3, то добавляем в лист и суммируем
print(sum/len(range2))  # Выводим среднее арифметическое
