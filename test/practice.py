# -*- coding: utf-8 -*-
#!/usr/bin/python3

# s  = input('birth:')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('90后')

name = input('please enter your name：')
h = int(input('please enter your height(cm):'))
w = float(input('please enter your weight(kg):'))
# h = 178
# w = 100
H = h/100  # 升高除以100 转换成M;
s = w/(H**H)
BMI = int(s)
# print ('%s,你的身高是(cm)%.2f,体重(kg):%.2f,你的BMI：%.2f,你太胖了' % (name, h, w, BMI))
if BMI<18.5:
    print('Hello,%s,你的身高:%.2f,体重是：%.2f,综合BMI:%.2f:体重过轻' %(name, h, w, BMI))
elif BMI<25:
    print('Hello,%s,你的身高:%.2f,体重是：%.2f,综合BMI:%.2f:体重过轻' % (name, h, w, BMI))
elif BMI<28 :
    print('%s,身高(cm):%.2f,体重是(kg)：%.2f,BMI:%.2f,你心里有点数没？' %(name, h, w, BMI))
elif BMI<32 :
    print('%s,你的身高:%2f,体重是:%.2f,综合BMI:%.2f:体重肥胖'% (name, h, w, BMI))
else:
    print('Hello,%s,你的身高:%.2d,体重是：%.2f,综合BMI:%.2f:严重肥胖,\n赶紧回去减肥'% (name, h, w, BMI))

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
