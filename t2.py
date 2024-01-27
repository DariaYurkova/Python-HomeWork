chek_sum = int(input("Введите сумму:"))
time_work = int(input("Введите часы работы:"))
if 10 < time_work and time_work < 13:
    print(chek_sum/2)
elif 20 < time_work and time_work < 23:
    print(chek_sum/4)
elif 8 < time_work and time_work < 10 or 13 < time_work and time_work < 21:
    print(chek_sum)