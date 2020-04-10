#!/usr/bin/python3
# list,列表，是一种有序的集合，可以随时添加和算出其中的元素

# classmates= ['JACK', 'MAKE', 'tracy'] # 列表

# print(len(classmates)) #函数可以获得list元素的个数

# print(classmates[1]) #索引是从0开始的，也可以是负数

# classmates.append('Adam')# 新增加
# classmates.insert(1,'Tracy') # 可以把元素插入到指定位置，索引号为1的位置
# classmates.pop(0) # 删除list末尾的元素，用pop()方法
# classmates[0] = 'Sarah' #把某个元素替换成别的元素，直接赐值给对一个的索引位置
# classmates = ['python', 123, True, ['asp', 'clean']]
# print(classmates)

# tuple:元组，tuple和list非常类似
# 不同点：tuple一旦初始化就不可以被更改

# 相同点：同样是列出名字
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
# print(L[0][0])

# 小结
# list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们.


# 循环： Python的循环有两种
# classmates = ['python', 123, True, ['asp', 'clean']]
# for origin in classmates: #一种是for...in循环，依次把list或tuple中的每个元素迭代出来
#     print(origin)

# 另一种for x in ...循环就是把每个元素带入变了x,然后执行缩进块的语句
# clean = 0
# for x in [1, 2, 3, 4, 510]:
#     clean = clean + x
# print(clean)

# for a in list(range(4)):  # Python提供一个range()函数，可以生成一个整数序列
#     print(a)

# sum = 0
# for x in range(101):  # range(101)就可以生成0-100的整数序列
#     sum = sum + x
# print(sum)

# # 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现
# sum = 0
# n = 100
# while n > 0:
#     sum = sum + n
#     n = n - 2
# print(sum)

# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
# L = ['Bart', 'Lisa', 'Adam']
# print('for循环测试开始')
# for i in L:
#     print('Hello,%s!' % i)

# print('while循环测试开始')
# i = 0
# while i < 3:
#     print('Hello,%s!' % L[i])
#     i = i + 1

# 在循环中，break语句可以提前退出循环
# n = 0
# while n <= 100:
#     if n > 10:  # 当n = 11时,条件满足的情况下,执行break 语句；
#         break   # break 执行当前语句
#     print(n)  # 输出n,
#     n = n + 1  # n 自己+1
# print('END')  # 执行上面的代码可以看到,打印出1-10后,紧接着打印END,程序结束

# continue：在循环过程中，也可以通过continue 语句,跳过当前这次循环，直接开始下一次循环。
# 题目：如果我只想打印奇数,可以通过continue语句跳过某些循环
# n = 0
# while n < 10:  # while循环 当n 小于 10
#     n = n+1  # 第一次 0 = 0+ 1
#     if n % 2 == 0: # 如果n是偶数,执行continue语句
#         continue
#     print(n)  # 当n = 奇数输出

# 输出0-100的偶数：
n = 100
while n >=100:
    n = n+1
    if n % 2 ==1:  # 如果n%2 等于1 那么就执行continue
        continue
    print(n)


















