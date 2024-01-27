#Рекомендации товаров
categ = input("Введите категорию товара:").lower()
price = 0
if categ == "продукты":
    price = float(input("Введите цену:"))
    if price < 101:
        print("Попробуйте нашу выпечку!")
    elif price > 99 and price < 501:
        print("Как насчёт орехов в шоколаде?")
    elif price > 499:
        print("Попробуйте экзотические фрукты!")
else:
    print("Загляните в товары для дома!")
