"""
while循环通过一个能生成或转换bool值的表达式控制循环
"""
# 表达式为ture的时候循环继续，表达式为false循环结束
while True:
    print("a")
    break
print("------------------------")


a = 1
# while循环使用else语句n
while a == 1:
    print("a==1")
    a = a + 1
else:
    print("a!=1")
print(a)
print("------------------------")

b = 1
# 如果while循环体中只有一条语句，可以将该语句与while写在同一行中
while b == 1: b = b + 1
else:
    print("b!=1")
print(b)
print("------------------------")

# break 跳出整个循环体
for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("------------------------")
# continue 跳出当前一次循环，跳出i==5的一次循环
for n in range(1, 10):
    if n == 5:
        continue
    print(n)

