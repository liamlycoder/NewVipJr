# !/usr/bin/python
# coding: utf8
# Time: 2020/5/13 20:09
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import turtle

# 绘制脸框
turtle.pensize(5)
turtle.color("orange", "yellow")
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()

# 绘制左眼
turtle.penup()
turtle.goto(-20, 100)
turtle.pendown()
turtle.lt(90)
turtle.circle(15, 180)

# 绘制右眼
turtle.penup()
turtle.goto(20, 100)
turtle.pendown()
turtle.lt(180)
turtle.circle(-15, 180)

# 绘制左边脸颊
turtle.fillcolor("pink")
turtle.penup()
turtle.goto(-65, 75)
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()

# 绘制右边脸颊
turtle.penup()
turtle.goto(65, 75)
turtle.begin_fill()
turtle.circle(-15)
turtle.end_fill()

# 绘制嘴巴
turtle.penup()
turtle.goto(-35, 50)
turtle.pendown()
turtle.circle(35, 180)
"""
import random
turtle.setup(width=1.0, height=1.0)
turtle.speed(0)

size = random.randint(50, 250)

# 绘制脸框
turtle.pensize(size*5/80)
turtle.color("orange", "yellow")
turtle.begin_fill()
turtle.circle(size)
turtle.end_fill()

# 绘制左眼
turtle.penup()
turtle.goto(-size*20/80, size*100/80)
turtle.pendown()
turtle.lt(90)
turtle.circle(size*15/80, 180)

# 绘制右眼
turtle.penup()
turtle.goto(size*20/80, size*100/80)
turtle.pendown()
turtle.lt(180)
turtle.circle(-size*15/80, 180)

# 绘制左边脸颊
turtle.fillcolor("pink")
turtle.penup()
turtle.goto(-size*65/80, size*75/80)
turtle.begin_fill()
turtle.circle(size*15/80)
turtle.end_fill()

# 绘制右边脸颊
turtle.penup()
turtle.goto(size*65/80, size*75/80)
turtle.begin_fill()
turtle.circle(-size*15/80)
turtle.end_fill()

# 绘制嘴巴
turtle.penup()
turtle.goto(-size*35/80, size*50/80)
turtle.pendown()
turtle.circle(size*35/80, 180)
"""
turtle.done()

