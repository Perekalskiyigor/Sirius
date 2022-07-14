import requests
resp = requests.get('https://www.swapi.tech/api/starships/')
resp = resp.json()

one = resp['results']
cur_ids = []

for x in one:  # Для каждого словаря в списке
    if x['uid'] == one[-1]['uid']:  # Если айди последний то ставим ": "
        print(x['uid'], end=": ")
    else:
        print(x['uid'], end=", ")  # В остальных случаях ", "
    cur_ids.append(x['uid'])  # Добавляем айди в список
print("IDs на данный момент")

ship_id = input("Введите один из ids >")
if ship_id in cur_ids:  # Если такой индекс существует
    ship_data = one[cur_ids.index(ship_id)]
    # Получаем словарь из списка по индексу айди в cur_ids
    print(f"name: {ship_data['name']} \n"
          f"id: {ship_data['uid']} \n"
          f"url: {ship_data['url']}")  # Выводим данные корабля
else:
    print('ТЫ НЕ ЕШЬ ГРИБЫ?')  # Если айди нет
