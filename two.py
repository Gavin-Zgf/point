#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# name=input('学生的名字是:')
# s1=int(input('去年的分数是:'))
# s2=int(input('今年的分数是:'))
name='大海'
s1=72
s2=85
r = ((s2-s1)/s1)*100
if s1 > s2 :
    print('你好，%s!\n你去年的成绩%d,\n今年的成绩是%d\n今年比去年下滑了:%.2f %%' % (name,s1,s2,r))
else :
    print('hello,{0}!,去年的成绩{1},\n今年的成绩：{2},\n成绩提升了{3:.1f}%'.format(name,s1,s2,r))
    # print('你好%s!,\n去年成绩:%d,\n今年的成绩:%d,\n%s表现不错,成绩提升了: %.2f%%,\nwow晚上加鸡腿' % (name,s1,s2,name,r))
