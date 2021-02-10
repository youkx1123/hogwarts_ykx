
# 格式化小数长度（会四舍五入）
# 方法1 format（保留2位小数）
num = 3.14999994
print("这个数是{:.2f}".format(num))
# 方法2 F表达式（不保留小数位）
# print(F"这个百分数是：{num:0%}")
print(F"这个百分数是：{num:.0%}")
# 格式化字符串长度，并进行左、右、居中对齐
# 1format
s1 = "我是小可爱，你是小糊涂"
print("我的备注是：{:<15},你要记得！".format(s1))
print("我的备注是：{:>15},你要记得！".format(s1))
print("我的备注是：{:^15},你要记得！".format(s1))
# 2F表达式
print(F"我的备注是：{s1:<15},你要记得！")
print(F"我的备注是：{s1:>15},你要记得！")
print(F"我的备注是：{s1:^15},你要记得！")
# 3格式化百分比，并控制小数位
per = 0.44
print("{:.2%}".format(per))
print(F"{per:.2%}")
# 字符串的常用方法
# 一、find：查找字符串，返回的是字符串的索引（下标）
#
"""
1、“e”的下标是8
2、下标是从0开始计数的
3、如果查找的字符串存在多个，查找结果是第一个出现的字符串下标
4、从第3个下标开始找，一直找到第9-1个，第一个“t”的下标是7
5、找不到字符串“b”，就返回-1
6、可以查找字符串“anc”，返回字符串的第一个字符“a”的下标是9
"""
s2 = "python hello word! or"
res1 = s2.find("e")
res2 = s2.find(" ")
res3 = s2.find("o", 3, 9)
res4 = s2.find("r", 0, 10)
res5 = s2.find("ord")
print("res1={}\tres2={}\tres3={}\tres4={}\tres5={}".format(res1, res2, res3, res4, res5))

# 二、count：计算字符的个数
# 1、计算字符“a”的个数是3个
res6 = s2.count("o")
# 计算字符串“ah”的个数是2个
res7 = s2.count("or")
# 计算不存在的字符的个数是0个
res8 = s2.count("ol")
print("res6={}\tres7={}\tres8={}".format(res6, res7, res8))

# 三、replace：替换字符串的内容
# 1将字符串“or”替换成“rr”，输出替换后的内容
s2 = "python hello word! or"
res9 = s2.replace("or", "rr")

# 2将不存在的字符串“word1”替换成“max”，将不会改变原内容
res10 = s2.replace("word1", "max")

# 3将字符“o”替换成“omega”，输出替换后的内容
res11 = s2.replace("o", "omega")

# 4若存在多个被替换的字符串“来呀快活呀111"”，将默认全部替换
res12 = s2.replace("l", "来呀快活呀111")

# 5将所有的“空格”替换成“我是空格”，输出替换后的内容
res13 = s2.replace(" ", "我是空格")

# 6通过第三个参数，指定替换的个数，只替换前2个“空格”
res14 = s2.replace(" ", "我原本是空格", 2)
print(
    "res9={}\tres10={}\t\nres11={}\t\nres12={}\t\nres13={}\t\nres14={}".format(res9, res10, res11, res12, res13, res14))

# 四split：字符串分割
# 1、将字符串，用规定的字符“a”进行分割，得到一个列表
s3 = "111a2222a3333"
s = s3.split("a")
print(s)
# 2、实际工作中会用到的情况
s4 = "data:111,url:www.baidu.com,mubile:13111323223"
s = s4.split(",")
print(s)

# 五、upper：把小写的字母转换为大写
# 实际工作中会用到的场景，将“post”所有的小写字母转换成大写“POST”
method = 'post'
met = method.upper()
print(method)
print("POST" == method.upper())
# 六、lower：把大写的字母转换为小写
# 1、将字符串中所有的大写字母，转换为小写字母
s5 = "TIANQIDASHA"
print(s5.lower())
#  2、将字符串中所有的字母，转换成第一个大写，其他小写
s6 = "tqds"
print(F"TIANQIDASHA首字母大写：{s5.capitalize()}")
print("tqds首字母大写:{}".format(s6.capitalize()))

# 七、strip：去除字符串首尾的空格
# 1、将首尾的“空格”去除，默认去空格（工作中会用到）
s7 = " 644 55556 "
print('" 6444 55556  "去掉首尾空格:{}'.format(s7.strip()))
# 将首尾的“6”去除
print(s7.strip(' ' + "6"))
# print(f"去掉空格和6：{s7.strip(' '+"6")}")
# 如果想把所有的空格都去除，通过替换方法“replace”将“空格”替换成“无”
print(s7.replace(" ", ""))
# 八"join"：字符串拼接
'''
1、使用“空格”作为连接符，将“a、b、c”连接起来
2、使用join时，必须将被连接的字符串，放入列表中
3、同等于“a+连接符+b+连接符+c”
'''
a = "你好呀"
b = "小明"
c = "同学"
d = ''.join([a, b, c])
print(''.join([a, b, c]))
print(d)
