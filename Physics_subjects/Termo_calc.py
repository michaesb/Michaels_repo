import numpy as np
import matplotlib.pyplot as plt
import scipy as sci
k = 8.617e-5 # eV /K
T = 300 #K
E1 = np.array([-0.1, -0.05, 0, 0.05, 0.1 ])
def Partition(E):
    z =(np.exp(-E/(k*T)))
    Z = np.sum(z)
    return Z

Z1 = Partition(E1)
print('Z1',Z1)

def Probability(E):
    Z = Partition(E)
    P = np.exp(-E/(k*T))/Z
    return P

P1 = Probability(E1)
for i in P1:
    print(("possible %f")%i)
#print('total possiblity1', np.sum(P1))
#---------------------
E2 = np.array([0,0.05,0.1,0.15,0.2])
Z2 = Partition(E2)
print('Z2',Z2)

P2 = Probability(E2)
for i in P2:
    print(("possible %f")%i)
#print('total possiblity2', np.sum(P2))

#-------------------------
#Oppg.3
#-------------------------
k = 1.38e-23 # J/K
m = 0.028 #kg/mol
M = 0.028/(6.022e+23) #kg
T1 = 300 # K
T2 = 600 # K

def max_(T):
    v = np.sqrt(2*k*T/M)
    return v

def rms(T):
    v = np.sqrt(3*k*T/M)
    return v

def average(T):
    v = np.sqrt(8*k*T/(np.pi*M))
    return v

def D(v,T,M_):
    D = ((M_/(2.*np.pi*k*T))**(1.5))*4.*np.pi*(v**2)*np.exp(-M_*v**2/(2*k*T))
    return D

print("ave= ",str(average(T1)),"v_rms = ",str(rms(T1)),"v_p = ",str(max_(T1)))
print("ave= ",str(average(T2)),"v_rms = ",str(rms(T2)),"v_p = ",str(max_(T2)))
v =np.linspace(0,2000,1000)

plt.plot(v,D(v,T1,M))
plt.plot(v,D(v,T2,M))
plt.legend(['T = 300K','T = 600K'])
plt.xlabel('v [m/s]')
plt.ylabel('D(v)')
plt.show()

N = 10000.
a = 1000.
b = 1500.

m_h2 = 0.002/(6.022e+23) #kg
m_he = 0.004/(6.022e+23) #kg
T3 = 1000

v_300 = np.linspace(0,300,N)
dx_300 = 300/N
v_11000 = np.linspace(11000,1e6,N)
dx_11000 = (10**6 -1100.)/N

print('speed under 300  m/s ', np.trapz(D(v_300, T1, M), dx = dx_300))

print('escape velocity 11 km/s and prosentage of N_2 gas that has this or higher is=',np.trapz(D(v_11000,T3,M),dx = dx_11000))

print('escape velocity 11 km/s and prosentage of H_2 gas that has this or higher is=',np.trapz(D(v_11000,T3,m_h2),dx = dx_11000))

print('escape velocity 11 km/s and prosentage of He gas that has this or higher is=',np.trapz(D(v_11000,T3,m_he),dx = dx_11000))
v_2400= np.linspace(2400,1e+6,N)
dx_2400 = (1e+6-2400)/N
print('escape velocity 2.4 km/s and prosentage of N_2 gas that has this or higher is=',np.trapz(D(v_2400,T3,M),dx = dx_2400))

"""
v= np.linspace(200,17000,N)
plt.plot(v,D(v,T3,m_h2))
plt.plot(v,D(v,T3,m_he))
#plt.plot((11000,11000),(0,0.0004),'k-')
plt.legend(['H_2','He'])
plt.xlabel('v [m/s]')
plt.ylabel('D(v)')
plt.show()

v1 = np.linspace(200,5000, N)
plt.plot(v1,D(v1,T3,M))
plt.plot((2400,2400),(0,0.0008),'k-')
plt.xlabel('v [m/s]')
plt.ylabel('D(v)')
plt.show()
"""
