##1. 理解闭包函数定义
##2. 理解闭包函数的调用
##3. 变量在不同函数中的作用域

# 闭包函数
# 函数定义

# 鲸鱼吃人，人吃虾米，鲸鱼不知道人的肚子里面有虾米 最外层的级别最高，最内层的级别最低
name = "鲸鱼"
def func1():
    print("我是func1")
    print(name)
    # 在函数func1 内再定义一个函数
    def func2():
        name = "虾米"
        print("我是func2")
        print(name)
    # 返回 "肚子"里面的函数对象
    return func2
# 不加括号叫做函数对象
# func1
# 加了括号叫做函数的调用
# func1()-->func1的调用，其实== func2 (看return)
#func1()
func22 = func1()
## func22是 return的func2 的函数对象
func22()
