# !/usr/bin/python
# coding: utf8
# Time: 2020/7/14 8:27
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import turtle
turtle.fillcolor("grey")
turtle.begin_fill()
turtle.forward(120)
turtle.left(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(120)
turtle.left(90)
turtle.forward(40)
turtle.end_fill()
turtle.penup()
turtle.goto(120, 40)

turtle.left(90+20)
turtle.pendown()
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(180, 325)
turtle.end_fill()


turtle.done()


