import numpy as np
import matplotlib.pyplot as plt


L1 = 100.9 #mm
L2 = 222.1 #mm
L3 = 136.2 #mm

class kinematics():
    def __init__(self,):
        return

    def forward3(self,theta1, theta2, theta3):
        Px = L3*np.cos(theta3 +theta2)*np.cos(theta1)+L2*np.cos(theta1)*np.cos(theta2)
        Py = L3*np.cos(theta2 +theta3)*np.sin(theta1)+L2*np.cos(theta2)*np.sin(theta1)
        Pz = L3*np.sin(theta2 +theta3)+ L2*np.sin(theta2)+L1
        if np.sin(set[2]) < tol or (L3*np.cos(set[1] +set[2]) +L2*np.cos(set[1])) <tol:
            raise VaulueError('The robot is approching a singularity')
        return Px, Py, Pz

    def inverse3(self,Px,Py,Pz):
        """number of solutions wanted n. ex: n=1 gives on set of solution"""
        if np.sqrt(Px**2 +Py**2 +Pz**2) > (L1+L2+L3) or np.sqrt(Px**2 + Py**2) > (L2+L3):
            raise ValueError('The values are outside the workspace of the robot')
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
        set[2] = np.arccos((L2**2 +c**2 -L3**2)/(2*L2*c)) + Beta
        if np.sin(set[2]) < tol or (L3*np.cos(set[1] +set[2]) +L2*np.cos(set[1])) <tol:
            raise VaulueError('The robot is approching a singularity')
        return set

    def Jacobian(self,theta,omega):
        theta1, theta2, theta3 = theta
        omega1, omega2, omega3 = omega

        Px = L3*np.cos(theta3 +theta2)*np.cos(theta1)+L2*np.cos(theta1)*np.cos(theta2)
        Py = L3*np.cos(theta2 +theta3)*np.sin(theta1)+L2*np.cos(theta2)*np.sin(theta1)
        Pz = L3*np.sin(theta2 +theta3)+ L2*np.sin(theta2)+L1
        Vx= -Py*omega1 -np.cos(theta1)*(Pz-L1)*omega2 \
        -np.cos(theta1)*(L3*np.sin(theta2 +theta3))*omega3
        Vy= Px*omega1 -np.sin(theta1)*(Pz-L1)*omega2 \
        -np.sin(theta1)*L3*np.sin(theta2 +theta3)*omega3
        Vz= (np.sin(theta1)*Py + np.cos(theta1)*Px)*omega2\
        +(np.sin(theta1)*(Py- L2*np.cos(theta2)*np.sin(theta1)) \
        +np.cos(theta1)*(Px- L2*np.cos(theta1)*np.cos(theta2)))*omega3

        V = np.array([Vx,Vy,Vz])
        P = np.array([Px,Py,Pz])
        return P,V

Theta = np.array([np.pi,np.pi/6,-np.pi/4])
Omega = np.array([0.1,-0.05,-0.05])
