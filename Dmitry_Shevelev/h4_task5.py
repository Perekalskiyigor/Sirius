print("Блок на числа:")
a: int = int(input("От числа>"))
b: int = int(input("До числа>"))
print("На числа:")
c: int = int(input("От числа>"))
d: int = int(input("До числа>"))  # Вводим переменные

factor1: list = list(range(a, b+1))
factor2: list = list(range(c, d+1))  # Диапазон чисел в листы

print(" ", end="\t")  # Угловая клетка
for x in factor1:
    if x != b:
        print(x, end="\t")  # Выводим шапку таблицы вместо концов TAB
    else:
        print(x)  # Последний элемент шапки, конец - обычный

for y in factor2:
    print(y, end="\t")  # Выводим заданные столбцы
    for x in factor1:
        if x != b:
            print(y*x, end="\t")  # Выводим содержимое таблицы вместо концовTAB
        else:
            print(y*x)  # Последний элемент содержимого, конец - обычный
