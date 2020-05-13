# !/usr/bin/python
# coding: utf8
# Time: 2020/5/12 10:28
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import sys

year = input("请输入一个四位数的年份：")
if len(year) != 4:
    print('输入错误')
    sys.exit()
else:
    year = int(year)
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print('是闰年')
    else:
        print("不是闰年")
