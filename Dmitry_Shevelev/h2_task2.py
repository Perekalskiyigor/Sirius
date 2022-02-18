n_list: list = []
right_nl: list = []
new_el: int = 0  # Задаём переменные

while new_el != "":
    new_el: int = input("Ещё число? >")  # Пока строка ввода не пустая - всё ок
    if new_el != "":
        n_list.append(int(new_el))  # Если строка не пустая - добавляем в лист
print("Список:", n_list)  # Его выводим

for x in n_list:
    if x < 0:
        right_nl.append(x)  # Добавляем отрицательные числа в лист
for x in n_list:
    if x == 0:
        right_nl.append(x)  # Добавляем нули в лист
for x in n_list:
    if x > 0:
        right_nl.append(x)  # Добавляем положительные числа в лист
for x in right_nl:
    print(x)  # Всё выводим
