# !/usr/bin/python
# coding: utf8
# Time: 2020/7/29 18:07
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import tensorflow as tf

# 定义了一个随机数（标量）
random_float = tf.random.uniform(shape=())

# 定义一个有2个元素的零向量
zero_vector = tf.zeros(shape=(2))

# 定义两个2x2的常量矩阵
A = tf.constant([
    [1., 2.],
    [3., 4.]
])

B = tf.constant([
    [5., 6.],
    [7., 8.]
])

C = tf.add(A, B)
D = tf.matmul(A, B)

# print(A.shape)
# print(A.dtype)
# print(A.numpy())
print(C)
print(D)


