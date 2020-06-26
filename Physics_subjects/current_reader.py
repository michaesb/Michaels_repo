import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio

mat = sio.loadmat('matlab_data.mat')
print (np.array(mat))
data = mat.get('ICI2_dataInterp')
time = mat.get('Time')
print (data)
plt.plot(time, data)
plt.legend(['2.5V','4V','5.5V','10V'])
plt.show()
