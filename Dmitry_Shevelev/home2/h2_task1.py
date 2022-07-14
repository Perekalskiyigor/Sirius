word_list: list = []
new_wl: list = []
new_el: str = "_"  # Задаём переменные
while new_el != "":
    new_el: str = input("Ещё слово? >")  # Пока строка ввода не пустая - всё ок
    if new_el != "":
        word_list.append(new_el)  # Если строка не пустая - добавляем в лист
print("Список:", word_list)  # Его выводим
for x in word_list:
    if new_wl.count(x) == 0:
        new_wl.append(x)  # Если кол-во элемента = 0, то добавляем во 2-ой лист
for word in new_wl:
    print(word)  # Выводим каждое слово
