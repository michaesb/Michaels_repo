import numpy as np

m_p = 1.67e-24
q = 1.60e-19
r_e = 6370e+3
M = 7.8e+15
u_0 = 4*np.pi*1e-8

radius_beta_line = lambda L, theta: L*r_e *np.cos(theta)


def oblig3():
    B_oo = 30e-3 #T
    n_sw = float(6e+6)
    K = 0.88
    L = 7.5
    B = B_oo/((L)**(3))
    print(B*np.sqrt((2./(u_0*K*n_sw*m_p)))*10**-3,' km/s')

oblig3()
