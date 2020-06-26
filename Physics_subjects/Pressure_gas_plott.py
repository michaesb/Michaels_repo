import numpy as np
import matplotlib.pyplot as plt

N = 6.022e+23 #number of molecules
k = 1.38e-23
P_c = 33.6 #Pa
T_c = 126 #K
V_c = 0.089 #l/mol
T = np.array([77.,100.,110.,115.,120.,125.])/T_c
V_r = np.linspace(1.5/3.5,40,1000)
def P(T,V,N):
    P_r = 8.*T/(3.*V -1.) -  3./(V**2)
    return P_r


for i in T:
    plt.plot(V_c*V_r,P_c*P(i,V_r,N))
plt.title('wan der Waals gas for multiple temperatures')
plt.xlabel('V/V_c')
plt.ylabel('P/P_c')
#plt.savefig('Wan_der_Waals_plot')
plt.show()

string_list = []
V = np.linspace(0.0333,1e100,1000)/V_c

plt.plot(V,P(T[5],V_r,N)/P_c)
plt.savefig('125 K')
plt.show()
