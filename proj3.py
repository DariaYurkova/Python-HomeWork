import random
import time


hp = 20

kit = 2


def room_one():
    correct_answers = 0
    random_effect = random.randint(1, 3)
    if random_effect == 1:
        sleep= int(input("Вы устали, вам нужно поспать, нажмите 7, чтобы поспать"))
        if sleep == 7:
            time.sleep(1)
            print("Вы поспали")
        else:
            print("Вы умерли от недосыпа")
            game_over()

    if random_effect == 2:
        eat = int(input("Вы проголодались,необходимо покушать, нажмите 8, что бы покушать"))
        if eat == 8:
            time.sleep(1)
            print("Вы покушали")
        else:
            print("Вы умерли от голода(")
            game_over()

    if random_effect == 3:
        print("Эх")


    print("Вы как обычно легли спать, но внезапно просыпаетесь от шума, и оказываетесь в незнакомом Вам месте.\n"
          "Вы напуганы, но решили осмотреть местность. Вы понимаете, что находитесь в тёмной комнате, Ваше зрениеz\n"
          "пытается привыкнуть к темноте,и как только это происходит, Вы видите перед собой старика. Вы пытаетесь с ним\n"
          " поговорить, но он не собирается отвечать на Ваши вопросы. Спустя несколько минут молчания, старик говорит:\n "
          "Чтобы пройти эту комнату, тебе, нужно решить мои загадки,"
          "Вот моя первая загадка: Я иду, но никогда не прихожу. Что я?", name)
    print("1. Дорога")
    print("2. Время")
    print("3. День")
    answer = int(input("Выберите номер правильного ответа: "))
    if answer == 2:
        correct_answers += 1
        print("Правильно! Посмотрим как ты справишься со следующей загадкой")


    print("Моя вторая загадка: Я могу летать без крыльев, Я могу плакать без глаз. Что я?")
    print("1. Воздух")
    print("2. Небо")
    print("3. Мысли")
    answer = int(input("Выберите номер правильного ответа: "))
    if answer == 3:
        correct_answers += 1
        print("Правильно!Неплохо, что скажешь на счёт следующей?")


    print("Моя третья загадка: На деревья, на кусты с неба падают цветы. Белые, пушистые, только не душистые. Что это?")
    print("1. Цветы")
    print("2. Снег")
    print("3. Дождь")
    answer = int(input("Выберите номер правильного ответа: "))
    if answer == 2:
        correct_answers += 1
        print("Правильно!Чтож, ты решил все мои загадки")


    if correct_answers >= 2:
        print("Вы решили достаточно загадок и перед вами предстаёт призрак,он охраняет комнату загадок,"
              "его зовут Гидеон. Он проводит вас в следующую комнату, дверь открыта!")
        room_two()
    else:
        print("Вы решили недостаточно загадок,дверь остаётся закрытой.")


def room_two():

    random_effect = random.randint(1, 3)
    if random_effect == 1:
        sleep= int(input("Вам необходимо поспать, нажмите 7, чтобы поспать"))
        if sleep == 7:
            time.sleep(1)
            print("Вы поспали")
        else:
            print("Вы умерли от недосыпа")
            game_over()

    if random_effect == 2:
        eat = int(input("Вам необходимо покушать, нажмите 8, чтобы покушать"))
        if eat == 8:
            time.sleep(1)
            print("Вы покушали")
        else:
            print("Вы умерли от голода(")
            game_over()

    if random_effect == 3:
        print("Эх")


    print("Перед Вами комната с 8 зеркалами.Вся комната была освещена факелами. В ней Вы встречаете призрака,\n "
          "стража этой комнаты. Он был в хорошем настроении.""Как только он Вас заметил, сказал: \n"
          "Одно из зеркал ведет на другой уровень, а остальные - ловушки. Тебе просто нужно "
          "угадать какое зеркало правильное.")
    note=1
    correct_mirror = random.randint(1, 8)

    while True:

        chosen_mirror = int(input("Выберите номер зеркала от 1 до 8 или вы можете осмотреть комнату, для этого нажмите 9 "))

        if chosen_mirror == correct_mirror:
            print("Поздравляю! Вы нашли зеркало, которое ведет на другой уровень, - скакзал Гидеон и проводил \n"
                  "Вас в следующую комнату")
            room_three()
        elif chosen_mirror != correct_mirror and chosen_mirror !=9:
            print("Вы выбрали неверное зеркало и возвращаетесь назад в предыдущую комнату.")


        if chosen_mirror == 9:
            choice=int(input("Вы нашли записку, прочесть ее? 1-да, 2-нет"))
            if choice==1 and note==1:
                print("В записке было следующее: Покажи меня Гидеону. Вы последовали указанию записки и отдали её призраку.\n"
                      "Гидеон её забрал и сказал Вам номер правильного зеркала", correct_mirror)
            if choice==1 and note==0:
                print("Вы уже прочли записку")
            if choice==2:
                print("Ну удачи)")



