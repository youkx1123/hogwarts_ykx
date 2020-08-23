#面向对象
#定义一个类
class House:
    #静态属性-》变量,类变量-》在类之中，方法之外
    door = "red"
    floor = "white"

    def _int_(self):
        #实例变量，类之中，方法之内以"self.变量名的方式定义"，实例变量的作用域为这个类中的
        # 所有方法
        # 实例变量， 类体重，方法之内， 以"self.变量名的方式去定义"，实例变量的作用域为这个类中的
        print("我是self.door",self.door)
        self.yangtai = "大"


    #动态属性-》方法（函数）
    def sleep(self):
        #普通变量-》类之中，方法之中，并且不在self
        self.shuijiao = "房子是用来睡觉的"

    def cook(self):
        print("房子可以用来做饭吃")
        print(self.shuijiao)

north=House()
#如果方法A使用方法B中的实例变量，需要先声明方法B，在调用方法B中的实例变量
#或者把实例变量放入构造函数中(构造函数在实例化时直接被执行，变量会被声明，直接可以调用)

north.sleep()
north.cook()


#实力化-》变量=类（）
north_house = House()
china_house = House()

#调用变量
print("House1",House.door)

House.door="white"
print("第一次打印",north_house.door)

#实例属性实例化后north_house就变成实例对象，door就变成实例属性 ，变成"black"
north_house.door="black"
print("第二次打印",north_house.door)

print("House2",House.door)
print(china_house.door)