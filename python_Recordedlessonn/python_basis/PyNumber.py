a = 1
print(a)
# id可以打印变量的存储地址
print(id(a))

int_a = 1
float_a = 0.2
complex_a = 0.3J
complex_b = 0.3j
# 通过tape来查看变量的数据类型
print(type(int_a))
print(type(float_a))
print(type(complex_a))
print(type(complex_b))


"""
#变量：命名规则
-硬性规则
  变量名由字母（广义的Ucode字符，不包括特殊字符）、数字和下划线构成，数字不能开头。
  大小写敏感（大写的'A'和小写的‘a’是两个不同的变量）
  不要跟关键字（有特殊含义的单词）和系统保留字（如函数、模块等的名字）冲突。
"""
