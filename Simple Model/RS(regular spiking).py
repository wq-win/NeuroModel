# the original code was written by izhikevich in MATLAB
import matplotlib.pyplot as plt
import numpy as np

# parameters used for RS
C = 100
vr = -60
vt = -40
k = 0.7

# neocortical pyramidal neurons
a = 0.03
b = -2
c = -50
d = 100

# spike cutoff
v_peak = 35

# time span and step(ms)
T = 1000
tau = 1

# number of simulation steps
n = round(T / tau)

# initial values
v = vr * np.ones(n)
u = 0 * v

# pulse of input DC method
I1 = np.zeros(int(0.1 * n))
I2=70 * np.ones(int(0.9 * n))
I = np.append(I1,I2)

# forward Euler method
t = np.arange(1, n - 1, 1)
for i in t:
    v[i + 1] = v[i] + tau * (k * (v[i] - vr) * (v[i] - vt) - u[i] + I[i]) / C
    u[i + 1] = u[i] + tau * a * (b * (v[i] - vr) - u[i])
    if v[i + 1] >= v_peak:  # a spike is fired
        v[i] = v_peak  # padding the spike amplitude
        v[i + 1] = c  # membrane voltage reset
        u[i + 1] = u[i + 1] + d  # recovery variable update


# plot the result
x=np.linspace(1,T,1000)
# fig, (ax1,ax2)=plt.subplots(2,1,sharex=True)
# ax1.plot(np.linspace(1, T, 1000), v)
# ax2.plot(np.linspace(1,T,1000),I,label='input')
grid = plt.GridSpec(4,1)
plt.subplot(grid[0:3,0])
plt.plot(x, v)
plt.subplot(grid[3,0])
plt.plot(x,I)
plt.show()
