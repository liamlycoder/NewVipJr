# !/usr/bin/python
# coding: utf8
# Time: 2020/3/12 18:21
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm


# 1. 首先，函数可以作为参数传递吗？
def op(way, x, y):
    result = way(x, y)
    return result


# def add(x, y):
#     return x + y

# def mul(x, y):
#     return x*y


# 2. 用lambda表达式写匿名函数
# print(op(lambda x, y: x + y, 2, 3))
# print(op(lambda x, y: x * y, 2, 3))


# 3. 使用if条件
get_odd_even = lambda x: 'even' if x % 2 == 0 else "odd"
# print(get_odd_even(44))

# 4. 无参的lambda表达式
generateNum = lambda: [x for x in range(1, 11)]
# print(generateNum())

# 5. map的使用
result = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
# print(list(result))


# 6. reduce的使用
from functools import reduce

res = reduce(lambda x, y: x + y, range(1, 101))
print(res)
