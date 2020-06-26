import numpy as np

x_0 = 170 # km

def height_v1(H_1,z_1,H_2,z_2):
    I_1 = np.arctan(z_1/H_1)+ np.pi
    I_2 = np.arctan(z_2/H_2) + np.pi
    print("I1 = ",I_1*180/np.pi,"I2=",I_2*180/np.pi)
    h = x_0*(1/((1/np.tan(270-I_1))+(1/np.tan(I_2 -90))))
    return h


def height_v2(H_1,z_1,H_2,z_2):
    I_1 = np.arctan(z_1/H_1) + np.pi
    I_2 = np.arctan(z_2/H_2) + np.pi
    print("I1 = ",I_1*180/np.pi,"I2=",I_2*180/np.pi)
    x_p = x_0 *np.tan(270 -I_2)/(np.tan(270 - I_2)+np.tan(270-I_1))
    print("x_p =", x_p)
    h = x_p*np.tan(270- I_1)
    return h



print (height_v1(-327,-102,-270,160))
print ("h2=",height_v2(-327,-102,-270,160))
