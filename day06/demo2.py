# read=open("小宝.JPG","rb+")
# write=open("F:\\小宝1.JPG","wb+")
# data=read.read()
# write.write(data)
# read.close()
# write.close()


#-*- coding: utf-8 -*-
import turtle

# 设置初始位置
turtle.penup()
turtle.left(90)
turtle.fd(200)
turtle.pendown()
turtle.right(90)

# 花蕊
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(10, 180)
turtle.circle(25, 110)
turtle.left(50)
turtle.circle(60, 45)
turtle.circle(20, 170)
turtle.right(24)
turtle.fd(30)
turtle.left(10)
turtle.circle(30, 110)
turtle.fd(20)
turtle.left(40)
turtle.circle(90, 70)
turtle.circle(30, 150)
turtle.right(30)
turtle.fd(15)
turtle.circle(80, 90)
turtle.left(15)
turtle.fd(45)
turtle.right(165)
turtle.fd(20)
turtle.left(155)
turtle.circle(150, 80)
turtle.left(50)
turtle.circle(150, 90)
turtle.end_fill()

# 花瓣1
turtle.left(150)
turtle.circle(-90, 70)
turtle.left(20)
turtle.circle(75, 105)
turtle.setheading(60)
turtle.circle(80, 98)
turtle.circle(-90, 40)

# 花瓣2
turtle.left(180)
turtle.circle(90, 40)
turtle.circle(-80, 98)
turtle.setheading(-83)

# 叶子1
turtle.fd(30)
turtle.left(90)
turtle.fd(25)
turtle.left(45)
turtle.fillcolor("green")
turtle.begin_fill()
turtle.circle(-80, 90)
turtle.right(90)
turtle.circle(-80, 90)
turtle.end_fill()

turtle.right(135)
turtle.fd(60)
turtle.left(180)
turtle.fd(85)
turtle.left(90)
turtle.fd(80)

# 叶子2
turtle.right(90)
turtle.right(45)
turtle.fillcolor("green")
turtle.begin_fill()
turtle.circle(80, 90)
turtle.left(90)
turtle.circle(80, 90)
turtle.end_fill()

turtle.left(135)
turtle.fd(60)
turtle.left(180)
turtle.fd(60)
turtle.right(90)
turtle.circle(200, 60)
turtle.done()


# import turtle
#
# # 定义常用的函数
# def c(x,y):
#     turtle.circle(x, y)
# def r(x):
#     turtle.right(x)
# def l(x):
#     turtle.left(x)
# def f(x):
#     turtle.fd(x)
#
# # 落笔处
# turtle.penup()
# l(90)
# f(200)
# turtle.pendown()
# r(90)
#
# # 花心
# turtle.fillcolor("red")
# turtle.begin_fill()
# c(10, 180)
# c(25, 110)
# l(50)
# c(60, 45)
# c(20, 170)
# r(24)
# f(30)
# l(10)
# c(30, 110)
# f(20)
# l(40)
# c(90, 70)
# c(30, 150)
# r(30)
# f(15)
# c(80, 90)
# l(15)
# f(45)
# r(165)
# f(20)
# l(155)
# c(150, 80)
# l(50)
# c(150, 90)
# turtle.end_fill()
#
# # 右瓣
# l(150)
# c(-90, 70)
# l(20)
# c(75, 105)
# turtle.setheading(60)
# c(80, 98)
# c(-90, 40)
#
# # 左瓣
# l(180)
# c(90, 40)
# c(-80, 98)
# turtle.setheading(-83)
#
# # 右叶
# f(30)
# l(90)
# f(25)
# l(45)
# turtle.fillcolor("green")
# turtle.begin_fill()
# c(-80, 90)
# r(90)
# c(-80, 90)
# turtle.end_fill()
#
# r(135)
# f(60)
# l(180)
# f(85)
# l(90)
# f(80)
#
# # 左叶
# r(90)
# r(45)
# turtle.fillcolor("green")
# turtle.begin_fill()
# c(80, 90)
# l(90)
# c(80, 90)
# turtle.end_fill()
#
# l(135)
# f(60)
# l(180)
# f(60)
# r(90)
# c(200, 60)
# turtle.done()