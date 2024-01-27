import re
from datetime import datetime

schedule = {
    'понедельник': '14:00 - 16:00',
    'вторник': '16:30 - 18:30',
    'среда': '10:00 - 12:00',
    'четверг': '18:00 - 20:00',
    'пятница': '13:00 - 15:00',
}

contacts = {
    'имя': 'Иван',
    'фамилия': 'Иванов',
    'телефон': '+7 (123) 456-78-90',
    'email': 'ivanov@example.com',
}

payment_amount = 1000

people = 0
visitors = int(input('Введите количество посетителей:'))
if visitors > 0 :
    people += visitors


def handle_request(request):
    for day, time in schedule.items():
        if re.search('расписание', request, re.IGNORECASE):
            print(f"Расписание занятий на {day}: {time}")
        if re.search('контакты', request, re.IGNORECASE):
            print(f"Контакты тренера: {contacts}")
        if re.search('сумма', request, re.IGNORECASE):
            print(f"Сумма оплаты за занятие: {payment_amount}")
        if re.search('посетители', request, re.IGNORECASE):
            print(f"Количество посетителей:", people )

request = input("Введите ваш запрос: ")
handle_request(request)