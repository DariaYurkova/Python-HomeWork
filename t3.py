t1 = float(input("Введите цену первого товара: "))
t2 = float(input("Введите цену второго товара: "))
t3 = float(input("Введите цену третьего товара: "))
if t1 < t2 and t2 < t3:
    print("Акция!" , round((t1+t2+t3)/2, 2))
elif t1 > t2 and t2 > t3:
    print("Акция!" , round((t1+t2+t3)/2, 2))
else:
    print(t1+t2+t3)