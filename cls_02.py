# !/usr/bin/python
# coding: utf8
# Time: 2020/1/15 12:16
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import turtle

# 画三角形
# turtle.forward(300)
# turtle.left(120)
# turtle.forward(300)
# turtle.left(120)
# turtle.forward(300)

# 画正方形
# turtle.forward(300)
# turtle.right(90)
# turtle.forward(300)
# turtle.right(90)
# turtle.forward(300)
# turtle.right(90)
# turtle.forward(300)

# 画五边形
# turtle.forward(200)
# turtle.left(72)
# turtle.forward(200)
# turtle.left(72)
# turtle.forward(200)
# turtle.left(72)
# turtle.forward(200)
# turtle.left(72)
# turtle.forward(200)
# turtle.left(72)

# 画六边形
# turtle.forward(200)
# turtle.left(60)
# turtle.forward(200)
# turtle.left(60)
# turtle.forward(200)
# turtle.left(60)
# turtle.forward(200)
# turtle.left(60)
# turtle.forward(200)
# turtle.left(60)
# turtle.forward(200)
# turtle.left(60)

# 规律：旋转的度数 = 360/n   其中，n为正多边形的边数

# 综合作图
turtle.penup()
turtle.goto(-200, 200)
turtle.pendown()
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)

turtle.penup()
turtle.goto(200, 200)
turtle.pendown()
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)

turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.left(144)

turtle.penup()
turtle.goto(200, -200)
turtle.pendown()
turtle.circle(50)


turtle.done()
