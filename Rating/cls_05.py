'''
@Author: Liam
@E-mail: luyu.real@qq.com
@Date: 2020-04-19 12:00:38
@LastEditTime: 2020-04-19 12:59:18
@Software: Visual Studio Code
'''
import turtle as t
import time

"""
print("To see a world in a grain of sand.")
time.sleep(5)
print("And a heaven in a wild flower.")
time.sleep(5)
print("Hold infinity in the palm of your hand.")
time.sleep(5)
print("And eternity in an hour.")
"""

t.pensize(10)  # 设置画笔粗细

# 绘制外边框
t.fd(130)
t.lt(90)
t.fd(330)
t.lt(90)
t.fd(130)
t.lt(90)
t.fd(330)

t.hideturtle()   # 隐藏海龟
t.speed(0)  # 将画笔速度调到最快
t.pencolor('white')

# 绘制红灯
t.penup()
t.goto(35, 260)
t.pendown()
t.fillcolor('red')
t.begin_fill()
t.circle(30)
t.end_fill()

# 暂停2秒
time.sleep(2)

# 撤销红灯
t.undo()

# 绘制黄灯
t.penup()
t.goto(35, 170)
t.pendown()
t.fillcolor('orange')
t.begin_fill()
t.circle(30)
t.end_fill()

# 暂停2秒
time.sleep(2)

# 撤销红灯
t.undo()

# 绘制绿灯
t.penup()
t.goto(35, 80)
t.pendown()
t.fillcolor('green')
t.begin_fill()
t.circle(30)
t.end_fill()

# 绘制完成
t.done()
