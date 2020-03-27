# !/usr/bin/python
# coding: utf8
# Time: 2020/3/28 00:47
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np
from sklearn.svm import SVC

X, y = make_blobs(n_samples=50, centers=2, random_state=0, cluster_std=0.6)
clf = SVC(kernel='linear').fit(X, y)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap="rainbow")
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()
x = np.linspace(xlim[0], xlim[1], 30)
y = np.linspace(ylim[0], ylim[1], 30)
Y, X = np.meshgrid(y, x)
xy = np.vstack([X.ravel(), Y.ravel()]).T
# plt.scatter(xy[:,0],xy[:,1],s=1,cmap="rainbow")
# plt.show()

P = clf.decision_function(xy).reshape(X.shape)
ax.contour(X, Y, P, colors="k", levels=[-1, 0, 1], alpha=0.5, linestyles=["--", "-", "--"])
ax.set_xlim(xlim)
ax.set_ylim(ylim)
plt.show()

"""举例
x = np.linspace(xlim[0], xlim[1], 30)
y = np.linspace(ylim[0], ylim[1], 30)
a = [1, 2, 3, 4]
b = [5, 6]
aa, bb = np.meshgrid(a, b)
print(aa.ravel())
print(bb.ravel())
xp = np.vstack([aa.ravel(), bb.ravel()]).T
print(xp)
"""
