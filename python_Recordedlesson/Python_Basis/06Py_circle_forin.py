"""
1、计算1-100求和
2、加入分支实现1-100偶数求和
3、使用python实现1-100偶数求和
"""
# 1
result = 0
for i in range(101):
    result = result + i
print(result)

# 2
result = 0
for i in range(101):
    if i % 2 == 0:
        result = result + i
print(result)

# 3
result = 0
for i in range(0, 101, 2):
    result = result + i
print(result)

