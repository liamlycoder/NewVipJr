# !/usr/bin/python
# coding: utf8
# Time: 2020/1/21 09:28
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm


# 阶乘
def Factorial(n):
    if n == 1:
        return 1
    return n * Factorial(n - 1)


# 斐波那契非递归
def fab1(n):
    a1 = 1
    a2 = 1
    a3 = 1
    while (n-2 > 0):
        a3 = a1 + a2
        a1 = a2
        a2 = a3
        n -= 1
    return a3


# 斐波那契递归
def fab2(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fab2(n-1) + fab2(n-2)


# 汉诺塔
def hanoi(n, x, y, z):
    if n == 1:
        print(x, "--->", z)
    else:
        hanoi(n-1, x, z, y)
        print(x, "--->", z)
        hanoi(n-1, y, x, z)

# 命令： python3 -m turtledemo.minimal_hanoi


if __name__ == '__main__':
    hanoi(3, 'X', 'Y', 'Z')

