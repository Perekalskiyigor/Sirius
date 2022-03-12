a: int = int(input("Введите кол-во биологов >"))
b: int = int(input("Введите кол-во информатиков >"))  # Вводим переменные
noda: int = a
nodb: int = b
while noda != nodb:
    if noda > nodb:
        noda = noda - nodb
    else:
        nodb = nodb - noda  # Используем алгоритм Евклида
pieces = a*b//noda   # Через НОД получаем НОК
print(pieces)  # Выводим кол-во кусочков или НОК
