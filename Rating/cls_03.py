# !/usr/bin/python
# coding: utf8
# Time: 2020/4/15 23:29
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import turtle as t


t.pensize(4)
t.circle(100, 360)  # 绘制大圆

t.penup()
t.lt(90)
t.fd(50)  # 寻找新的落笔点

# 绘制内圈的虚线圆
t.pensize(1)
t.pendown()
t.rt(90)
t.circle(50, 22.5)
t.penup()
t.circle(50, 45)
t.pendown()
t.circle(50, 45)
t.penup()
t.circle(50, 45)
t.pendown()
t.circle(50, 45)
t.penup()
t.circle(50, 45)
t.pendown()
t.circle(50, 45)
t.penup()
t.circle(50, 45)
t.pendown()
t.circle(50, 22.5)

# 画横线
t.penup()
t.goto(-120, 100)
t.pendown()
t.fd(240)

# 画竖直线
t.penup()
t.goto(0, -20)
t.pendown()
t.lt(90)
t.fd(240)

t.hideturtle()  # 将海龟隐藏起来

t.done()
