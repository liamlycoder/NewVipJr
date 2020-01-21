# !/usr/bin/python
# coding: utf8
# Time: 2020/1/19 17:12
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import turtle
color = input("请输入三角形的颜色：")
length = int(input("请输入三角形的边长："))
turtle.fillcolor(color)
turtle.begin_fill()
turtle.forward(length)
turtle.right(120)
turtle.forward(length)
turtle.right(120)
turtle.forward(length)
turtle.right(120)
turtle.end_fill()
turtle.done()

