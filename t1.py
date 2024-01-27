food = input("Приём пищи: ").lower()
if food == "завтрак":
    print("Каша")
else:
    wish = input("Хотели бы вы плотно поесть? ")
    if wish == "да":
        print("Советуем плов")
    else:
        print("Советуем котлету с пюре")
