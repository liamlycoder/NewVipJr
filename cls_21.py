# !/usr/bin/python
# coding: utf8
# Time: 2020/1/18 12:24
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import turtle


def yu(radius, color1, color2):
    t.color('black', color1)
    t.begin_fill()
    t.circle(radius / 2, 180)
    t.circle(radius, 180)
    t.left(180)
    t.circle(-radius / 2, 180)
    t.end_fill()
    t.left(90)
    t.penup()
    t.fd(radius * 0.35)
    t.right(90)
    t.down()
    t.color('black', color2)
    t.begin_fill()
    t.circle(radius * 0.15)
    t.end_fill()
    t.left(90)
    t.up()
    t.bk(radius * 0.35)
    t.down()
    t.left(90)


def Main():
    yu(200, 'black', 'white')
    yu(200, 'white', 'black')


t = turtle.Pen()
Main()
turtle.done()
