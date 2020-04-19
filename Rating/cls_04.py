'''
@Author: Liam
@E-mail: luyu.real@qq.com
@Date: 2020-04-19 13:05:26
@LastEditTime: 2020-04-19 13:43:12
@Software: Visual Studio Code
'''
import turtle as t

red_x = 300
orange_x = red_x - 20
yellow_x = orange_x - 20
green_x = yellow_x - 20
cyan_x = green_x - 20
blue_x = cyan_x - 20
purple_x = blue_x - 20

red_r = 300
orange_r = red_r - 20
yellow_r = orange_r - 20
green_r = yellow_r - 20
cyan_r = green_r - 20
blue_r = cyan_r - 20
purple_r = blue_r - 20


t.penup()
t.goto(red_x, 0)
t.down()
t.lt(90)
t.pensize(30)
t.pencolor("red")
t.circle(red_r, 180, steps=15)

t.penup()
t.goto(orange_x, 0)
t.down()
t.lt(180)
t.pensize(30)
t.pencolor("orange")
t.circle(orange_r, 180, steps=15)

t.penup()
t.goto(yellow_x, 0)
t.down()
t.lt(180)
t.pensize(30)
t.pencolor("yellow")
t.circle(yellow_r, 180, steps=15)

t.penup()
t.goto(green_x, 0)
t.down()
t.lt(180)
t.pensize(30)
t.pencolor("green")
t.circle(green_r, 180, steps=15)

t.penup()
t.goto(cyan_x, 0)
t.down()
t.lt(180)
t.pensize(30)
t.pencolor("cyan")
t.circle(cyan_r, 180, steps=15)

t.penup()
t.goto(blue_x, 0)
t.down()
t.lt(180)
t.pensize(30)
t.pencolor("blue")
t.circle(blue_r, 180, steps=15)

t.penup()
t.goto(purple_x, 0)
t.down()
t.lt(180)
t.pensize(30)
t.pencolor("purple")
t.circle(purple_r, 180, steps=15)

t.done()
