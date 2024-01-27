"""
Дана строка чисел от 0 до 9 необходимо создать словарь где в качестве ключа будет цифра,
а в качестве значения количество этих цифр в строке
"""
numbers = "0139412831055230677798"

dict = {
    0: numbers.count(0),
    1: numbers.count(1),
    2: numbers.count(2),
    3: numbers.count(3),
    4: numbers.count(4),
    5: numbers.count(5),
    6: numbers.count(6),
    7: numbers.count(7),
    8: numbers.count(8),
    9: numbers.count(9)
}