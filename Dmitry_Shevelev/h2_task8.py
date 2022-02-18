minutes: int = int(input(">"))  # Вводим минуты
hours: int = minutes // 60  # Считаем часы
rem_min: int = minutes % 60  # Считаем остаток
print(f"{minutes} мин - это {hours} час {rem_min} минут.")  # Выводим как надо
