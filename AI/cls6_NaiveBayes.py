# !/usr/bin/python
# coding: utf8
# Time: 2020/4/12 0:09
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm

import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

digits = load_digits()
X, y = digits.data, digits.target

Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, y, test_size=0.3, random_state=420)
# print(Xtrain.shape)
# print(Xtest.shape)
# print(np.unique(Ytrain))

# 可视化数据集
for i in range(1, 11):
    plt.subplot(2, 5, i)  # 划分成2行5列
    plt.imshow(digits.data[i - 1].reshape([8, 8]), cmap=plt.cm.gray_r)
plt.show()

# 建模三步走
gnb = GaussianNB().fit(Xtrain, Ytrain)
acc_score = gnb.score(Xtest, Ytest)
# print(acc_score)

Y_pred = gnb.predict(Xtest)

prob = gnb.predict_proba(Xtest)
# print(prob.shape)

from sklearn.metrics import confusion_matrix as CM

# 打印混淆矩阵
cmresult = CM(Ytest, Y_pred)
print(cmresult)
