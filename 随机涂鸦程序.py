# !/usr/bin/python
# coding: utf8
# Time: 2020/7/18 19:58
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import turtle
import random
turtle.speed(0)
turtle.setup(width=800, height=600)

for i in range(40):
    turtle.colormode(255)
    turtle.penup()
    turtle.goto(random.randint(-400, 400), random.randint(-300, 300))
    turtle.fillcolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    turtle.begin_fill()
    step = random.randint(0, 200)
    for j in range(4):
        turtle.fd(step)
        turtle.left(90)
    turtle.end_fill()

turtle.done()

