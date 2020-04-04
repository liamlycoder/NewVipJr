from sklearn.datasets import make_blobs
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np
X, y = make_blobs(n_samples=50, centers=2, random_state=0, cluster_std=0.6)
clf = SVC(kernel="linear").fit()
clf.fit(X, y)
plt.scatter(X[:, 0], X[:, 1], c=y,s=50,cmap='rambow'
ax=plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

x = np.linspace(xlim[0], xlim[1], 30)
y = np.linspace(ylim[0], ylim[1], 30)
Y, X = np.meshgrid(y, x)
xy = np.vstack([X.ravel(), Y.ravel()]).T
P = model.decision_function(xy).reshape(X.shape)
"""
n_samples = 100
datasets = [
    make_circles(n_samples=n_samples, noise=0.2, factor=0.5, random_state=1)
]
Kernel = ["linear", "poly", "rbf", "sigmoid"]
for X,Y in datasets:
     plt.figure(figsize=(5,4))
     plt.scatter(X[:,0],X[:,1],c=Y,s=50,cmap="rainbow")
plt.show()
"""
