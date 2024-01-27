#Задача "Новая акция"
sum1 = 0
summa = []
while True:
    sum1 = int(input("Введите стоимость товара(Вводить до 0):"))
    summa.append(sum1)
    if sum1 == 0:
        break
if summa[0] > summa[1] and summa[1] > summa[2]:
    print("Акция!\nВаша скидка равна 50%!\nИтого к оплате:", sum(summa) / 2)
elif summa[0] < summa[1] and summa[1] < summa[2]:
    print("Акция!\nВаша скидка равна 66!\nИтого к оплате:", sum(summa) / 3)
else:
    print("Итого к оплате:", sum(summa))