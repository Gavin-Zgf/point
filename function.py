#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 函数调用：
# a = abs(-20)
# a = abs(100)
# print(a)
# # abs函数: 调用函数的时候，如果传入的参数数量不对，会报TypeError的错误，并且Python会明确地告诉你：abs()有且仅有1个参数，但给出了两个
# abs(1, 2)
# # 如果传入的参数数量是对的，但参数类型不能被函数所接受，也会报TypeError的错误，并且给出错误信息：str是错误的参数类型：
# abs('a')
# # 而max函数max()可以接收任意多个参数，并返回最大的那个
# b = max(1, 3, 4, 10)
# print(b)
#
# # 数据类型转换
# int('123')
# int(12.23)
# float('12.34')
# str(1.23)
# str(100)
# bool(1)
# bool('')

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
# a = abs  # 变量a指向abs函数
# a(-1)  # 所以也可以通过a调用abs函数
# 输出  1

# 定义函数
# 在python中,定义一个函数要用到def语句,依次写出函数名、括号、括号中打参数和冒号，然后，在缩进块中编写函数体
#       函数的返回值用return语句返回。

# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type111')
#     if x >= 0:
#         return x
# print(my_abs(13.14))
#
# # 空函数：pass
# def d():
#     pass

# 返回多个值
# 函数可以返回多个值，比如在游戏中需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的坐标;

















