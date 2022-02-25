a: int = int(input("Первой число =>"))
b: int = int(input("Второй число =>"))
c: int = int(input("Третье число =>"))  # Вводим числа
check_list: list = sorted([a, b, c])  # Их сортируем по возрастанию
print(check_list[2])
print(check_list[0])
print(check_list[1])  # Выводим макс, мин, остав число
