class User():
    def __init__(self, first_name, last_name, phone_number, mail, about_me):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.mail = mail
        self.about_me = about_me
    def describe_user(self):
        print(self.first_name, self.last_name, self.phone_number, self.mail, self.about_me)
    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}')
    def call_user(self):
        print(f'Вы можете позвонить {self.first_name} {self.last_name} по номеру телефона: {self.phone_number}')
Aleksei = User("Алексей", "Классовый", "89285005578", "alekseiklassoviy@yandex.ru", "Юрист")
Vyacheslav = User('Вячеслав', 'Молотов', '89556179844', 'molotovstolyr@gmail.com', 'Столяр')
Aleksei.describe_user()
Aleksei.greet_user()
Vyacheslav.describe_user()
Vyacheslav.greet_user()
Aleksei.call_user()
Vyacheslav.call_user()