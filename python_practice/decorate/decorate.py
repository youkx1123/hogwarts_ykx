# 概念：
#
# 1.装饰器的实现是由闭包支撑的；
#
# 2.装饰器本质上是⼀个python函数，它可以在让其他函数在不需要做任何代码的变动的前提下增加额外的功能；
#
# 3.装饰器的返回值也是⼀个函数的对象，它经常用于有切面需求的场景，实现路由传参，flask的路由传参依赖于装饰器，浏览器通过url访问到装饰器的路由，从而访问视图函数获得返回的HTML页面；
#
# 应用场景：
#
# 1.可以在外层函数加上时间计算函数，计算函数运行时间；
# 2.计算函数运行次数；
# 3.可以用在框架的路由传参上；
# 4.插入日志，作为函数的运行日志；
# 5.事务处理，可以让函数实现事务的一致性，让函数要么一起运行成功，要么一起运行失败；
# 6.缓存，实现缓存处理；
# 7.权限的校验，在函数外层套上权限校验的代码，实现权限校验；


#写出一个单例的装饰器(使一个本来不是单例类的类变成单例类))
def set_func(func):
    __singleton = None

    def call_func(*args, **kwargs):
        nonlocal __singleton
        if not __singleton:
            __singleton = func(*args, **kwargs)
            return __singleton
        else:
            return __singleton

    return call_func


@set_func
class Std(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age


s2 = Std('jack', 18)
print(id(s2), s2.name, s2.age)

s1 = Std('leo', 23)
print(id(s1), s1.name, s1.age)


# 登录判断装饰器:
# 之前做过的一个用flask框架实现的移动app项目，里面大量用到是否已经登录的判断，
# 如果这个业务逻辑大量重复地写在视图函数，代码的复用性很差，因此我将登录判断封装成装饰器，
# 然后用这个装饰器装饰每一个需要验证是否登录的视图函数，代码如下:


def login_required(view_func):
    """自定义装饰器判断用户是否登录"""

    @wraps(view_func)
    def wrapper(*args, **kwargs):
        """具体实现判断用户是否登录的逻辑"""
        user_id = session.get('user_id')
        if not user_id:
            return jsonify(errno=RET.SESSIONERR, errmsg='用户未登录')
        else:
            g.user_id = user_id
            return view_func(*args, **kwargs)

    return wrapper

# 总结:装饰器是python三大神器(迭代器，生成器，装饰器)中比较难理解的，但是它的本质实际上就是闭包，
# 我们在闭包函数或者类外面封装了一套逻辑，因此可以增强函数的功能，增加权限校验，事务一致性，缓存等功能，
# 这就是装饰器，使漂亮的姑娘(函数)变得更加漂亮。

