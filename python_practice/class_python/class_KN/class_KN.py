

# KN(缩写） Knowledge Node
# ython与面向对象

# 三种变量

class House:
    # 静态属性 -> 变量 ，类变量，在类之中，方法之外
    door = "red"

    # 实例变量， 类体中，方法之内， 以"self.变量名的方式去定义"，实例变量的作用域为这个类中的
        self.yangtai = "大"

    def sleep(self):
        yangtai = "aaaa"
        # 普通变量， 在类之中、方法之中，并且不会以self.


# 构造函数

class House:

    # 静态属性 -> 变量 ，类变量，在类之中，方法之外
    door = "red"
    floor = "white"
    # 构造函数，是在类实例化的时候直接执行
    def __init__(self):
    # 实例变量， 类体重，方法之内， 以"self.变量名的方式去定义"，实例变量的作用域为这个类中的
    # 所有方法
        print(self.door)
