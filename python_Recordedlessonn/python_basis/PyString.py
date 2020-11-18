"""
\:转义符
r：忽略转义符的作用
+以及空格：多个字符串链接
切片
根据官网补充
更多的用法可以关注官网文档
"""
str_a = "aa"
print(type(str_a))

# 1"bb\n"打印会空一行 2 打印"\n" "bb\\n"或者" r"bb\n" "打印结果bb\n
str_b = "bb"
str_c = "cc"
print(str_b)
print(str_c)
# "str_b+str_c"打印结果bbcc
print(str_b + str_c)
str_d = "aaa" "fff"
print(str_d)

str_e = "12345678"
# 索引
print(str_e[0])
# 切片 [star:stop:step][开始：结束：步长]
print(str_e[0:4:2])
print(str_e[0:4])


