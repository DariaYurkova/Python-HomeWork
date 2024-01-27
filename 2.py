"""
2.	Номерной знак имеет вид Х000ХХ00 где Х – буква от А до Я, а 0 – цифра от 0 до 9.
Напишите функцию генерирующую случайный номерной знак.
"""
import random
from random import randint

def license_plate(pas):
    num =''
    for i in range(1):
        num += random.choice('абвгдеёжзийклмнопрстуфхцчшщыэюя')
    return num
print(license_plate())
pas = int(input())

def num_gen(pas):
    num_2 = ''
    for i in range(3):
        num_2 += random.choice('0123456789')
    return num_2
print(num_gen())
