import random
from random import randint


def password(num):
    pas = ''
    for i in range(num):
        pas = pas + random.choice('1234567890abcdefghijklmnopqrstuvwxyz!@,.')
    return pas

num = int(input('Введите желаемую длину пароля'))
print(password(num))
