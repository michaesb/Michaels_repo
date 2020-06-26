import numpy as np
import matplotlib.pyplot as plt

L1 = 100.9 #mm
L2 = 222.1 #mm
L3 = 136.2 #mm

m1 = 0.3833 # kg
m2 = 0.2724 #kg
m3 = 0.1406 #kg
m = np.array([m1,m2,m3])
g = -9.81

def J_v(theta):
    c1 = np.cos(theta[0]); c2 = np.cos(theta[1]); c3 = np.cos(theta[2])
    s1 = np.sin(theta[0]); s2 = np.sin(theta[1]); s3 = np.sin(theta[2])
    ############################################################################
    J_v2 = np.array([[-L2*s1*s2, -L2*s2*(s1-c1)],[L2*c2*c1, L2*(c1*c2- s2*s1)],
                    [0, L2*((s1**2)*s2- (c1**2)*c2)]])

    J_v3 = np.array([[-s1*(L2*c2+L3*np.cos(theta[1] +theta[2])),\
    -c1*(L2*s2+L3*np.sin(theta[1]+ theta[2])),+
    -c1*(L3*np.sin(theta[1] + theta[2]))],\
    [c1*(L2*c2+L3*np.cos(theta[1] +theta[2])),\
    -s1*(L2*s2+L3*np.sin(theta[1]+ theta[2])),\
    -s1*(L3*np.sin(theta[1] + theta[2]))], \
    [0, (L2*c2+L3*np.cos(theta[1]+ theta[2])), L3*np.cos(theta[1] + theta[2])]])
    return J_v2,J_v3

def J_w(theta):
    Jw1 =np.array([0,0,1] )
    Jw2 =np.array([[0,np.sin(theta[0])],[0,-np.cos(theta[0])],[1,0]] )
    Jw3 =np.array([[0,np.sin(theta[0]),np.sin(theta[0])], \
    [0,-np.cos(theta[0]),-np.cos(theta[0])],[1,0,0]] )
    return Jw1,Jw2,Jw3

def R(theta):
    c1 = np.cos(theta[0]); c2 = np.cos(theta[1]); c3 = np.cos(theta[2])
    s1 = np.sin(theta[0]); s2 = np.sin(theta[1]); s3 = np.sin(theta[2])
    R1 = np.array([[c1, 0, s1],[s1,0,-c1],[0,1,0]])
    R2 = np.array([[c1*c2, -c1*s2, s1],[s1*c2,-s1*s2,-c1],[s2,c2,0]])
    R3 = np.array([[c1*c2*c3 -c1*s2*s3, -c1*c2*s3-c1*s2*s3, s1],\
    [s1*c2*c3-s1*s2*s3,-s1*c2*s3-s1*s2*c3,-c1],[s2*c3+c2*s3,c2*c3+s2*s3,0]])
    return R1, R2, R3

def Inertiamatrixmaker(x,y,z):
    I = np.array([[x,0,0],[0,y,0],[0,0,z]])
    return I

I1 = Inertiamatrixmaker(2.5135, 0.9198, 1.8316)
I2 = Inertiamatrixmaker(3.0675, 0.2234, 2.9577)
I3 = Inertiamatrixmaker(0.1171, 2.1680, 2.1680)

def matrix_tri_multiplier(I,R):
    "multiplies the matrices I R I.T together"
    IR = np.dot(I, R)
    return np.dot(IR, np.transpose(I))

def potential(m,theta):
    P1 = m[0]*g*L1
    P2 = m[1]*g*(L1 + L2*np.sin(theta[1]))
    P3 = m[2]*g*(L3*np.sin(theta[1]+theta[2]) + L2*np.sin(theta[1]) + L1)
    return P1 + P2 + P3

print('P =', potential(m,(0,0,0)))

def kinetic(m,theta,omega):
    #### Translatoric #####
    # v1 is zero because theta1 doesn't move the mass center
    theta_ = theta[0]
    omega_ = omega[0]
    omega2 = np.array([omega[0,0:2]]) # creating the right type of array
    J_v2,J_v3 = J_v(theta_)
    v2, v3 = np.dot(J_v2, omega2.T), np.dot(J_v3, omega.T)
    K_T2 = m[1]*np.dot(v2.T,v2)[0,0]
    K_T3 = m[2]*np.dot(v3.T,v3)[0,0]
    #### Rotational ######
    J_w1, J_w2, J_w3 = J_w(theta_)
    w1 = np.array([J_w1* omega_[0]])
    w2 = np.array([np.dot(J_w2, omega2.T)])[0]
    w3 = np.array([np.dot(J_w3, omega.T)])[0]
    IR1I, IR2I,IR3I = matrix_tri_multiplier(I1,R(theta_)[0])\
    ,matrix_tri_multiplier(I2,R(theta_)[1]), matrix_tri_multiplier(I3,R(theta_)[2])
    print('w2.T=',w2.T, 'IR2I.T=',IR2I.T, 'w2=', w2)
    print('w2=', w2,'IR2Iw2=',np.dot(IR2I.T,w2))
    K_R1 = np.dot(w1,np.dot(IR1I,w1.T))
    K_R2 = np.dot(w2.T,np.dot(IR2I.T,w2))
    K_R3 = np.dot(w3.T,np.dot(IR3I.T,w3))
    #print('K1',K_R1)
    #print('K2',K_R2)
    #print('K3',K_R3)
    print('KT2=',K_T2,'KT3=',K_T3,'KR1=',K_R1,'KR2=',K_R2,'KR3=',K_R3)
    return 0.5*(K_T2+K_T3+K_R1+K_R2+K_R3)

theta_ = np.array([[1,1,1]])
omega_ = np.array([[4,2,0.5]])

print('K=', kinetic(m, theta_, omega_))

def torque(theta, omega,)
