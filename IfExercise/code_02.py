# !/usr/bin/python
# coding: utf8
# Time: 2020/5/12 10:21
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
jitu = int(input("请输入鸡兔总数："))
tui = int(input("请输入腿的总数："))
tu = (tui - jitu*2) / 2
if int(tu) == tu:
    print("鸡：", jitu-tu, "  兔：", tu)
else:
    print("输入的数据不正确")

