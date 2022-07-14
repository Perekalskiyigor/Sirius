line: list = list(input(">").lower())  # Вводим список, занижаем в регистре
sum = line.count("c") + line.count("g")  # Считаем кол-во "c" и "g"
print(sum/len(line)*100)  # Выводим процентное содержание
