#!/usr/bin/python3
# -*- coding: utf-8 -*-

# dict：字典 dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# d = {'Michael': 60, 'Bob': 30, 'Tracy': 10}
print(d['Michael'])  # 一个key只能对应一个value值,所以,多次对一个key放入value，后面的值会把前面的值冲掉

# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在
print("Thomas" in d)

# dict提供的一个get()方法，如果key不存在,可以返回None,或者是制定的value
print(d.get("Tony"))  # 
print(d.get("Tony", -1))


















