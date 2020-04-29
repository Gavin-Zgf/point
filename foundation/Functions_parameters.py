# -*- coding: utf-8 -*-

# 位置参数
# 定义函数的时候，我们把参数的名字和位置确定下来，函数的接口定义就完成了。对于函数的调用者来说，只需要知道如何传递正确的参数，以及函数将返回什么样的值就够了
# def power(x):
#     return x * x
# print(power(5))
# print(power(15))

# 默认函数
# 你也许想到了，可以把power(x)修改为power(x, n)，用来计算x的n平方：
# 当我们调用power(5)时，相当于调用power(5, 2)
# def power(x, n=5):
#     s = 1
#     while n > 0:
#         s = x * s
#         n = n - 1
#     return s
#
#
# print(power(5))


# 从上面的例子可以看出，默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
#
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
#
# 二是如何设置默认参数。
#
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
#
# 使用默认参数有什么好处？最大的好处是能降低调用函数的难度。

# 举个例子，我们写个一年级小学生注册的函数，需要传入name和gender两个参数
# 如果要继续传入年龄、城市等信息怎么办？这样会使得调用函数的复杂度大大增加
# bad 例子1：
# def zhuce(name, Nan):
#     print('name', name)
#     print('Nan', Nan)
#
#
# print(zhuce('Tony', 'Nv'))


# 我们可以把年龄和城市设为默认参数：
# def enroll(name, gender, age=6, city='Beijing'):
#     print('名字', name)
#     print('性别', gender)
#     print('年龄', age)
#     print('市', city)
#
#
# print(enroll('Tony', 'Nv', 10, 'Shanghai'))

# 错误例子：(虽然没试出来错在哪)
#   因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了
# def add_end(L=[]):
#     L.append('END')
#     return L
#
#
# print(add_end([]))


# 定义默认参数要牢记一点：默认参数必须指向不变对象！
# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L


# print(add_end([1, 755]))

# 可变函数
# 我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……


# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
#
#
# # 但是调用的时候，需要先组装出一个list或tuple：
# print(calc([5, 6, 7]))
# print(calc((6, 7, 5)))


# 如果利用可变参数，调用函数的方式可以简化成这样,(说：)
#   定义可变参数和定义一个就是在函数里加一个*,所以list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。
#   但是，调用该函数时，可以传入任意个参数，包括0个参数

# def calc(*numbers):
#     sums = 0
#     for n in numbers:
#         sums = sums + n * n
#     return sums


# print(calc(5, 6, 7))
# print(calc(0))

# 如果已经有一个list或者tuple，要调用一个可变参数怎么办
# def aa(nnn=None):
#     if nnn is None:
#         nnn = [5, 6, 7]
#     sums = 0
#     for bb in nnn:
#         sums = sums + bb * bb
#     return sums
#
#
# print(aa())

# def calc(*numbers):
#     sums = 0
#     for n in numbers:
#         sums = sums + n * n
#     return sums
#
#
# # 如果已经有一个list或者tuple，要调用一个可变参数怎么办？
# nums = [1, 2, 3]
# print(calc(nums[0], nums[1], nums[2]))

# 把list或tuple的元素变成可变参数传进去
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法很常用
# print(calc(*nums))


# 关键字参数
# 函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数
def person(name, age, **rrr):
    print('name:', name, 'age:', age, 'other:', rrr)


print(person('Michael', 30))
# 也可以传入任意个数的关键字参数
print(person('Tony', 35, city='Shanghai'))
print(person('Adam', 45, gender='M', job='Engineer'))

# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去

extra = {'city': 'Beijing', 'job': 'Engineer'}

# 真的太复杂......
# print(person('jack', 20, city=extra['city'], job=extra['job']))
# 简化调用写法：
print(person('Jack', 20, **extra))


# 小结：**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
# 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

# 命名关键字参数
# 对于关键字参数，函数打调用者可以传入仍以不受限制的关键字参数。至于到底传入哪些，就需要在函数内部通过kw检查。
# 仍以person()函数为例，我们希望检查是否有city和job参数
def person(name, age, **kw):
    if 'city' in kw:  # 有city参数
        pass
    if 'job' in kw:  # 有job的参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)


print(person('jack', 24, city='Shanghai', addr='Chaoyang', zipcode=123455))


# 如果要限制关键字参数名字，就可以用命名关键字参数，比如只接收city，job做为关键字参数，
# 可以用 * 隔开，和关键字 **kw 不同，命名关键字只要一个 * 隔开, * 隔开后面的视为关键字参数.
# 由于命名关键字参数city具有默认值，调用时，可不传入city参数
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)


person('Jack', 24, job='Engineer')


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
# def person(name, age, *args, city, job):
#     print(name, age, args, city, job)
#
# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
# print(person('jack', 20, "北京", 'Engineer'))

def person(name, age, city, job):  # 缺少 * , city和job被视为位置参数
    print(name, age, city, job)
    pass


print(person('Tony', 2222222222, 'Shanghai', 'Engineer'))


# 参数组合
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


print(f1(1, 2))  # 必选参数
print(f1(1, 2, c=4))  # 默认参数
print(f1(1, 2, 3, 'a', 'b'))  # 可变参数
print(f1(1, 2, 3, v=99))  # 命名关键字
print(f2(1, 2, d=99, ext=None))  # 关键字参数

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '&&&'}
print(f1(*args, **kw))

# 最神奇的是通过一个tuple和dict，你也可以调用上述函数
args = (11, 22, 33)
kw = {'d': 100, 'x': '&&&'}
print(f2(*args, **kw))

# Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
#
# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
#
# 要注意定义可变参数和关键字参数的语法：
#
# *args是可变参数，args接收的是一个tuple；
#
# **kw是关键字参数，kw接收的是一个dict。
#
# 以及调用函数时如何传入可变参数和关键字参数的语法：
#
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
#
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
#
# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
#
# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
#
# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
