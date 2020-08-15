import numpy as np
import matplotlib.pyplot as plt

def beta(X,y):
    beta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
    return beta

def f(x):
    return 5*x*x+0.5*x


x_min= 0
x_max = 1
n = 100
x = np.linspace(x_min,x_max,n)
epsilon = 20*np.random.random(n)


y = f(x) +epsilon

X = np.c_[np.ones(n,dtype=int), x, x**2]


n_plot=20
x_plot=np.linspace(x_min,x_max,n_plot)
X_plot= np.c_[np.ones(n_plot),x_plot,x_plot**2]
beta = beta(X,y)
y_model = X_plot @beta

plt.plot(x,f(x)+ np.mean(epsilon),"r")
plt.plot(x,y,'b*',)
plt.plot(x_plot, y_model, "g",linewidth=3)
plt.title('OLS second order regression')
plt.legend(["true pattern ","y_data", "y_model"])
plt.show()
