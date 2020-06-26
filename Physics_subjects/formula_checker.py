import numpy as np

_M_2 = 1.666; M2 = 1.666
_M_1 = 1.555; M1 = 1.555
_L_1 = 1.444; L1 = 1.444
_L_2 = 1.333; L2 = 1.333
diff_theta = np.pi; deltat = np.pi
y = [1.22,1.11, 0.99, 0.88]
g = 9.81
d_omega_1 = (_M_2 *_L_1*(y[1]**2)*np.sin(diff_theta)*np.cos(diff_theta)\
                    +_M_2*g*np.sin(y[2])*np.cos(diff_theta)\
                    + _M_2*_L_2*(y[3]**2)*np.sin(diff_theta)\
                    -(_M_1 + _M_2) *g*np.sin(y[0]))\
                    /((_M_1 + _M_2)*_L_1 \
                    - _M_2*_L_1*(np.cos(diff_theta)**2))

domega1 = (M2*L1*(y[1]**2)*np.sin(deltat)*np.cos(deltat) \
                   + M2*g*np.sin(y[2])*np.cos(deltat) \
                   + M2*L2*(y[3]**2)*np.sin(deltat) \
                   - (M1 + M2)*g*np.sin(y[0]) \
                    )/((M1 + M2)*L1  \
                        - M2*L1*(np.cos(deltat)**2))

domega2 = (-M2*L2*y[3]**2*np.sin(deltat)*np.cos(deltat) \
                   + (M1 + M2)*g*np.sin(y[0])*np.cos(deltat) \
                   - (M1 + M2)*L1*y[1]**2*np.sin(deltat) \
                   - (M1 + M2)*g*np.sin(y[2])
                    )/((M1 + M2)*L2 \
                        - M2*L2*np.cos(deltat)**2)

d_omega_2 = (-_M_2 *_L_2*(y[3]**2)*np.sin(diff_theta)*np.cos(diff_theta)\
                  + (_M_1 + _M_2)*g*np.sin(y[0])*np.cos(diff_theta) \
                  - (_M_1 + _M_2)*_L_1*(y[1]**2)*np.sin(diff_theta)\
                  - (_M_1 + _M_2) *g*np.sin(y[2]))\
                  /((_M_1 + _M_2)*_L_2\
                  -_M_2*_L_2*np.cos(diff_theta)**2)

if d_omega_1 == domega1:
    print 'yes'


if d_omega_2 == domega2:
    print 'yes'
