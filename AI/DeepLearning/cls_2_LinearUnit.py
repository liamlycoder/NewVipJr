# !/usr/bin/python
# coding: utf8
# Time: 2020/5/23 0:22
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
from cls_1_Perceptron import Perceptron

f = lambda x: x


class LinearUnit(Perceptron):
    def __init__(self, input_num):
        Perceptron.__init__(self, input_num, f)


if __name__ == '__main__':
    input_vecs = [[5], [3], [8], [1.4], [10.1]]
    labels = [5500, 2300, 7600, 1800, 11400]
    lu = LinearUnit(1)
    lu.train(input_vecs, labels, 10, 0.01)
    print(lu)
    print('Work 3.4 years, monthly salary = {:.2f}'.format(lu.predict([3.4])))
    print('Work 15 years, monthly salary = {:.2f}'.format(lu.predict([15])))
    print('Work 1.5 years, monthly salary = {:.2f}'.format(lu.predict([1.5])))
    print('Work 6.3 years, monthly salary = {:.2f}'.format(lu.predict([6.3])))

    import matplotlib.pyplot as plt
    import numpy as np

    x = np.array(input_vecs)
    y = np.array(labels)
    line_x = np.linspace(0, 15, 500)
    line_y = lu.weights[0] * line_x + lu.bias
    plt.plot(line_x, line_y, '-r')
    plt.scatter(x, y)
    plt.show()
