#!/usr/bin/python3

# 递归函数
# 汉诺塔的移动可以用递归函数非常简单地实现。
# 请编写move(n, a, b, c)函数，它接收参数n,
# 表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法

# def move(n, a, b, c):
#     if n == 1:
#         print(a, '-->', c)
#     else:
#         move(n - 1, a, c, b)  # 将n-1块由a绕过c搬运至b
#         print(a, '-->', c)  # 将最后一块最大块由a搬运至c
#         move(n - 1, b, a, c)  # 将b上的n-1块由把绕过a搬运至c


# print(move(4, 'A', 'B', 'C'))

# 切片

def trim(s):
    if len(s) != 0:
        if s[0] == ' ':
            return trim(s[1:])
        elif s[-1] == ' ':
            return trim(s[:-1])
        else:
            return s
    else:
        return s


if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
