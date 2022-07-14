num_line: str = input(">")
total1: int = 0
total2: int = 0  # Задаем переменные
for x in num_line[:3]:
    total1 += int(x)  # Сумма первых трёх
for x in num_line[3:6]:
    total2 += int(x)  # Сумма вторых трёх
if total1 == total2:
    print("Счастливый")  # Если равны, то выводим "Cчастливый"
else:
    print("Обычный")  # Если нет, то выводим "Обычный"
