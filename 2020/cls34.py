# !/usr/bin/python
# coding: utf8
# Time: 2020/9/13 下午12:21
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import turtle

state = {"turn": 100}


def spinner():
    turtle.clear()

    angle = state['turn'] / 10
    turtle.left(angle)

    turtle.pensize(10)
    turtle.fd(80)
    turtle.dot(60, "red")
    turtle.penup()
    turtle.goto(0, 0)
    turtle.left(120)
    turtle.pendown()
    turtle.fd(80)
    turtle.dot(60, "blue")
    turtle.penup()
    turtle.goto(0, 0)
    turtle.left(120)
    turtle.pendown()
    turtle.fd(80)
    turtle.dot(60, "green")
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.left(120)


def animate():
    # if state['turn'] > 0:
    #     state['turn'] -= 1
    spinner()
    turtle.ontimer(animate, 20)



if __name__ == '__main__':
    turtle.ht()
    turtle.tracer(False)
    animate()
    turtle.done()
