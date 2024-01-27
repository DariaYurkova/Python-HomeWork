
games = []
while True:
    input_game = input("Введите игру(Вводить до 0):")
    if input_game != "0":
        if input_game in games:
            print("Это игра уже есть")
        else:
            games.append(input_game)
            print("Игра добавлена")
    else:
        break
print(games)

        
