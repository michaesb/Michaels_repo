#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
# import sklearn.linear_model as skl
# from sklearn.metrics import mean_squared_error

x = np.random.rand(100, 1)
y = 5*x*x+0.1*np.random.randn(100, 1)

#X = np.asarray([[ 1, x_, x_**2 ] for x_ in x ])
X = np.c_[np.ones(100), x, x**2]

XT = np.transpose(X)
XTX = np.dot( XT, X )
XTy = np.dot( XT, y )
XTXinv = np.linalg.inv(XTX)
beta = np.dot( XTXinv, XTy )

# beta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)

def f(x, beta):
    return beta[2]*x**2 + beta[1]*x + beta[0]



# clf = skl.LinearRegression().fit(X, y)
# ytilde = clf.predict(X)

# øæ'a.'.maefæs()

var = mean_squared_error(y, ytilde)
print(var)



plt.plot(x, y, "r.")
x_ = np.linspace(0, 1, 1000)
plt.plot(x_, f(x_, clf.coef_[0]), "g--")
plt.plot(x_, f(x_, beta), "b-")
plt.show()
