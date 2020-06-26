import numpy as np
import matplotlib.pyplot as plt


minutes = np.array([20,19,18,18,17,17,17,16])
seconds = np.array([0,0.,23.,8.,54.,29.,3.,25])

runs = minutes +seconds/60.
time = np.linspace(1,len(runs)+1, len(runs))
before_flex = np.ones(len(time)+3)*20
goal = np.ones(len(time)+3)*16.5
time_v2 = np.linspace(1,len(before_flex)+1, len(before_flex))

plt.plot(time_v2,before_flex, 'r')
plt.plot(time,runs,'-*')
plt.plot(time_v2, goal, 'g')
plt.legend(['average time before summer', "progress this semester", "goal this semester" ], loc = "best")
plt.xlabel("number of runs")
plt.title("Run times for this semester. Distance =  3.258 km ")
plt.ylabel("time of runs [minutes]")
plt.axis([0.5,10,16,20.1])
plt.grid("on")
plt.show()
