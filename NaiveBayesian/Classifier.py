import numpy as np
import matplotlib as plt
import seaborn as sns; sns.set()

from sklearn.datasets import make_blobs
X, y = make_blobs(100, 2, centers=2, random_state=2, cluster_std=1.5)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='RdBu');

from sklear.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(X,y);


