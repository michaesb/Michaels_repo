from numpy import cos,sin,pi,array
import numpy as np
import matplotlib.pyplot as plt

L1 = 100.9 #mm
L2 = 222.1 #mm
L3 = 136.2 #mm

tol = 1e-6

def forward2(theta1, theta2):
    Px = L2*cos(theta1)*cos(theta2)
    Py = L2*cos(theta2)*sin(theta1)
    Pz = L2*sin(theta2) + L1
    return [Px,Py,Pz]

def forward3(theta1, theta2, theta3):
    Px = L3*cos(theta3)*cos(theta1)*cos(theta2)- L3*sin(theta2)*cos(theta1)*sin(theta3)\
    +L2*cos(theta1)*cos(theta2)
    Py = L3*cos(theta2)*cos(theta3)*sin(theta1)- L3*sin(theta2)*sin(theta1)*sin(theta3)\
    +L2*cos(theta2)*sin(theta1)
    Pz = L3*sin(theta1)*cos(theta3)+L3*sin(theta3)*cos(theta2)+ L2*sin(theta2)+L1
    return Px, Py, Pz

def inverse3(Px,Py,Pz):
    """number of solutions wanted n. ex: n=1 gives on set of solution"""
    if np.sqrt(Px**2 +Py**2 +Pz**2) > (L1+L2+L3) or np.sqrt(Px**2 + Py**2) > (L2+L3):
        raise ValueError('The values are outside the workspace of the robot')
        #set2 = np.ones_like(set1); set3 = np.ones_like(set1); set4 = np.ones_like(set1)
    set = np.ones(3)
    r = np.sqrt(Px**2 + Py**2)
    s = Pz-L1
    c = np.sqrt(r**2 + s**2)
    #############################
    if s == 0:
        Beta = 0
    else:
        Beta  = np.arctan(r/s)
    #############################
    if Py<tol:
        set[0] = 0
    elif Px<tol:
        set[0] =  np.pi/2
    else:
        set[0]= np.arctan2(Py,Px)

    set[1] = np.arccos((-c**2 + L2**2 +L3**2 )/(2*L2*L3))
    print ((L2**2 +c**2 -L3**2)/(2*L2*c))
    print (Beta)
    set[2] = np.arccos((L2**2 +c**2 -L3**2)/(2*L2*c)) + Beta

    if np.sin(set[2]) < tol or (L3*np.cos(set[1] +set[2]) +L2*np.cos(set[1])) <tol:
        raise VaulueError('The robot is approching a singularity')
    return set

def plot_robot():
    """ Plots a configuration of the robot """
    Px2,Py2,Pz2 =forward2(0,0)
    Px3,Py3,Pz3 =forward3(0,0,np.pi/2)
    print (Px2,Pz2)
    print (Px3,Pz3)
    x = array([0,0,Px2,Px3])
    y = array([0,L1,Pz2,Pz3])
    plt.plot(x,y)
    plt.axis('equal')
    plt.show()
print(forward3(0,0,0))
Px,Py,Pz = forward3(0,0,np.pi/2)
print(Px,Py,Pz)
print(inverse3(L2,0,L1+L3))


"""
Tried to get the inverse kinematics to work for many hours, but couldn't get it
to work. I Get one solution correctly, but I am struggling on how to get more than one.
Feedback, or a working script would be appreciated to get a functioning.
kinematics.

In task 5c) I would write:
Px, Py, Pz = forward(0,0,np.pi/2)
print (inverse3(Px,Py,Pz,1) )
to check if I get the same answers

In task 5d) I would input the coordinates into the inverse:
print(inverse3(0,-323.9033,176.6988,4))
"""
