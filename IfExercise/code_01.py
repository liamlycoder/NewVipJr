# !/usr/bin/python
# coding: utf8
# Time: 2020/5/12 10:17
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
x = input("请输入两个数字：")
a, b = map(int, x.split())
if a > b:
    a, b = b, a
print("排序后：", a, b)
