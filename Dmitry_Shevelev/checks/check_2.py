import requests


def friend_add(a, b):
    resp = requests.get(f'https://api.vk.com/method/friends.add?user_id={a}&text={b}&access_token=6954338eaf791248224605877613e24433b1a2a227838bc168e0f0e8fa5ca6965c724cfb66f2ffe2554ae&v=5.131')


def check_add():
    while True:
        resp = requests.get('https://api.vk.com/method/friends.add?user_id=94341903&text=&access_token=61534bf42584a814300e9517eeb29c9918a2cea4856ac585cc9764b327630937bd6f8560febc899f12408&v=5.131')
        resp1 = resp.json()
        current_n = resp1
        past_n = 0
        # print(resp1)
        if current_n != past_n:
            current_n = past_n
        else:
            if resp1['response'] == 1:
                print("ЖДИ! Я получил заявку!")
            elif resp1['response'] == 2:
                print("Ну ты же мог подождать. Я уже принял.")
            elif resp1['response'] == 4:
                print("Повторная отправка заявки")
            else:
                print('Доступ в сеть ограничен.')


check_add()
