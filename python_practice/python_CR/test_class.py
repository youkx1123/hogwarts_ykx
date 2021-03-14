# 创建一个类
# 通过class关键字，进行定义了一个类
# 定义一个类为了实例化具体的实例，如何实例化一个实例？
class Person:
    # 属性
    # 类变量
    name = "default"
    age = 0
    gender = "male"
    weight = 0

    def __init__(self, name, age, gender, weight):
        # self.变量名的方式，访问的问题，叫做实例变量
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight

    # 设置本地类属性的方法
    def set_param(self, name):
        # self.name 是类里面的 ，name是外面传进来的
        self.name = name

    def set_age(self, age):
        self.age = age

    # 方法： def 方法名字（eat（）） self：在类里面创建方法的时候需要加self "："结束符 回车 填写代码块
    @classmethod
    def eat(self):
        # 代码块
        print(f"{self.name} esting")

    def paly(self):
        print(f"{self.name}palying")

    def jump(self):
        print(f"{self.name}jump")


# 类变量和实例变量的区别
# 类变量是需要类来访问，实例变量是需要实例来访问

# 类变量
print(Person.name)

# 类变量和实例变量都可以被修改
Person.name = "tom"
print(Person.name)
print("***********************")

# 实例变量
zs = Person("张三", 20, "男", 130)
print(zs.name)

# 类变量和实例变量都可以被修改
zs.name = "lily"
print(zs.name)

print("--------------------------")

# 类方法和实例方法的区别
# 类方法不能访问,实例方法
# 类方法访问实例方法需要访添加装饰器@classmethod

# 类方法不能访问实例方法：ypeError: eat() missing 1 required positional argument: 'self'
Person.eat()

zs = Person("张三", 20, "男", 130)
zs.eat()

# 实例化一个实例  类名+（）"实例化zs  -》zs=Person()"
# 类的实例化，创造了一个实例
zs = Person("张三", 20, "男", 130)
zs.jump()

# zs.set_param("张三")
# zs.set_age(28)

print(f"zs的姓名是:{zs.name}")
print(f"zs的年龄是:{zs.age}")
print(f"zs的姓名是:{zs.name},年龄是:{zs.age},性别是：{zs.gender},体重是：{zs.weight}")

ls = Person("李四", 30, "女", 144)
ls.jump()
print(f"ls的姓名是:{ls.name},年龄是:{ls.age},性别是：{ls.gender},体重是：{ls.weight}")
