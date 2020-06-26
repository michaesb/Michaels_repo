import numpy as np
import matplotlib.pyplot as plt
from tcp_latency import measure_latency
from pythonping import ping
from progressbar import progress_bar
import time

n = 3*10**2
pings = -np.ones(n)


t1 = time.time()
for i in range(n):
    progress_bar(i,n)
    measure_latency(host='amazon.com')
    pings[i] =measure_latency(host='8.8.8.8', port=443, runs=1, timeout=2.5)[0]
    print(pings[i])
t2 = time.time()
t = np.linspace(0, t2-t1,n)/60
plt.plot(t,pings)
plt.title("Latency over "+ str(int((t2-t1)/60)) +"minutes")
plt.xlabel("minutes")
plt.ylabel("latency")
plt.grid("on")
plt.show()
