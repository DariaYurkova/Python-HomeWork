fives = 0
res = []
while True:
    nums = int(input("Введите оценки:"))
    res1 = res.append(nums)
    if 5 in res:
        fives += 1
    if nums == 0:
        res.pop(-1)
        break
len = len(res)
res = 100 // len(int(res1)) * len(int(res))
print(res)
