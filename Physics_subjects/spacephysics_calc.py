import numpy as np
#universal constants
m_p = 1.67e-27 #kg
m_e = 9.109e-31 #kg
pi = np.pi
e = 1.602e-19 #C
epsilon = 8.85e-12 #Farad /m base permitivity

E = 20000*1.60e-19
alpha = np.pi*30/180
omega = 574.85
_B = 0.06
B_00 = 30e-3
L = (((B_00/_B)* (1+np.sin(alpha)**2)**(0.5))/(np.cos(alpha)**6))**(1./3)
#print(L)
v = (E*2/m_p)**(0.5)*np.sin(alpha)
r = v /omega
#print(r)
v =(E*2/m_p)**(0.5)
__B = 0.24
r = v*m_p/(__B*e)
#print(r)

"""
Calculating the gyrofrequency and plasmafrequency of the F2 region
"""

def plasma_freq(N_e):
    f_p = np.sqrt((e**2 *N_e)/(epsilon *m_e))*1/(2*pi)
    return f_p

def gyro_freq(B_0):
    f_g = B_0*abs(-1*e)/(2*m_e*pi)
    return f_g

N_e = 3.0e+12 # m^-3
B_0 = 5e-5 #T

print('gyro', gyro_freq(B_0), 'plasma', plasma_freq(N_e))
