a = 9
if a == 0:
    print("a=0")
elif a == 1:
    print("a=1")
elif a == 2:
    print("a=2")
else:
    print("a!=0,1,2,3")

"""
       3*x-5 (x>1)
 f(x)= x+2   (-1<=x<=1)
       5*x+3 (x<-1)     
"""
# 多重分支
x1 = 1
if x1 > 1:
    y1 = 3 * x1 - 5
elif -1 <= x1 <= 1:
    y1 = x1 + 2
elif x1 < -1:
    y1 = 5 * x1 + 3
print(y1)


# 分支机构
x = 0
if x > 1:
    y = 3 * x - 5
    print(y)
else:
    # if -1 <= x <= 1:
    #     y = x+2
    #     print(y)
    if x < -1:
        y = 5 * x + 3
        print(y)
    else:
        y = x + 2
        print(y)
print(y)
