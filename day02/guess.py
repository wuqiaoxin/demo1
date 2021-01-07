# 猜数字，计算机随机定义一个数字进行猜测，怎么判断猜的对不对
# 如何循环，while，break
# if else

import random #让系统产生一个随机数
num=int(random.random()*100)#0-1
i=0

while True:
    a=int(input("请输入您猜的数："))
    i=i+1
    if a>num:
        print("您猜大了")
    elif a<num:
        print("您猜小了")
    else:
        print("恭喜您，猜对了！！！",num,"您猜了",i,"次")
        break









