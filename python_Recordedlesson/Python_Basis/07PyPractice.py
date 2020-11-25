"""
计算出1-100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""
import random

i = 0
while True:
    i = i+1
    print("第{}回合".format(i))
    a = random.randint(1, 100)
    b = int(input("input:"))
    print("随机数：", a)
    print("你猜的是：", b)
    if a < b:
        print("你猜大了一点")
    elif b == a:
        print("优秀，你猜对喽")
    else:
        print("你猜小了一点")
    if i == 4:
        break

