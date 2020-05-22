# !/usr/bin/python
# coding: utf8
# Time: 2020/5/5 0:19
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
from functools import reduce


class Perceptron(object):
    def __init__(self, input_num, activator):
        self.activator = activator
        self.weights = [0.0 for _ in range(input_num)]
        self.bias = 0.0

    def __str__(self):
        return "weights:{}\nbias:{}\n".format(self.weights, self.bias)

    def predict(self, input_vec):
        return self.activator(
            reduce(lambda a, b: a + b, map(lambda x: x[0] * x[1], zip(input_vec, self.weights)), 0.0) + self.bias)

    def _update_weight(self, input_vec, output, label, rate):
        delta = label - output
        self.weights = list(map(lambda x: x[1] + rate * delta * x[0], zip(input_vec, self.weights)))
        self.bias += rate * delta

    def _one_iteration(self, input_vecs, labels, rate):
        samples = zip(input_vecs, labels)
        for input_vec, label in samples:
            output = self.predict(input_vec)
            self._update_weight(input_vec, output, label, rate)

    def train(self, input_vecs, labels, iteration, rate):
        for i in range(iteration):
            self._one_iteration(input_vecs, labels, rate)


def f(x):
    return 1 if x > 0 else 0
    # if x > 0:
    #     return 1
    # else:
    #     return 0


def get_trainning_dataset():
    input_vecs = [[1, 1], [0, 0], [1, 0], [0, 1]]
    labels = [1, 0, 0, 0]
    return input_vecs, labels


def train_and_perceptron():
    p = Perceptron(2, f)
    input_vecs, labels = get_trainning_dataset()
    p.train(input_vecs, labels, 8, 0.1)
    return p


if __name__ == '__main__':
    and_perception = train_and_perceptron()
    print(and_perception)
    print("1 and 1 = {}".format(and_perception.predict([1, 1])))
    print("0 and 0 = {}".format(and_perception.predict([0, 0])))
    print("1 and 0 = {}".format(and_perception.predict([1, 0])))
    print("1 and 1 = {}".format(and_perception.predict([0, 1])))
