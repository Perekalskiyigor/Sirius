n: int = int(input("Население Вселенной>"))  # Вводим переменную
alive_n: int = n // 2 + n % 2  # Считаем выживших, округляя в большую сторону
print(alive_n)  # Выводим это кол-во