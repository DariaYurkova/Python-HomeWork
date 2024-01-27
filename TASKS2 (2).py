#Успеваемость
res = []
while True:
    input_res = int(input("Введите оценку(Вводить до 0):"))
    res.append(input_res)
    if input_res == 0:
        res.pop(-1)
        break
print(sum(res) / len(res) * 100)

