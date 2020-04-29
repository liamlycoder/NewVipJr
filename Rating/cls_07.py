# !/usr/bin/python
# coding: utf8
# Time: 2020/4/29 9:05
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import turtle as t

OnOff = input("请输入：")

if OnOff == "on":
    bulb_color = 'yellow'
elif OnOff == 'off':
    bulb_color = 'black'
else:
    print("输入不合法")

width = 250
height = 150
radius = 30
battery_w = 65
battery_h = 33

t.penup()
t.goto(-125, -75)
t.pendown()

t.pensize(5)
t.color('orange', 'green')

t.fd(width/4)
t.rt(90)

t.begin_fill()
t.fd(battery_h/2)
t.lt(90)
t.fd(battery_w)
t.lt(90)
t.fd(battery_h)
t.lt(90)
t.fd(battery_w)
t.lt(90)
t.fd(battery_h/2)
t.end_fill()

t.penup()
t.lt(90)
t.fd(battery_w)
t.pendown()
t.fd(width - width/4 - battery_w)
t.lt(90)
t.fd(height)
t.lt(90)
t.fd((width-radius*2)/2)
t.rt(90)
t.penup()
t.fillcolor(bulb_color)
t.begin_fill()
t.circle(radius)
t.end_fill()
t.lt(90)
t.fd(radius*2)
t.pendown()
t.fd((width-radius*2)/2)
t.lt(90)
t.fd(height)
t.lt(90)





t.done()
