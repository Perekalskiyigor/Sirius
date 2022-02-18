num: int = int(input("Введите положительное трёхзначное число >"))  # Вводим
a: int = num // 100
b: int = num // 10 % 10
c: int = num % 10  # Получаем цифры
print(f"{a}{b}{c}",
      f"{a}{c}{b}",
      f"{b}{a}{c}",
      f"{b}{c}{a}",
      f"{c}{a}{b}",
      f"{c}{b}{a}", sep="\n")  # Выводим
