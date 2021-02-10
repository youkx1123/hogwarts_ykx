import random
from dataclasses import replace

e = random.randint(10, 20)
a = 30
b = 8
c = a // b
f = random.random()
g = random.randint(1, 100) + random.random()
# 换行\n
h1 = "python\njava"
# \t 空格
h2 = "python\tjava"
# 加单引号
h3 = "python\'java"
# 加双引号
h4 = "python\"java"
print(c)
print(a < b)
print(e)
print(f)
print(g)
print(h1)
print(h2)
print(h3)
print(h4)
# 字符串拼接和格式化
name = "我叫张三"
age = "我今年18"
sex = "性别女"
desc = name + age + sex
# 输入方法一 直接使用 + 进行拼接
print(desc)
# 格式化1 使用format格式化
print("{}{}{}".format(name, age, sex))
# 方式2：字符串的F表达式（F、f都一样，python3.6以上支持）
print(F'今天收到{name}来信，他说{age},{sex}')
# 方式3：%号格式化输出
'''
%s：表示为任意的类型占位
%f：为浮点数占位
%d：为数值类型占位
'''
print('今天收到%s来信，他说%s，他说%s' % (name, age, sex))