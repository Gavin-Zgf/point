#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 有四本书，分别是：大学，中庸，论语，孟子
# 按照这四个选项做一个小程序，需要列表有：
# （1、查看当前所有图书列表；2、车讯某本图书位置；3、更改图书编号；4、删除某本图书；5、增加某本图书；0、退出）

Book = {'大学': 1, '中庸': 2, '论语': 3, '孟子': 4}
book_key = list(Book.keys())
book_values = list(Book.values())
xx = 10
while xx != 0:
    print("\n*************选择列表*************\n",
          "1、查看当前所有图书列表\n",
          "2、查询某本图书位置\n",
          "3、更改图书编号\n",
          "4、删除某本图书\n",
          "5、增加某本图书\n",
          "0、退出\n\n")
    xx = input("请输入：")
    if xx == '1':
        print('书籍有：', Book, "\n", '操作完成')
    elif xx == '2':
        n1 = input("请输入你要查找的书籍名称:")
        if n1 in Book:
            print("编号是:", Book[n1])
        else:
            print("\n没有此书，请重试\n")
    elif xx == '3':
        n2 = input("需要更改图书名称：")
        n3 = input("更改编号是：")
        if n2 in Book:
            Book[n2] = n3
        else:
            print("\n请验证\n")
    elif xx == '4':
        n4 = input("\n需要删除哪本图书:\n")
        if n4 in Book:
            print(Book.pop(n4))
            print("修改成功")
        else:
            print("\n********重新验证输入********\n")
    elif xx == '5':
        book_name = str(input("新增书籍名称:"))
        if book_name in book_key:
            print("已有此书，请勿重复添加")
        else:
            book_values1 = int(input("请输入编号："))
            if book_values1 in book_values:
                print("书架被占用")
            else:
                Book[book_name] = book_values1
                print("添加%s成功,新书架号为%d,感谢您的使用" % (book_name, book_values1))
    elif xx == '0':
        print("退出程序")
    else:
        break
