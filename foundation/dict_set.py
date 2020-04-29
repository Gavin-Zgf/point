#!/usr/bin/python3
# -*- coding: utf-8 -*-

# dict：字典 dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度

# d = {'Mich    ael': 95, 'Bob': 75, 'Tracy': 85}
# # d = {'Michael': 60, 'Bob': 30, 'Tracy': 10}
# print(d['Michael'])  # 一个key只能对应一个value值,所以,多次对一个key放入value，后面的值会把前面的值冲掉
#
# # 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在
# print("Thomas" in d)

# # dict提供的一个get()方法，如果key不存在,可以返回None,或者是制定的value
# print(d.get("Tony"))  # 返回None的时候Python的交互环境不显示结果
# print(d.get("Tony", -1))
#
# if d.pop('Bob'):  # 用pop(key)方法，对应的value也会从dict中删除
#     print(d)

# 和list比较，dict有以下几个特点：
#
# 1、查找和插入的速度极快，不会随着key的增加而变慢；
# 2、需要占用大量的内存，内存浪费多。
# 而list相反：

# 1、查找和插入的时间随着元素的增加而增加；
# 2、占用空间小，浪费内存很少。
# dict是换区时间的一种方法；
# 要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key


# set 套,集合
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
# set也可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交际、并集操作

s = set([1, 2.1, 1, 'adm'])  # 重复元素在set中自动被过滤
print(s)
print(s.add(4))
print(s.remove(4))  # 通过remove(key)方法可以删除元素
print(s)

s1 = set([1,2,'Tony'])
s2 = set([2,4,'Tony'])
print(s1 & s2)
print(s1 | s2)

# 不可变对象
# str是不变对象，而lise是可变对象，对于可变对象比如list，对list进行操作，list内部的内容会变化
a =['c', 'va', 'ad']  # list可变
print(a.sort())
print(a)

a = 'abc'  # 对于str而言可以变成A，但变量a仍是‘abc‘
print(a.replace('a', 'A'))
print(a)

# 小结
# 使用key-value存储结构的dict在Python中非常有用，选择不可变对象作为key很重要，最常用的key是字符串。
#
# tuple虽然是不变对象，但试试把(1, 2, 3)和(1, [2, 3])放入dict或set中，并解释结果。




