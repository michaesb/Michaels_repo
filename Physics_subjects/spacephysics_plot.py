import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

phi1 = np.array([47,52,46,52,51,50,49,47,50,51,51,47,49,53,53,32,38,42,37]) #from 14:30 until 17:30
phi2 = np.array([46,44,44,42,43,52,51,47,46,44,47]) #17:40 until 19:20
phi3 = np.array([43,36,34,33,35,39,37,34,36,36,31,32,43,36,37,37,35,34,37,]) #from 19:30 until 24:0

cap_size1 = np.array([69,59,68,68,65,62,64,63,68,68,66,63,61,61,67,68,68,69,70]) #same structure as phi
cap_size2 = np.array([69,68,69,68,68,67,67,68,68,68,68])
cap_size3 = np.array([68,68,66,66,65,65,67,67,68,68,68,68,67,69,68,68,68,66,68,68,68,70,68,70,69,71,69,69])
time = np.linspace(14.5,24.,58)
Phi_s = np.concatenate((phi1,phi2,phi3))
Polar_cap = np.concatenate((cap_size1, cap_size2, cap_size3))
print np.median(Polar_cap[3:])
def specific_times_plot():
    """
    fig, axis = plt.subplots(2,1)
    axis[0].plot(time,Phi_s, 'r')
    axis[0].plot(time,Phi_s, 'r*')
    axis[0].set_title(r' $\Phi$ maximum potential difference')
    axis[1].plot(time,Polar_cap, 'b')
    axis[1].plot(time,Polar_cap, 'b*')
    axis[1].set_title('Polar cap size given in degrees')
    axis[1].set_xlabel('time of the day')
    axis[0].set_ylabel('Potential [kV]')
    axis[1].set_ylabel('Polar cap size given in Latitude ['+u'\N{DEGREE SIGN}'+']')
    plt.show()
    plt.plot(time,Phi_s, 'r')
    plt.plot(time,Phi_s, 'r*')
    plt.title(r' $\Phi$ maximum potential difference')
    plt.xlabel('time of day')
    plt.ylabel('Potential [kV]')
    plt.show()
    """
    times = np.linspace(15,24,10)
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    plt.plot(time[3:],Polar_cap[3:], 'b', linewidth=0.8)
    plt.plot(time[3:],Polar_cap[3:], 'b*')
    ax.grid(True)
    ax.set_xticks(times)
    plt.title('Polar cap boundary in latitude over time')
    plt.xlabel('time of the day [UT]')
    plt.ylabel('Latitude ['+u'\N{DEGREE SIGN}'+']')
    plt.show()

specific_times_plot()

def full_day_plot():
    Phi = np.array([46,41,32,43,56,39,44,53,51,53,51,52,48,\
                    44,53,52,51,32,44,46,33,36,37,33,31]) #kV

    Lambda = np.array([68,59,64,70,64,64,74,75,71,68,71,71,74,\
                       72,70,68,68,68,69,68,66,68,68,70,69]) #degrees
    t = np.linspace(0,24,25)
    fig, axis = plt.subplots(2,1)
    axis[0].plot(t,Phi)
    axis[0].set_title('difference of charges between the area in the poles')
    axis[1].plot(t,Lambda)
    axis[1].set_title('The size of the polar cap given in degrees latitude')
    plt.show()


def very_specific_time_plot():
    hour_base = np.linspace(0,.56,15)
    time = []
    for i in range(19,21):
        hour = i + hour_base
        print (hour_base)
        print (hour)
        time.extend(hour)
    time.append(21)
    Lambda = np.array([68,68,68,68,68,68,68,68,68,67,68,67,66,66,66,66,65,65,65,65,65,67,67,65,67,67,68,68,68,68,68])
    fig, ax = plt.subplots()
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.plot(time,Lambda, 'b',linewidth=0.8)
    plt.xlabel('time of the day')
    plt.ylabel('Polar cap size given in Latitude ['+u'\N{DEGREE SIGN}'+']')
    plt.plot(time,Lambda, 'b*')
    plt.grid(True)
    plt.show()

def another_very_specific_time_plot():
    hour_base = np.linspace(0,.56,15)
    time = []
    for i in range(17,19):
        hour = i + hour_base
        print (hour_base)
        print (hour)
        time.extend(hour)
    time.append(19)
    Lambda = np.array([68,66,68,68,68,69,69,70,70,69,69,69,68,68,68,69,70,69,68,68,68,68,68,66,65,67,68,68,68,68,68])
    fig, ax = plt.subplots()
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.plot(time,Lambda, 'b',linewidth=0.8)
    plt.xlabel('time of the day')
    plt.ylabel('Polar cap size given in Latitude ['+u'\N{DEGREE SIGN}'+']')
    plt.plot(time,Lambda, 'b*')
    plt.grid(True)
    plt.show()

"""
plt.subplot(2,2)
plt.plot(t,Lambda, 'r')
plt.plot(t,Lambda, '*r')
plt.title('Lambda')
plt.show()
plt.title('N_vc')
plt.plot(t, N_vc, 'y')
plt.plot(t, N_vc,'*y')
plt.show()
"""
