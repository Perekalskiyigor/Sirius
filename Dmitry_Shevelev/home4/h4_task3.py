from math import lcm  # Импортируем НОД из стандартной библиотеки питона
a: int = int(input("Введите кол-во биологов >"))
b: int = int(input("Введите кол-во информатиков >"))  # Вводим переменные
print(lcm(a, b))  # Выводим кол-во кусочков или НОД
