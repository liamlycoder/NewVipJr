# !/usr/bin/python
# coding: utf8
# Time: 2020/2/16 17:27
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
def discounts(price, rate):
    final_price = price * (rate / 10)
    return final_price


# print(final_price)  # final_price为函数discounts的局部变量，在函数外面已经死亡了
old_price = float(input('原价：'))
rate = float(input('折扣：'))
new_price = discounts(old_price, rate)
print("折后价：{}".format(new_price))


# 问题一：如果在函数内部也定义一个old_price呢？那么在外面使用该变量会是全局还是局部？
def discounts2(price, rate):
    old_price = 100  # 局部变量old_price
    final_price = price * (rate / 10)
    return final_price


old_price = 200
res = discounts2(old_price, 8)
print(res)  # 说明当局部变量和全局变量冲突时，在函数外面使用的是全局变量


# 问题二：如果在函数内部使用一个和全局变量同名的局部变量会怎样？
def discounts3(rate):
    old_price = 100
    final_price = old_price * (rate / 10)
    return final_price


old_price = 200
res = discounts3(8)
print(res)  # 在函数内部发生冲突，则函数内使用的是局部变量

# 问题三：那如果我非要在函数内部使用全局变量应该怎么办呢？
old_price = 200


def discounts4(rate):
    global old_price
    final_price = old_price * (rate / 10)
    return final_price


print(discounts4(8))
