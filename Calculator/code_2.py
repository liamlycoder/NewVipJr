# !/usr/bin/python
# coding: utf8
# Time: 2020/3/11 17:11
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
from tkinter import *
import tkinter.font as tkfont
from tkinter import messagebox


class Calculator(object):
    def __init__(self):
        self.tk = Tk()
        self.tk.title("史上最强计算器")
        self.tk.geometry('370x460')
        self.tk.resizable(0, 0)

        self.EntroyFont = tkfont.Font(root=self.tk, size=13)
        self.ButtonFont = tkfont.Font(root=self.tk, size=12)
        self.count = StringVar()
        self.count.set('0')

        self.label = Label(master=self.tk, bg='#EEE9E9', anchor='e', font=self.EntroyFont, textvariable=self.count)
        self.label.place(x=30, y=10, width=310, height=40)

        self.ButtonList = [
            '清空', '/', '*', '退格', 7, 8, 9, '-', 4, 5, 6, '+', 1, 2, 3, 0,
            '.', '=', '1/x', '%', 'sqrt']  # 按钮文本列表
        self.NumButton = Button(master=self.tk, relief=GROOVE, bg='#EE6A50', text=self.ButtonList[0],
                                font=self.ButtonFont)
        # relief属性用来设置按钮的样式，取值可以有：FLAT， RAISED, SUNKEN, GROOVE, RIDGE
        self.NumButton.place(x=30, y=80, width=70, height=55)
        self.NumButton = Button(master=self.tk, relief=GROOVE, bg='#BFEFFF', text=self.ButtonList[1],
                                font=self.ButtonFont)
        self.NumButton.place(x=110, y=80, width=70, height=55)
        self.NumButton = Button(master=self.tk, relief=GROOVE, bg='#BFEFFF', text=self.ButtonList[2],
                                font=self.ButtonFont)
        self.NumButton.place(x=190, y=80, width=70, height=55)
        self.NumButton = Button(master=self.tk, relief=GROOVE, bg='#EE6A50', text=self.ButtonList[3],
                                font=self.ButtonFont)
        self.NumButton.place(x=270, y=80, width=70, height=55)
        self.NumButton = Button(master=self.tk, relief=GROOVE, bg='#CDBA96', text=self.ButtonList[4],
                                font=self.ButtonFont)
        self.NumButton.place(x=30, y=140, width=70, height=55)
        self.NumButton = Button(master=self.tk, relief=GROOVE, bg='#CDBA96', text=self.ButtonList[5],
                                font=self.ButtonFont)
        self.NumButton.place(x=110, y=140, width=70, height=55)
        self.NumButton = Button(master=self.tk, relief=GROOVE, bg='#CDBA96', text=self.ButtonList[6],
                                font=self.ButtonFont)
        self.NumButton.place(x=190, y=140, width=70, height=55)
        self.NumButton = Button(master=self.tk, relief=GROOVE, bg='#BFEFFF', text=self.ButtonList[7],
                                font=self.ButtonFont)
        self.NumButton.place(x=270, y=140, width=70, height=55)
        self.NumButton = Button(master=self.tk, relief=GROOVE, bg='#CDBA96', text=self.ButtonList[8],
                                font=self.ButtonFont)
        self.NumButton.place(x=30, y=200, width=70, height=55)
        self.NumButton = Button(master=self.tk, relief=GROOVE, bg='#CDBA96', text=self.ButtonList[9],
                                font=self.ButtonFont)
        self.NumButton.place(x=110, y=200, width=70, height=55)
        self.NumButton = Button(master=self.tk, relief=GROOVE, bg='#CDBA96', text=self.ButtonList[10],
                                font=self.ButtonFont)
        self.NumButton.place(x=190, y=200, width=70, height=55)
        self.NumButton = Button(master=self.tk, relief=GROOVE, bg='#BFEFFF', text=self.ButtonList[11],
                                font=self.ButtonFont)
        self.NumButton.place(x=270, y=200, width=70, height=55)
        self.NumButton = Button(master=self.tk, relief=GROOVE, bg='#CDBA96', text=self.ButtonList[12],
                                font=self.ButtonFont)
        self.NumButton.place(x=30, y=260, width=70, height=55)
        self.NumButton = Button(master=self.tk, relief=GROOVE, bg='#CDBA96', text=self.ButtonList[13],
                                font=self.ButtonFont)
        self.NumButton.place(x=110, y=260, width=70, height=55)
        self.NumButton = Button(master=self.tk, relief=GROOVE, bg='#CDBA96', text=self.ButtonList[14],
                                font=self.ButtonFont)
        self.NumButton.place(x=190, y=260, width=70, height=55)
        self.NumButton = Button(master=self.tk, relief=GROOVE, bg='#CDBA96', text=self.ButtonList[15],
                                font=self.ButtonFont)
        self.NumButton.place(x=30, y=320, width=150, height=55)
        self.NumButton = Button(master=self.tk, relief=GROOVE, bg='#EECFA1', text=self.ButtonList[16],
                                font=self.ButtonFont)
        self.NumButton.place(x=190, y=320, width=70, height=55)
        self.NumButton = Button(master=self.tk, relief=GROOVE, bg='#E0EEE0', text=self.ButtonList[17],
                                font=self.ButtonFont)
        self.NumButton.place(x=270, y=260, width=70, height=175)
        self.NumButton = Button(master=self.tk, relief=GROOVE, bg='#BFEFFF', text=self.ButtonList[18],
                                font=self.ButtonFont)
        self.NumButton.place(x=30, y=380, width=70, height=55)
        self.NumButton = Button(master=self.tk, relief=GROOVE, bg='#BFEFFF', text=self.ButtonList[19],
                                font=self.ButtonFont)
        self.NumButton.place(x=110, y=380, width=70, height=55)
        self.NumButton = Button(master=self.tk, relief=GROOVE, bg='#BFEFFF', text=self.ButtonList[20],
                                font=self.ButtonFont)
        self.NumButton.place(x=190, y=380, width=70, height=55)

        # 添加菜单（可选学）
        self.menuBar = Menu(master=self.tk)
        self.tk.config(menu=self.menuBar)
        aboutMenu = Menu(self.menuBar, tearoff=0)
        moreMenu = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label='拓展', menu=moreMenu)
        self.menuBar.add_cascade(label='帮助', menu=aboutMenu)
        aboutMenu.add_command(label='关于', command=self.about)

    def about(self):
        messagebox.showinfo(title='关于', message='作者：Liam\n感谢使用')

    def start(self):
        self.tk.mainloop()


if __name__ == '__main__':
    c = Calculator()
    c.start()
