import numpy as np

L1 = 100.9 #mm
L2 = 222.1 #mm
L3 = 136.2 #mm

def jacobian(theta,omega):
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

Theta = np.array([3*np.pi/2,np.pi/6,-np.pi/4])
Omega = np.array([0.1,0.05,0.05]) #negative because


print (Jacobian(Theta, Omega))