def room_three():
    random_effect = random.randint(1, 3)
    if random_effect == 1:
        sleep= int(input("Вам необходимо поспать, нажмите 7, чтобы поспать"))
        if sleep == 7:
            time.sleep(1)
            print("Вы поспали")
        else:
            print("Вы умерли от недосыпа")
            game_over()

    if random_effect == 2:
        eat = int(input("Вам необходимо покушать, нажмите 8, чтобы покушать"))
        if eat == 8:
            time.sleep(1)
            print("Вы покушали")
        else:
            print("Вы умерли от голода")
            game_over()

    if random_effect == 3:
        print("Эх")


    print("Вы попали в следующую комнату. Здесь темно, а в воздухе витает ужасный запах. Немного подаждав, когда глаза\n"
          " привыкнут к темноте, Вы замечаете чей-то силуэт. Вы решили подойти поближе, и как только сделали шаг,\n"
          "в комнате зажглись факелы, и Вы увидели страшного монстра. Гидеон, уходя, Вас предупредил: \n" 
          "У него 10 HP, у вас 20 HP, Вам нужно его победить. У вас есть 2 аптечки.")
    hp = 20
    hp_enemy = 10
    kit = 2

    while hp >= 0 and hp_enemy >= 0:
        print("Нажмите 1, чтобы атаковать монстра, 2, чтобы использовать аптечку (у вас", kit, "аптечек)")
        choice = input()

        enemy_damage = random.randint(1, 3)
        hp -= enemy_damage
        print("Враг атаковал вас и нанес", enemy_damage, "урона. Ваше текущее HP:", hp)

        if choice == "1":
            damage = random.randint(1, 3)
            hp_enemy -= damage
            print("Вы нанесли", damage, "урона. У врага осталось", hp_enemy, "HP.")

        elif choice == "2":
            if kit > 0:
                heal = random.randint(1, 3)
                hp += heal
                kit -= 1

                print("Вы использовали аптечку и восстановили", heal, "HP. Ваше текущее HP:", hp)
            else:
                print("У вас больше нет аптечек. Вы не можете использовать их.")



        else:
            print("Выберите действие, нажав 1, 2 ")

    if hp_enemy <= 0:
        print("Внезапно появляется Гидеон, - Вы победили монстра, а значит, сможете покинуть это место.\n"
              "Вас начинае клонить в сон, Вы засыпаете. Как только Вы открыли глаза, Вы оказались в своей комнате,\n2"
              "а всё, что происходило с Вами, оказалось сном.")
        win()

    if hp <= 0:
        print("Вы погибли.")
        game_over()

def game_over():
    x=int(input("игра окончена, нажмите 1 для продолжения: "))
    if x==1:
        room_one()
    else:
        menu()


def win():
    x=int(input("Вы выиграли нажмите 1 для продолжения или 0, чтобы вернуться в меню "))
    if x==1:
        room_one()
    else:
        menu()



name=""

def menu():
    print("Добро пожаловать в игру!")
    print("1. Начать игру")
    print("0. Выйти")
    choice = int(input("Выберите действие: "))
    if choice==1:
        global name
        name=input("Введите Имя: ")
        room_one()
    else:
        print("досвидание")



menu()


    
















