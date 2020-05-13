# !/usr/bin/python
# coding: utf8
# Time: 2020/5/12 10:25
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import sys
score = int(input("请输入分数："))
if score > 100 or score < 0:
    print("输入的数据不合法")
    sys.exit()
elif score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('E')


