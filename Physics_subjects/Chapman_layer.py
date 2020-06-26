import numpy as np
import matplotlib.pyplot as plt

h_max = 350 #km
H = 100 #km
N_max = 3.0e+12 # m^-3

h = np.linspace(100,800,10000) #km
X = np.array([0,20,50,80])*np.pi/180

def N_e(h,X):
    z = (h-h_max)/H
    N = N_max* np.exp(1-z-np.exp(-z)/np.cos(X))
    return N
for x in X:
    plt.plot(N_e(h,x),h)


plt.title('plotted the Chapman layer for different Xenith angles')
plt.legend(['Zenith angle =0','Zenith angle =20','Zenith angle =50','Zenith angle =80'])
plt.xlabel('concentration of electrons [m^-3]')
plt.ylabel('height h [km]')
plt.show()

"""
to Calculate the TEC at a Zenith angle, we use the trapez method as integrator
"""

TEC = np.trapz(N_e(h,0),dx =(800.-100.)/10000.)/1e16
print(TEC)
