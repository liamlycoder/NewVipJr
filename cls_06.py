# !/usr/bin/python
# coding: utf8
# Time: 2020/1/20 18:55
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import turtle

turtle.speed(4)
turtle.hideturtle()
for i in range(4):
    if i % 2 == 0:
        turtle.pendown()
    else:
        turtle.penup()
    turtle.forward(100)
    turtle.left(90)
turtle.done()


turtle.speed(5)
for j in range(100):
    for i in range(4):
        if i == 1 and j % 20 == 1:
            turtle.down()
        else:
            turtle.penup()
        turtle.forward(j)
        turtle.left(90)
turtle.done()

for j in range(0, 100, 10):
    for i in range(4):
        if i == 1:
            turtle.pendown()
        else:
            turtle.penup()
        turtle.forward(j)
        turtle.left(90)
turtle.done()


turtle.speed(0)
colors = ["red", 'green', 'blue', 'purple']
for i in range(100000):
    turtle.pencolor(colors[i % 4])
    turtle.forward(200)
    turtle.left(91)
turtle.done()
