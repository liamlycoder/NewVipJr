# !/usr/bin/python
# coding: utf8
# Time: 2020/6/6 19:02
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
from tkinter import *
win = Tk()
win.title("计算器v1.0")
win.geometry("255x455")


def numInput(number):
    first_num = en.get()
    en.delete(0, END)
    en.insert(0, first_num + str(number))


def clear():
    en.delete(0, END)


def plus():
    global operator
    global first_num
    first_num = en.get()
    en.delete(0, END)
    operator = "addition"

def equal():
    global operator
    global first_num
    second_num = en.get()
    en.delete(0, END)
    if operator == "addition":
        en.insert(0, int(first_num) + int(second_num))


bu7 = Button(win, text=7, width=2, font=("Arial", 31), command=lambda: numInput(7))
bu8 = Button(win, text=8, width=2, font=("Arial", 31), command=lambda: numInput(8))
bu9 = Button(win, text=9, width=2, font=("Arial", 31), command=lambda: numInput(9))
bu4 = Button(win, text=4, width=2, font=("Arial", 31), command=lambda: numInput(4))
bu5 = Button(win, text=5, width=2, font=("Arial", 31), command=lambda: numInput(5))
bu6 = Button(win, text=6, width=2, font=("Arial", 31), command=lambda: numInput(6))
bu1 = Button(win, text=1, width=2, font=("Arial", 31), command=lambda: numInput(1))
bu2 = Button(win, text=2, width=2, font=("Arial", 31), command=lambda: numInput(2))
bu3 = Button(win, text=3, width=2, font=("Arial", 31), command=lambda: numInput(3))
bu0 = Button(win, text=0, width=2, font=("Arial", 31), command=lambda: numInput(0))
bu_eq = Button(win, text="=", font=("Arial", 31), command=equal)
bu_clear = Button(win, text="C", width=2, font=("Arial", 31), command=clear)
bu_add = Button(win, text="+", width=2, font=("Arial", 31), command=plus)
bu_min = Button(win, text="-", width=2, font=("Arial", 31))
bu_mul = Button(win, text="*", width=2, font=("Arial", 31))
bu_div = Button(win, text="/", width=2, font=("Arial", 31))


bu7.place(x=10, y=100)
bu8.place(x=70, y=100)
bu9.place(x=130, y=100)
bu4.place(x=10, y=185)
bu5.place(x=70, y=185)
bu6.place(x=130, y=185)
bu1.place(x=10, y=270)
bu2.place(x=70, y=270)
bu3.place(x=130, y=270)
bu_eq.place(x=10, y=355)
bu0.place(x=70, y=355)
bu_clear.place(x=130, y=355)
bu_add.place(x=190, y=100)
bu_min.place(x=190, y=185)
bu_mul.place(x=190, y=270)
bu_div.place(x=190, y=355)

en = Entry(win, width=10, font=("Arial", 31))
en.place(x=10, y=30)

mainloop()

