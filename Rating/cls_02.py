# !/usr/bin/python
# coding: utf8
# Time: 2020/4/15 23:29
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import turtle as t


t.pensize(4)
t.circle(100, 360)

t.penup()
t.lt(90)
t.fd(50)

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

t.penup()
t.goto(-120, 100)
t.pendown()
t.fd(240)

t.penup()
t.goto(0, -20)
t.pendown()
t.lt(90)
t.fd(240)

t.hideturtle()


t.done()
