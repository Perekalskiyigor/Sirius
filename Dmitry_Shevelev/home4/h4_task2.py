num: int = 1
total: int = 0
while num != 0:  # Пока ввод не равен 0
    num = int(input(">"))  # Вводим числа
    total += num  # Их суммируем, 0 на сумму не влияет
print(total)  # Выводим сумму
