#Задача 5*: Число делится на 6 при соблюдении 2 условий:
# 1 – последняя его цифра четная
# 2 – сумма всех его чисел делится на 3

num = int(input("Введите число:"))
res = 0
res2 = 1
if num > 0:
    dig = num % 10
    res = res + dig
    res2 = res2 * dig
    num = num // 10
if dig // 2 == 0 and res // 3 == 0:
    print("Ваше число делится на 6")
else:
    print("Ваше число не делится на 6")
#pass