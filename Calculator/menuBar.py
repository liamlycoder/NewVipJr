# !/usr/bin/python
# coding: utf8
# Time: 2020/3/11 17:37
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import tkinter as tk

screen = tk.Tk()
screen.title("史上最强窗口")
screen.geometry('800x600')

resultLabel = tk.Label(master=screen, bg='pink')
resultLabel.place(x=30, y=30, width=740, height=60)


def newPro():
    resultLabel.config(text='您点击了New Project...')


def New():
    resultLabel.config(text='您点击了New...')


def otherSet():
    resultLabel.config(text='您点击了Other Settings')


menubar = tk.Menu(master=screen)
filemenu = tk.Menu(master=menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New Project...', command=newPro)
filemenu.add_command(label='New...', command=New)
filemenu.add_separator()
filemenu.add_command(label='Other Settings', command=otherSet)

editmenu = tk.Menu(master=menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Copy Path')

screen.config(menu=menubar)

screen.mainloop()
