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
# print ('%s,你的身高是(cm)%.2f,体重(kg):%.2f,你的BMI：%.2f,你太胖了' % (name,h,w,BMI))
if BMI<18.5:
    print('Hello,%s,你的身高:%.2f,体重是：%.2f,综合BMI:%.2f:体重过轻' %(name,h,w,BMI))
elif BMI<25 :
    print('Hello,%s,你的身高:%.2f,体重是：%.2f,综合BMI:%.2f:体重过轻' %(name,h,w,BMI))
elif BMI<28 :
    print('%s,身高(cm):%.2f,体重是(kg)：%.2f,BMI:%.2f,你心里有点数没？' %(name,h,w,BMI))
elif BMI<32 :
    print('%s,你的身高:%2f,体重是:%.2f,综合BMI:%.2f:体重肥胖'% (name,h,w,BMI))
else:
    print('Hello,%s,你的身高:%.2d,体重是：%.2f,综合BMI:%.2f:严重肥胖,\n赶紧回去减肥'% (name,h,w,BMI))

