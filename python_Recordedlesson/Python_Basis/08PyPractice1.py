"""
计算出1-100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""
import random
computer_number = random.randint(1, 100)
while True:
    person_number = int(input("请输入你要猜的1到100的整数："))
    if computer_number > person_number:
        print("再大一点")
    elif computer_number < person_number:
        print("再小一点")
    elif computer_number == person_number:
        print("猜对了")
        break
print("我是计算机数字：", computer_number)