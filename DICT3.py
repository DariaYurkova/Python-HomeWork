"""
Напишите программу принимающую ввод информации о треке(место в чарте,исполнитель, название) пока пользователь
не введет "off". Программа должна вывести всю информацию в виде словаря вида: {(место,испонитель): название трека}
"""

name_list = []
place_list = []
autor_list = []
while True:
    name = input("Введите название трека(Для завершения введите off):")
    if name != "off":
        name_list.append(name)
        place = input("Введите место в чарте:")
        place_list.append(place)
        autor = input("Введите исполнителя:")
        autor_list.append(autor)
    else:
        break
dict = {
    name_list[0]: [place_list[0], autor_list[0]],
    name_list[1]: [place_list[1], autor_list[1]],
    name_list[2]: [place_list[2], autor_list[2]],
    name_list[3]: [place_list[3], autor_list[3]],
}
print(dict)
