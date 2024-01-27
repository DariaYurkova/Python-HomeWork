i = input("Введите game (off -игра завершится) ")
if i == 'game':
    print("Игра: Угадай число!")
rep = 0
while rep != 3:
    game = int(input("Введите число: "))
    rep += 1
    if game == 5:
        print("Вы выиграли билеты на концерт!")
    elif rep == 3:
        print("Вы проиграли( ")