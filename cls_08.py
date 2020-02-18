# !/usr/bin/python # coding: utf8
# Time: 2020/1/22 15:48
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import turtle


"""
# 上节课作业
turtle.speed(0)
for j in range(100):
    for i in range(4):
        if i == 2:
            turtle.down()
        else:
            turtle.penup()
        turtle.forward(j)
        turtle.left(90)
turtle.done()
turtle.speed(0)
turtle.hideturtle()
for c in range(3, 30):
    turtle.fillcolor(c/30, 0, 0)
    turtle.begin_fill()
    for i in range(c):
        turtle.forward(c)
        turtle.left(360/c)
    turtle.end_fill()
turtle.done()
"""
"""
# 经典鸡兔同笼
heads = 35
feet = 94
for rooster in range(1, heads+1):
    rabbit = heads - rooster
    if 2*rooster + 4*rabbit == feet:
        print("鸡有{}只, 兔有{}只".format(rooster, rabbit))
"""

# 升级版鸡兔同笼
heads = int(input('请输入鸡和兔的头的总数：'))
feet = int(input('请输入鸡和兔的脚的总数：'))
for rooster in range(1, heads+1):
    rabbit = heads - rooster
    if 2*rooster + 4*rabbit == feet:
        print("鸡有{}只, 兔有{}只".format(rooster, rabbit))
        break
else:
    print('{}只头，{}只脚的情况无解'.format(heads, feet))




