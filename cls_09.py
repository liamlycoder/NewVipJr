# !/usr/bin/python
# coding: utf8
# Time: 2020/1/22 19:20
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import random
targetNum = random.randint(1, 5)
for i in range(3):
    yourNum = int(input("你猜猜看是几？（不许猜0）"))
    if yourNum == 0:
        print("你浪费了一次机会")
        continue
    if yourNum == targetNum:
        print("天才啊，竟然猜对了")
        break
    elif yourNum > targetNum:
        print("猜大了")
    elif yourNum < targetNum:
        print("猜小了")
else:
    print("运气有点差哈, 正确的结果是{}".format(targetNum))
