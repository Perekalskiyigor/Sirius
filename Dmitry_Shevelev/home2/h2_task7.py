place: int = int(input("Номер места >"))  # Вводим переменную
coupe: int = (place - 1) // 4 + 1  # Считаем купе
print(coupe)  # Выводим её номер
