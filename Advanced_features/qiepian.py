#!/usr/bin/python3

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
r = []
n = 3
for i in range(n):
    r.append(L[i])


print(r)
print(L[0:3])
# 既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
print(L[-2:])
print(L[-2:-1])

L = list(range(100))
print(L)
print(L[:10:2])
print(L[::5])  # 所有提取一个5
print(L[:])
print((1, 2, 3, 4, 5)[:3])



